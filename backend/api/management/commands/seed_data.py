from django.core.management.base import BaseCommand
from api.models import Badge, Unit, Task, TaskQuestion, Vocabulary, MedicalIdiom, PhrasalVerb

# Import all unit data
from .seed_data1 import UNIT_1_DATA
from .seed_data2 import UNIT_2_DATA
from .seed_data3 import UNIT_3_DATA
from .seed_data4 import UNIT_4_DATA
from .seed_data5 import UNIT_5_DATA
from .seed_data6 import UNIT_6_DATA
from .seed_data7 import UNIT_7_DATA
from .seed_data8 import UNIT_8_DATA
from .seed_data9 import UNIT_9_DATA
from .seed_data10 import UNIT_10_DATA
from .seed_data11 import UNIT_11_DATA
from .seed_data12 import UNIT_12_DATA
from .seed_data13 import UNIT_13_DATA
from .seed_data14 import UNIT_14_DATA
from .seed_data15 import UNIT_15_DATA


class Command(BaseCommand):
    help = 'Seed database with all 15 units data'

    def handle(self, *args, **options):
        self.stdout.write('🚀 Seeding database with all 15 units...\n')
        
        # All unit data in order
        ALL_UNITS_DATA = [
            UNIT_1_DATA,
            UNIT_2_DATA,
            UNIT_3_DATA,
            UNIT_4_DATA,
            UNIT_5_DATA,
            UNIT_6_DATA,
            UNIT_7_DATA,
            UNIT_8_DATA,
            UNIT_9_DATA,
            UNIT_10_DATA,
            UNIT_11_DATA,
            UNIT_12_DATA,
            UNIT_13_DATA,
            UNIT_14_DATA,
            UNIT_15_DATA,
        ]
        
        # Create badges
        self.create_badges()
        
        # Create units
        self.create_units(ALL_UNITS_DATA)
        
        # Create tasks and questions for each unit
        self.create_tasks_and_questions(ALL_UNITS_DATA)
        
        # Create vocabulary, idioms, phrasal verbs
        self.create_vocabulary()
        self.create_idioms()
        self.create_phrasal_verbs()
        
        self.stdout.write(self.style.SUCCESS('\n✅ Database seeded successfully with all 15 units!'))
        self.stdout.write(self.style.SUCCESS(f'   📚 Units: 15'))
        self.stdout.write(self.style.SUCCESS(f'   📝 Tasks: {Task.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'   ❓ Questions: {TaskQuestion.objects.count()}'))
    
    def create_badges(self):
        """Create achievement badges"""
        Badge.objects.all().delete()
        badges = [
            {'name': 'Boshlang\'ich', 'description': 'Birinchi topshiriqni bajardingiz', 'icon': '🎯', 'requirement': 'first_task'},
            {'name': 'Faol', 'description': '10 ta topshiriq bajardingiz', 'icon': '⭐', 'requirement': '10_tasks'},
            {'name': 'Ustoz', 'description': '50 ta topshiriq bajardingiz', 'icon': '🏆', 'requirement': '50_tasks'},
            {'name': 'Mukammal', 'description': '100% natija oldingiz', 'icon': '💯', 'requirement': 'perfect_score'},
            {'name': 'Izchil', 'description': '7 kun ketma-ket o\'qidingiz', 'icon': '🔥', 'requirement': '7_day_streak'},
            {'name': 'Polyglot', 'description': 'Barcha mavzularni tugatdingiz', 'icon': '🌟', 'requirement': 'all_units'},
        ]
        for b in badges:
            Badge.objects.create(**b)
        self.stdout.write(self.style.SUCCESS('✓ Badges created'))
    
    def create_units(self, all_units_data):
        """Create all 15 units"""
        Unit.objects.all().delete()
        
        for unit_data in all_units_data:
            unit_info = unit_data['unit']
            Unit.objects.create(
                number=unit_info['number'],
                title=unit_info['title'],
                description=unit_info['description']
            )
        
        self.stdout.write(self.style.SUCCESS('✓ Units created (15)'))
    
    def create_tasks_and_questions(self, all_units_data):
        """Create tasks and questions for all units"""
        Task.objects.all().delete()
        TaskQuestion.objects.all().delete()
        
        # Task templates - 13 tasks per unit
        task_templates = [
            {'number': 1, 'title': 'Fill in the blanks', 'task_type': 'fill_blank', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Fill in the blanks with the correct form.'},
            {'number': 2, 'title': 'Identify / Choose', 'task_type': 'multiple_choice', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Choose the correct answer from the options.'},
            {'number': 3, 'title': 'Change the form', 'task_type': 'fill_blank', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Change to the correct form.'},
            {'number': 4, 'title': 'Choose the correct answer', 'task_type': 'multiple_choice', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Choose the correct answer from the options.'},
            {'number': 5, 'title': 'Read and translate', 'task_type': 'translation', 'points': 15, 'is_ai_evaluated': True, 'instruction': 'Read the text and translate it into Uzbek.'},
            {'number': 6, 'title': 'Topical vocabulary', 'task_type': 'fill_blank', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Inglizcha so\'zning o\'zbekcha tarjimasini yozing.'},
            {'number': 7, 'title': 'Match definitions', 'task_type': 'matching', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Match the words with their definitions.'},
            {'number': 8, 'title': 'Complete / Answer', 'task_type': 'fill_blank', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Complete the sentences or answer questions.'},
            {'number': 9, 'title': 'Find synonyms / Match', 'task_type': 'synonyms', 'points': 15, 'is_ai_evaluated': True, 'instruction': 'Find synonyms or match items.'},
            {'number': 10, 'title': 'Conversation questions', 'task_type': 'conversation', 'points': 15, 'is_ai_evaluated': True, 'instruction': 'Answer the conversation questions in English.'},
            {'number': 11, 'title': 'Speaking practice', 'task_type': 'speaking', 'points': 20, 'is_ai_evaluated': True, 'instruction': 'Speak on the given topic for 2 minutes.'},
            {'number': 12, 'title': 'Writing task', 'task_type': 'writing', 'points': 20, 'is_ai_evaluated': True, 'instruction': 'Write on the given topic (150-200 words).'},
            {'number': 13, 'title': 'Video retelling', 'task_type': 'video', 'points': 20, 'is_ai_evaluated': True, 'instruction': 'Watch the video and retell what it is about.'},
        ]
        
        total_questions = 0
        
        for unit_data in all_units_data:
            unit_number = unit_data['unit']['number']
            unit = Unit.objects.get(number=unit_number)
            tasks_data = unit_data.get('tasks', {})
            video_url = unit_data.get('video_url', '')
            
            self.stdout.write(f'  📖 Unit {unit_number}: {unit.title}')
            
            for template in task_templates:
                task_number = template['number']
                
                # Create task
                task_info = template.copy()
                
                # Add video URL for task 13
                if task_number == 13 and video_url:
                    task_info['content'] = {'video_url': video_url}
                
                task = Task.objects.create(unit=unit, **task_info)
                
                # Get questions for this task
                questions = tasks_data.get(task_number, [])
                
                for idx, q_data in enumerate(questions):
                    question_text = q_data[0]
                    correct_answer = q_data[1]
                    options = q_data[2] if len(q_data) > 2 else None
                    
                    TaskQuestion.objects.create(
                        task=task,
                        question_text=question_text,
                        correct_answer=correct_answer,
                        options=options,
                        order=idx + 1
                    )
                    total_questions += 1
            
            self.stdout.write(self.style.SUCCESS(f'     ✓ 13 tasks created'))
        
        self.stdout.write(self.style.SUCCESS(f'✓ All tasks and questions created ({total_questions} questions)'))
    
    def create_vocabulary(self):
        """Create medical vocabulary"""
        Vocabulary.objects.all().delete()
        vocab = [
            {'word': 'Abdomen', 'translation': 'Qorin', 'definition': 'The part of the body below the chest containing digestive organs'},
            {'word': 'Anesthesia', 'translation': 'Anesteziya', 'definition': 'Loss of sensation, especially to pain'},
            {'word': 'Biopsy', 'translation': 'Biopsiya', 'definition': 'Removal of tissue for examination'},
            {'word': 'Cardiac', 'translation': 'Yurakka oid', 'definition': 'Relating to the heart'},
            {'word': 'Diagnosis', 'translation': 'Tashxis', 'definition': 'Identification of a disease or condition'},
            {'word': 'Emergency', 'translation': 'Shoshilinch', 'definition': 'A serious, unexpected situation requiring immediate action'},
            {'word': 'Fracture', 'translation': 'Sinish', 'definition': 'A break in a bone'},
            {'word': 'Hemorrhage', 'translation': 'Qon ketish', 'definition': 'Severe bleeding'},
            {'word': 'Injection', 'translation': 'Ukol', 'definition': 'Administration of medicine by needle'},
            {'word': 'Laboratory', 'translation': 'Laboratoriya', 'definition': 'A place for scientific testing'},
            {'word': 'Malignant', 'translation': 'Xavfli', 'definition': 'Cancerous or very harmful'},
            {'word': 'Nausea', 'translation': 'Ko\'ngil aynish', 'definition': 'Feeling of sickness with urge to vomit'},
            {'word': 'Outpatient', 'translation': 'Ambulatoriya bemori', 'definition': 'A patient who visits but does not stay overnight'},
            {'word': 'Prescription', 'translation': 'Retsept', 'definition': 'A doctor\'s written order for medicine'},
            {'word': 'Quarantine', 'translation': 'Karantin', 'definition': 'Isolation to prevent spread of disease'},
            {'word': 'Radiology', 'translation': 'Radiologiya', 'definition': 'Medical imaging using X-rays'},
            {'word': 'Surgery', 'translation': 'Jarrohlik', 'definition': 'Medical treatment involving operations'},
            {'word': 'Therapy', 'translation': 'Terapiya', 'definition': 'Treatment of disease or disorder'},
            {'word': 'Ultrasound', 'translation': 'Ultratovush', 'definition': 'Imaging using sound waves'},
            {'word': 'Vaccine', 'translation': 'Vaksina', 'definition': 'Substance to produce immunity to disease'},
        ]
        for v in vocab:
            Vocabulary.objects.create(**v)
        self.stdout.write(self.style.SUCCESS(f'✓ Vocabulary created ({len(vocab)} words)'))
    
    def create_idioms(self):
        """Create medical idioms"""
        MedicalIdiom.objects.all().delete()
        idioms = [
            {'idiom': 'A clean bill of health', 'meaning': 'A report that confirms good health', 'example': 'The doctor gave him a clean bill of health after the checkup.'},
            {'idiom': 'Under the weather', 'meaning': 'Feeling slightly ill', 'example': 'I\'m feeling a bit under the weather today.'},
            {'idiom': 'Go under the knife', 'meaning': 'Have surgery', 'example': 'She had to go under the knife to remove her appendix.'},
            {'idiom': 'A bitter pill to swallow', 'meaning': 'Something unpleasant that must be accepted', 'example': 'Losing the job was a bitter pill to swallow.'},
            {'idiom': 'An apple a day keeps the doctor away', 'meaning': 'Eating healthy prevents illness', 'example': 'Remember, an apple a day keeps the doctor away!'},
            {'idiom': 'Be on the mend', 'meaning': 'Recovering from illness', 'example': 'After a week in bed, he\'s finally on the mend.'},
            {'idiom': 'Fit as a fiddle', 'meaning': 'In very good health', 'example': 'Despite his age, grandfather is fit as a fiddle.'},
            {'idiom': 'In the pink of health', 'meaning': 'In excellent health', 'example': 'After the treatment, she\'s in the pink of health.'},
            {'idiom': 'Sick and tired', 'meaning': 'Very annoyed or bored', 'example': 'I\'m sick and tired of waiting in long queues.'},
            {'idiom': 'Take a turn for the worse', 'meaning': 'Become more ill', 'example': 'The patient took a turn for the worse overnight.'},
        ]
        for i in idioms:
            MedicalIdiom.objects.create(**i)
        self.stdout.write(self.style.SUCCESS(f'✓ Idioms created ({len(idioms)} idioms)'))
    
    def create_phrasal_verbs(self):
        """Create medical phrasal verbs"""
        PhrasalVerb.objects.all().delete()
        pvs = [
            {'verb': 'Break out', 'meaning': 'To suddenly develop (a rash, disease)', 'example': 'She broke out in hives after eating shellfish.'},
            {'verb': 'Come down with', 'meaning': 'To become ill with', 'example': 'He came down with the flu last week.'},
            {'verb': 'Pass out', 'meaning': 'To lose consciousness', 'example': 'She passed out from the heat.'},
            {'verb': 'Throw up', 'meaning': 'To vomit', 'example': 'The patient threw up after taking the medication.'},
            {'verb': 'Get over', 'meaning': 'To recover from illness', 'example': 'It took her two weeks to get over the cold.'},
            {'verb': 'Come round/to', 'meaning': 'To regain consciousness', 'example': 'He came round after a few minutes.'},
            {'verb': 'Fight off', 'meaning': 'To resist an illness', 'example': 'Her immune system fought off the infection.'},
            {'verb': 'Flare up', 'meaning': 'To suddenly become worse', 'example': 'His arthritis flared up in cold weather.'},
            {'verb': 'Run down', 'meaning': 'To become weak or exhausted', 'example': 'Working too hard has run him down.'},
            {'verb': 'Swell up', 'meaning': 'To become swollen', 'example': 'Her ankle swelled up after the fall.'},
        ]
        for p in pvs:
            PhrasalVerb.objects.create(**p)
        self.stdout.write(self.style.SUCCESS(f'✓ Phrasal verbs created ({len(pvs)} verbs)'))
