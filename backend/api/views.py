from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.utils import timezone
import unicodedata
import re

from .models import Badge, UserBadge, Unit, Task, TaskQuestion, UserProgress, Vocabulary, MedicalIdiom, PhrasalVerb
from .serializers import (
    UserSerializer, RegisterSerializer, BadgeSerializer, UserBadgeSerializer,
    UnitSerializer, UnitListSerializer, TaskSerializer, TaskListSerializer,
    UserProgressSerializer, VocabularySerializer, MedicalIdiomSerializer, PhrasalVerbSerializer, LeaderboardSerializer
)
from .services import AIService

User = get_user_model()


def normalize_answer(text):
    """Normalize text for comparison - handles apostrophes, quotes, spaces, case-insensitive"""
    if not text:
        return ''
    
    # Convert to string and lowercase
    text = str(text).lower().strip()
    
    # Normalize unicode characters
    text = unicodedata.normalize('NFKC', text)
    
    # Replace ALL apostrophe/quote variants with standard ASCII apostrophe (0x27)
    # Using unicode code points for reliability
    apostrophe_chars = [
        '\u0027',  # ' APOSTROPHE (standard)
        '\u0060',  # ` GRAVE ACCENT (backtick)
        '\u00b4',  # ´ ACUTE ACCENT
        '\u2018',  # ' LEFT SINGLE QUOTATION MARK
        '\u2019',  # ' RIGHT SINGLE QUOTATION MARK (most common issue!)
        '\u201a',  # ‚ SINGLE LOW-9 QUOTATION MARK
        '\u201b',  # ‛ SINGLE HIGH-REVERSED-9 QUOTATION MARK
        '\u2032',  # ′ PRIME
        '\u2035',  # ‵ REVERSED PRIME
        '\u02b9',  # ʹ MODIFIER LETTER PRIME
        '\u02bb',  # ʻ MODIFIER LETTER TURNED COMMA (O'zbek)
        '\u02bc',  # ʼ MODIFIER LETTER APOSTROPHE
        '\u02bd',  # ʽ MODIFIER LETTER REVERSED COMMA
        '\u02c8',  # ˈ MODIFIER LETTER VERTICAL LINE
        '\u02ca',  # ˊ MODIFIER LETTER ACUTE ACCENT
        '\u02cb',  # ˋ MODIFIER LETTER GRAVE ACCENT
        '\u0022',  # " QUOTATION MARK
        '\u201c',  # " LEFT DOUBLE QUOTATION MARK
        '\u201d',  # " RIGHT DOUBLE QUOTATION MARK
        '\u00ab',  # « LEFT GUILLEMET
        '\u00bb',  # » RIGHT GUILLEMET
    ]
    
    for ap in apostrophe_chars:
        text = text.replace(ap, "'")
    
    # O'zbek tilidagi o' va g' uchun turli variantlar
    text = text.replace("o'", "o'")
    text = text.replace("g'", "g'")
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove leading/trailing punctuation that might cause issues
    text = text.strip('.,;:!?')
    
    return text


def answers_match(user_answer, correct_answer):
    """Check if user answer matches correct answer with flexible comparison"""
    user_norm = normalize_answer(user_answer)
    correct_norm = normalize_answer(correct_answer)
    
    # Direct match
    if user_norm == correct_norm:
        return True
    
    # Try without apostrophes at all
    user_no_apos = user_norm.replace("'", "").replace("'", "")
    correct_no_apos = correct_norm.replace("'", "").replace("'", "")
    if user_no_apos == correct_no_apos:
        return True
    
    return False


class RegisterView(generics.CreateAPIView):
    """User registration"""
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    authentication_classes = []


class ProfileView(generics.RetrieveUpdateAPIView):
    """User profile"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user


class DashboardView(APIView):
    """Dashboard stats"""
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        
        # Calculate stats
        total_tasks = Task.objects.count()
        completed = UserProgress.objects.filter(user=user, completed=True).count()
        
        # Recent activity
        recent = UserProgress.objects.filter(
            user=user, completed=True
        ).select_related('task').order_by('-completed_at')[:5]
        
        return Response({
            'user': UserSerializer(user).data,
            'stats': {
                'total_tasks': total_tasks,
                'completed_tasks': completed,
                'progress_percent': round((completed / total_tasks * 100) if total_tasks else 0),
            },
            'recent_activity': [
                {
                    'task': p.task.title,
                    'score': p.score,
                    'date': p.completed_at
                } for p in recent
            ]
        })


class UnitViewSet(viewsets.ReadOnlyModelViewSet):
    """Units API"""
    queryset = Unit.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return UnitListSerializer
        return UnitSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    """Tasks API"""
    queryset = Task.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        return TaskSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def submit(self, request, pk=None):
        """Submit task answers"""
        task = self.get_object()
        answers = request.data.get('answers', {})
        
        # AI-evaluated tasks
        if task.is_ai_evaluated:
            result = AIService.evaluate(task, answers)
            score = result['score']
            feedback = result['feedback']
        else:
            # Manual evaluation with flexible comparison
            correct = 0
            total = task.questions.count()
            
            for question in task.questions.all():
                user_answer = answers.get(str(question.id), '')
                # Support multiple correct answers separated by comma
                correct_answers = [a.strip() for a in question.correct_answer.split(',')]
                
                # Check if user answer matches any correct answer
                for correct_ans in correct_answers:
                    if answers_match(user_answer, correct_ans):
                        correct += 1
                        break
            
            score = round((correct / total * 100) if total else 0)
            feedback = f"To'g'ri javoblar: {correct}/{total}"
        
        # Update progress
        progress, _ = UserProgress.objects.get_or_create(user=request.user, task=task)
        progress.score = max(progress.score, score)
        progress.attempts += 1
        
        if score >= 60:
            if not progress.completed:
                request.user.add_points(task.points)
            progress.completed = True
            progress.completed_at = timezone.now()
        
        progress.save()
        
        # Update streak
        user = request.user
        today = timezone.now().date()
        if user.last_activity != today:
            if user.last_activity == today - timezone.timedelta(days=1):
                user.streak += 1
            else:
                user.streak = 1
            user.last_activity = today
            user.save()
        
        return Response({
            'score': score,
            'feedback': feedback,
            'passed': score >= 60,
            'points_earned': task.points if score >= 60 and progress.attempts == 1 else 0
        })


class VocabularyViewSet(viewsets.ReadOnlyModelViewSet):
    """Vocabulary API"""
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        unit = self.request.query_params.get('unit')
        if unit:
            queryset = queryset.filter(unit_id=unit)
        return queryset


class MedicalIdiomViewSet(viewsets.ReadOnlyModelViewSet):
    """Medical idioms API"""
    queryset = MedicalIdiom.objects.all()
    serializer_class = MedicalIdiomSerializer


class PhrasalVerbViewSet(viewsets.ReadOnlyModelViewSet):
    """Phrasal verbs API"""
    queryset = PhrasalVerb.objects.all()
    serializer_class = PhrasalVerbSerializer


class LeaderboardView(generics.ListAPIView):
    """Top users by points"""
    serializer_class = LeaderboardSerializer
    queryset = User.objects.order_by('-points')[:50]


class BadgeViewSet(viewsets.ReadOnlyModelViewSet):
    """Badges API"""
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer


class UserBadgesView(generics.ListAPIView):
    """User's earned badges"""
    serializer_class = UserBadgeSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return UserBadge.objects.filter(user=self.request.user)
