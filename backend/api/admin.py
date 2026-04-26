from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Badge, UserBadge, Unit, Task, TaskQuestion, UserProgress, Vocabulary, MedicalIdiom, PhrasalVerb


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'points', 'level', 'streak']
    list_filter = ['level', 'is_staff']
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Progress', {'fields': ('avatar', 'points', 'level', 'streak', 'last_activity')}),
    )


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'requirement']


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['number', 'title']


class TaskQuestionInline(admin.TabularInline):
    model = TaskQuestion
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['number', 'unit', 'title', 'task_type', 'points', 'is_ai_evaluated']
    list_filter = ['unit', 'task_type', 'is_ai_evaluated']
    inlines = [TaskQuestionInline]


@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ['word', 'translation', 'unit']
    list_filter = ['unit']


@admin.register(MedicalIdiom)
class MedicalIdiomAdmin(admin.ModelAdmin):
    list_display = ['idiom']
    search_fields = ['idiom', 'meaning']


@admin.register(PhrasalVerb)
class PhrasalVerbAdmin(admin.ModelAdmin):
    list_display = ['verb']
    search_fields = ['verb', 'meaning']


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'task', 'score', 'completed']
    list_filter = ['completed']
