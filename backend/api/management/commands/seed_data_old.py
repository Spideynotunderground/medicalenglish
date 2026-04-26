from django.core.management.base import BaseCommand
from api.models import Badge, Unit, Task, TaskQuestion, Vocabulary, MedicalIdiom, PhrasalVerb


class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        # Badges
        Badge.objects.all().delete()
        badges = [
            {'name': 'Boshlang\'ich', 'description': 'Birinchi topshiriqni bajardingiz', 'icon': '🎯', 'requirement': 'first_task'},
            {'name': 'Faol', 'description': '10 ta topshiriq bajardingiz', 'icon': '⭐', 'requirement': '10_tasks'},
            {'name': 'Ustoz', 'description': '50 ta topshiriq bajardingiz', 'icon': '🏆', 'requirement': '50_tasks'},
            {'name': 'Mukammal', 'description': '100% natija oldingiz', 'icon': '💯', 'requirement': 'perfect_score'},
            {'name': 'Izchil', 'description': '7 kun ketma-ket o\'qidingiz', 'icon': '🔥', 'requirement': '7_day_streak'},
        ]
        for b in badges:
            Badge.objects.create(**b)
        self.stdout.write(self.style.SUCCESS('✓ Badges'))
        
        # Units
        Unit.objects.all().delete()
        units = [
            {'number': 1, 'title': 'Simple Tenses in the Active Voice', 'description': 'Present Simple, Past Simple, Future Simple'},
            {'number': 2, 'title': 'Continuous Tenses in the Active Voice', 'description': 'Present, Past, Future Continuous'},
            {'number': 3, 'title': 'Perfect Tenses in the Active Voice', 'description': 'Present, Past, Future Perfect'},
            {'number': 4, 'title': 'Perfect Continuous Tenses in the Active Voice', 'description': 'Present, Past, Future Perfect Continuous'},
            {'number': 5, 'title': 'Simple Tenses in the Passive Voice', 'description': 'Present, Past, Future Simple Passive'},
            {'number': 6, 'title': 'Continuous Tenses in the Passive Voice', 'description': 'Present, Past Continuous Passive'},
            {'number': 7, 'title': 'Perfect Tenses in the Passive Voice', 'description': 'Present, Past, Future Perfect Passive'},
            {'number': 8, 'title': 'Sequence of Tenses', 'description': 'Rules of tense agreement'},
            {'number': 9, 'title': 'Direct and Reported Speech', 'description': 'Changing direct to reported speech'},
            {'number': 10, 'title': 'Direct Interrogative and Imperative Speech', 'description': 'Reported questions and commands'},
            {'number': 11, 'title': 'Subjunctive Mood', 'description': 'Wishes and hypothetical situations'},
            {'number': 12, 'title': 'Indicative and Imperative Mood', 'description': 'Statements and commands'},
            {'number': 13, 'title': 'Gerund', 'description': 'Verb forms ending in -ing as nouns'},
            {'number': 14, 'title': 'Infinitive', 'description': 'Base form of verb with "to"'},
            {'number': 15, 'title': 'Participle', 'description': 'Present and past participles'},
        ]
        for u in units:
            Unit.objects.create(**u)
        self.stdout.write(self.style.SUCCESS('✓ Units'))
        
        # Delete old tasks and questions first
        Task.objects.all().delete()
        
        # Tasks - 13 per unit
        tasks = [
            {'number': 1, 'title': 'Fill in the blanks', 'task_type': 'fill_blank', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Fill in the blanks with the correct form of the verb in brackets.'},
            {'number': 2, 'title': 'Identify the tense', 'task_type': 'multiple_choice', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Identify the tense used in each sentence.'},
            {'number': 3, 'title': 'Change the form', 'task_type': 'fill_blank', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Change the verb in brackets to the correct form.'},
            {'number': 4, 'title': 'Choose the correct answer', 'task_type': 'multiple_choice', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Choose the correct answer from the options.'},
            {'number': 5, 'title': 'Read and translate', 'task_type': 'translation', 'points': 15, 'is_ai_evaluated': True, 'instruction': 'Read the text and translate it into Uzbek.'},
            {'number': 6, 'title': 'Topical vocabulary', 'task_type': 'matching', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Match the English words with their Uzbek translations.'},
            {'number': 7, 'title': 'Match the words', 'task_type': 'matching', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Match the words with their definitions.'},
            {'number': 8, 'title': 'Complete the sentences', 'task_type': 'fill_blank', 'points': 10, 'is_ai_evaluated': False, 'instruction': 'Complete the sentences with appropriate words.'},
            {'number': 9, 'title': 'Find synonyms', 'task_type': 'synonyms', 'points': 15, 'is_ai_evaluated': True, 'instruction': 'Find synonyms for the given words from the text.'},
            {'number': 10, 'title': 'Conversation questions', 'task_type': 'conversation', 'points': 15, 'is_ai_evaluated': True, 'instruction': 'Answer the conversation questions in English.'},
            {'number': 11, 'title': 'Speaking practice', 'task_type': 'speaking', 'points': 20, 'is_ai_evaluated': True, 'instruction': 'Speak on the given topic for 2 minutes. Your speech will be evaluated by AI.'},
            {'number': 12, 'title': 'Writing task', 'task_type': 'writing', 'points': 20, 'is_ai_evaluated': True, 'instruction': 'Write an essay on the given topic (150-200 words).'},
            {'number': 13, 'title': 'Video retelling', 'task_type': 'video', 'points': 20, 'is_ai_evaluated': True, 'instruction': 'Watch the video and retell what it is about in English.'},
        ]
        
        # Video URLs for Task 13 (unit number -> video URL)
        video_urls = {
            1: 'https://www.youtube.com/watch?v=WaZcBJZCwqA',
            2: 'https://www.youtube.com/watch?v=UAX1boy_3Dc',
            3: 'https://www.youtube.com/watch?v=bFx6WOwXLBE',
            4: 'https://www.youtube.com/watch?v=Ih3-c7s2t70',
            5: 'https://www.youtube.com/watch?v=0b_C9_9BvGM',
            6: 'https://www.youtube.com/watch?v=zFf1y4X_uQc',
            7: 'https://www.youtube.com/watch?v=W1jWWRcmn9M',
            8: 'https://www.youtube.com/watch?v=okCC9LcyxHg',
            9: 'https://www.youtube.com/watch?v=bTK2v8z5fiw',
            10: 'https://www.youtube.com/watch?v=vtm-6uKaY9o',
            11: 'https://www.youtube.com/watch?v=8de2qgqhwQY',
            12: 'https://www.youtube.com/watch?v=yuipF_IE8KI',
            13: 'https://www.youtube.com/watch?v=IDOdBCSkRIQ',
            14: 'https://www.youtube.com/watch?v=WiPy0Pk7MeA',
            15: 'https://www.youtube.com/watch?v=HlCosIGaZR0',
        }
        
        for unit in Unit.objects.all():
            for t in tasks:
                task_data = t.copy()
                # Add video URL for Task 13
                if t['number'] == 13 and unit.number in video_urls:
                    task_data['content'] = {'video_url': video_urls[unit.number]}
                Task.objects.create(unit=unit, **task_data)
        self.stdout.write(self.style.SUCCESS('✓ Tasks'))
        
        # Questions for all units
        self.create_all_questions()
        
        # Vocabulary
        Vocabulary.objects.all().delete()
        vocab = [
            {'word': 'Abdomen', 'translation': 'Qorin', 'definition': 'Body part below chest'},
            {'word': 'Anesthesia', 'translation': 'Anesteziya', 'definition': 'Loss of sensation'},
            {'word': 'Biopsy', 'translation': 'Biopsiya', 'definition': 'Tissue sample removal'},
            {'word': 'Cardiac', 'translation': 'Yurakka oid', 'definition': 'Heart-related'},
            {'word': 'Diagnosis', 'translation': 'Tashxis', 'definition': 'Disease identification'},
            {'word': 'Emergency', 'translation': 'Shoshilinch', 'definition': 'Urgent situation'},
            {'word': 'Fracture', 'translation': 'Sinish', 'definition': 'Broken bone'},
            {'word': 'Hemorrhage', 'translation': 'Qon ketish', 'definition': 'Heavy bleeding'},
            {'word': 'Injection', 'translation': 'Ukol', 'definition': 'Medicine by needle'},
            {'word': 'Laboratory', 'translation': 'Laboratoriya', 'definition': 'Testing place'},
        ]
        for v in vocab:
            Vocabulary.objects.create(**v)
        self.stdout.write(self.style.SUCCESS('✓ Vocabulary'))
        
        # Idioms
        MedicalIdiom.objects.all().delete()
        idioms = [
            {'idiom': 'A clean bill of health', 'meaning': 'Good health report', 'example': 'He got a clean bill of health.'},
            {'idiom': 'Under the weather', 'meaning': 'Feeling ill', 'example': 'I\'m under the weather.'},
            {'idiom': 'Go under the knife', 'meaning': 'Have surgery', 'example': 'She went under the knife.'},
        ]
        for i in idioms:
            MedicalIdiom.objects.create(**i)
        self.stdout.write(self.style.SUCCESS('✓ Idioms'))
        
        # Phrasal verbs
        PhrasalVerb.objects.all().delete()
        pvs = [
            {'verb': 'Break out', 'meaning': 'Suddenly develop', 'example': 'She broke out in hives.'},
            {'verb': 'Come down with', 'meaning': 'Become ill', 'example': 'He came down with flu.'},
            {'verb': 'Pass out', 'meaning': 'Lose consciousness', 'example': 'She passed out.'},
        ]
        for p in pvs:
            PhrasalVerb.objects.create(**p)
        self.stdout.write(self.style.SUCCESS('✓ Phrasal verbs'))
        
        self.stdout.write(self.style.SUCCESS('\n✅ Database seeded successfully!'))
    
    def create_all_questions(self):
        """Create questions for all 15 units, all 13 tasks each"""
        
        # Question data for each unit
        all_questions = {
            1: {  # Simple Tenses
                1: [  # Fill in blanks
                    ('He _____ (receive) a new kidney from his brother.', 'received'),
                    ('He _____ (injure) his back lifting the table.', 'injured'),
                    ('She _____ (recover) from her concussion.', 'recovered'),
                    ('It was so hot that he _____ (faint).', 'fainted'),
                    ('Her condition _____ (require) surgery.', 'required'),
                    ('She _____ (suffer) from poor circulation.', 'suffered'),
                    ('She _____ (respond) well to her diet.', 'responded'),
                    ('The embryo _____ (develop) normally.', 'developed'),
                    ('His tibia _____ (fracture) in two places.', 'fractured'),
                    ('The patient _____ (react) badly to penicillin.', 'reacted'),
                ],
                2: [  # Identify tense (with options)
                    ('Does he go to hospital every day?', 'Present Simple', ['Present Simple', 'Past Simple', 'Future Simple', 'Present Continuous']),
                    ('An apple a day keeps the doctor away.', 'Present Simple', ['Present Simple', 'Past Simple', 'Present Perfect', 'Future Simple']),
                    ('I worked in the hospital for 15 years.', 'Past Simple', ['Present Perfect', 'Past Simple', 'Past Continuous', 'Present Simple']),
                    ('The patient will recover soon.', 'Future Simple', ['Present Simple', 'Future Simple', 'Future Continuous', 'Present Perfect']),
                    ('She takes medicine every morning.', 'Present Simple', ['Present Simple', 'Present Continuous', 'Past Simple', 'Future Simple']),
                    ('The surgeon performed the operation.', 'Past Simple', ['Present Perfect', 'Past Simple', 'Past Perfect', 'Present Simple']),
                    ('They will examine the patient tomorrow.', 'Future Simple', ['Present Simple', 'Future Simple', 'Future Perfect', 'Present Continuous']),
                    ('Water boils at 100 degrees.', 'Present Simple', ['Present Simple', 'Present Continuous', 'Present Perfect', 'Past Simple']),
                ],
                3: [  # Change form
                    ('Murod _____ (be) a salesman.', 'is'),
                    ('Every day he _____ (call) people up.', 'calls'),
                    ('He _____ (offer) them products.', 'offers'),
                    ('Usually he _____ (work) from home.', 'works'),
                    ('Last Monday he _____ (visit) a client.', 'visited'),
                    ('Tomorrow he _____ (start) a new project.', 'will start'),
                    ('Next week they _____ (have) a conference.', 'will have'),
                    ('He _____ (not/like) cold weather.', 'does not like'),
                ],
                4: [  # Multiple choice
                    ('He _____ to school every day.', 'goes', ['go', 'goes', 'going', 'went']),
                    ('She _____ a doctor last year.', 'became', ['becomes', 'become', 'became', 'becoming']),
                    ('They _____ the exam next week.', 'will take', ['take', 'took', 'will take', 'taking']),
                    ('The sun _____ in the east.', 'rises', ['rise', 'rises', 'rose', 'rising']),
                    ('I _____ my homework yesterday.', 'did', ['do', 'does', 'did', 'done']),
                    ('She _____ medicine twice a day.', 'takes', ['take', 'takes', 'took', 'taking']),
                    ('We _____ the doctor tomorrow.', 'will see', ['see', 'saw', 'will see', 'seeing']),
                    ('The patient _____ well last night.', 'slept', ['sleep', 'sleeps', 'slept', 'sleeping']),
                ],
                5: [  # Read and translate (AI)
                    ('Translate: "My name is Aziz. I am a first-year medical student. I want to become a skilled doctor."', 'AI_EVALUATED'),
                    ('Translate: "Every day I attend classes at the medical university. I study anatomy and physiology."', 'AI_EVALUATED'),
                    ('Translate: "Yesterday I visited the hospital for practical training."', 'AI_EVALUATED'),
                ],
                6: [  # Vocabulary
                    ('Higher State Educational Establishment', 'Oliy davlat ta\'lim muassasasi'),
                    ('extra lessons', 'qo\'shimcha darslar'),
                    ('competition', 'musobaqa'),
                    ('deep knowledge', 'chuqur bilim'),
                    ('particular field of medicine', 'tibbiyotning alohida sohasi'),
                    ('skilled doctor', 'malakali shifokor'),
                    ('consider', 'hisobga olish'),
                    ('a good remedy', 'yaxshi davo'),
                    ('fellow-students', 'kursdoshlar'),
                    ('awful', 'dahshatli'),
                    ('hostel', 'yotoqxona'),
                    ('additional medical literature', 'qo\'shimcha tibbiy adabiyotlar'),
                    ('abstracts', 'tezislar'),
                ],
                7: [  # Match definitions - PDF dan
                    ('biology', 'the study of living organisms'),
                    ('medical', 'relating to the science of medicine'),
                    ('disease', 'a disorder of structure or function'),
                    ('histology', 'the study of the microscopic structure of tissues'),
                    ('hospital', 'an institution providing medical treatment'),
                    ('doctor', 'a qualified practitioner of medicine'),
                    ('anatomy', 'the branch of science concerned with bodily structure'),
                    ('textbook', 'a book used for the study of a subject'),
                ],
                8: [  # Complete sentences
                    ('_____ must have deep knowledge of medicine.', 'A good doctor'),
                    ('When I have _____ I watch TV or visit friends.', 'free time'),
                    ('My working day begins _____ because classes start at 8:30.', 'early'),
                    ('Physical exercises are _____ for health protection.', 'necessary'),
                    ('We have several _____ and a lecture every day.', 'practical classes'),
                    ('Medical students _____ that it is not easy to be a specialist.', 'understand'),
                ],
                9: [  # Find synonyms (AI) - har bir so'z alohida
                    ('doctor', 'AI_EVALUATED'),
                    ('illness', 'AI_EVALUATED'),
                    ('medicine', 'AI_EVALUATED'),
                    ('hospital', 'AI_EVALUATED'),
                    ('study', 'AI_EVALUATED'),
                    ('work', 'AI_EVALUATED'),
                    ('help', 'AI_EVALUATED'),
                    ('important', 'AI_EVALUATED'),
                ],
                10: [  # Conversation (AI)
                    ('How old are you?', 'AI_EVALUATED'),
                    ('What would you like to be?', 'AI_EVALUATED'),
                    ('Where are you from?', 'AI_EVALUATED'),
                    ('When were you born?', 'AI_EVALUATED'),
                    ('How many people are in your family?', 'AI_EVALUATED'),
                    ('What is your mother\'s occupation?', 'AI_EVALUATED'),
                    ('Do you have brothers or sisters?', 'AI_EVALUATED'),
                    ('What subjects do you study?', 'AI_EVALUATED'),
                ],
                11: [  # Speaking (AI)
                    ('Talk about your dream job – Doctor. Say: what it is, what it is like, what qualification you need, why it is perfect for you. Speak for 2 minutes.', 'AI_EVALUATED'),
                ],
                12: [  # Writing (AI)
                    ('Write an essay (150-200 words) about "Why I want to become a doctor". Include your motivation, goals, and plans.', 'AI_EVALUATED'),
                ],
                13: [  # Video (AI)
                    ('Watch the video about "A Day in the Life of a Medical Student" and retell what it is about.', 'AI_EVALUATED'),
                ],
            },
            2: {  # Continuous Tenses
                1: [
                    ('The doctor _____ (examine) the patient now.', 'is examining'),
                    ('They _____ (wait) for the results now.', 'are waiting'),
                    ('She _____ (study) when I called her.', 'was studying'),
                    ('The nurse _____ (prepare) the injection now.', 'is preparing'),
                    ('We _____ (work) on a new treatment.', 'are working'),
                    ('The patient _____ (sleep) when the doctor arrived.', 'was sleeping'),
                    ('At 8 PM tomorrow, I _____ (attend) the conference.', 'will be attending'),
                    ('He _____ (recover) well from surgery.', 'is recovering'),
                    ('The surgeons _____ (operate) when the power went out.', 'were operating'),
                    ('She _____ (take) her medication now.', 'is taking'),
                ],
                2: [
                    ('The nurse is checking blood pressure.', 'Present Continuous', ['Present Simple', 'Present Continuous', 'Past Continuous', 'Future Continuous']),
                    ('They were discussing the diagnosis.', 'Past Continuous', ['Present Continuous', 'Past Continuous', 'Past Simple', 'Present Perfect']),
                    ('She will be having surgery tomorrow.', 'Future Continuous', ['Future Simple', 'Future Continuous', 'Present Continuous', 'Future Perfect']),
                    ('The doctors are treating patients today.', 'Present Continuous', ['Present Simple', 'Present Continuous', 'Present Perfect', 'Past Simple']),
                    ('He was recovering when complications appeared.', 'Past Continuous', ['Past Simple', 'Past Continuous', 'Past Perfect', 'Present Continuous']),
                    ('I am waiting for the doctor now.', 'Present Continuous', ['Present Simple', 'Present Continuous', 'Past Continuous', 'Future Simple']),
                    ('They will be performing surgery at noon.', 'Future Continuous', ['Future Simple', 'Future Continuous', 'Present Continuous', 'Future Perfect']),
                ],
                3: [
                    ('This time next week, I _____ (study) for exams.', 'will be studying'),
                    ('At 9 AM tomorrow, the surgeon _____ (perform) the operation.', 'will be performing'),
                    ('Next month, they _____ (work) at the new hospital.', 'will be working'),
                    ('Tomorrow evening, she _____ (attend) a seminar.', 'will be attending'),
                    ('This time next year, he _____ (complete) his residency.', 'will be completing'),
                ],
                4: [
                    ('While I _____ the chart, the doctor came in.', 'was reading', ['read', 'was reading', 'am reading', 'will read']),
                    ('She _____ at the clinic when I saw her.', 'was working', ['works', 'was working', 'is working', 'worked']),
                    ('Look! The nurse _____ the injection.', 'is giving', ['gives', 'gave', 'is giving', 'was giving']),
                    ('They _____ experiments all day today.', 'are conducting', ['conduct', 'conducted', 'are conducting', 'were conducting']),
                ],
                5: [
                    ('Translate: "I am studying medicine at the university. Right now I am learning about the human body."', 'AI_EVALUATED'),
                    ('Translate: "Yesterday at 5 PM, I was attending a lecture on anatomy."', 'AI_EVALUATED'),
                    ('Translate: "Tomorrow at this time, I will be taking an exam."', 'AI_EVALUATED'),
                ],
                6: [  # My future profession vocabulary
                    ('plumber', 'chilangar'),
                    ('to be curious about', 'qiziqtirish'),
                    ('to realize', 'anglamoq'),
                    ('facts about the medication', 'dori haqida faktlar'),
                    ('sick', 'kasal'),
                    ('to feel well', 'yaxshi his qilish'),
                    ('couple of years', 'ikki yil'),
                    ('a dermatologist', 'dermatolog'),
                    ('to take care about', 'g\'amxo\'rlik qilish'),
                    ('skin', 'teri'),
                    ('dermatology', 'dermatologiya'),
                    ('a pediatrician', 'pediatr'),
                    ('noble', 'olijanob'),
                ],
                7: [
                    ('general practitioner', 'a doctor who treats common conditions'),
                    ('surgeon', 'a doctor who performs operations'),
                    ('pediatrician', 'a doctor for children'),
                    ('cardiologist', 'a doctor for heart diseases'),
                    ('neurologist', 'a doctor for nervous system'),
                    ('dermatologist', 'a doctor for skin conditions'),
                    ('psychiatrist', 'a doctor for mental health'),
                    ('anesthesiologist', 'a doctor who gives anesthesia'),
                ],
                8: [
                    ('Maria works as a nurse. She _____ (check) patients now.', 'is checking'),
                    ('Dr. Smith _____ (perform) surgery when the emergency call came.', 'was performing'),
                    ('The team _____ (prepare) for the next operation now.', 'is preparing'),
                    ('While she _____ (study), she also worked part-time.', 'was studying'),
                    ('Tomorrow at this time, they _____ (attend) a conference.', 'will be attending'),
                ],
                9: [
                    ('Find synonyms for: examining, treating, recovering, working', 'AI_EVALUATED'),
                    ('Find synonyms for: doctor, nurse, hospital, patient', 'AI_EVALUATED'),
                ],
                10: [
                    ('What are you studying at medical school?', 'AI_EVALUATED'),
                    ('Why did you choose to become a doctor?', 'AI_EVALUATED'),
                    ('What is your favorite subject?', 'AI_EVALUATED'),
                    ('Are you planning to specialize?', 'AI_EVALUATED'),
                    ('What challenges are you facing?', 'AI_EVALUATED'),
                    ('How do you balance studies and life?', 'AI_EVALUATED'),
                ],
                11: [
                    ('Talk about "My Future Profession". Describe what kind of doctor you want to be, what specialty interests you, and why. Speak for 2 minutes.', 'AI_EVALUATED'),
                ],
                12: [
                    ('Write a Doctor\'s Curriculum Vitae (CV). Include: personal information, education, work experience, skills, and certifications. Use the format provided in the textbook.', 'AI_EVALUATED'),
                ],
                13: [
                    ('Watch the video about medical professions and answer: What different types of doctors did you see? What are their responsibilities?', 'AI_EVALUATED'),
                ],
            },
            3: {  # Perfect Tenses
                1: [
                    ('The doctor _____ (examine) 20 patients today.', 'has examined'),
                    ('She _____ (work) in this hospital since 2010.', 'has worked'),
                    ('They _____ (finish) the operation before noon.', 'had finished'),
                    ('By next year, he _____ (complete) his residency.', 'will have completed'),
                    ('The patient _____ (recover) completely.', 'has recovered'),
                    ('I _____ (never/see) such a case before.', 'have never seen'),
                    ('The nurse _____ (already/give) the injection.', 'has already given'),
                    ('By the time I arrived, the surgery _____ (begin).', 'had begun'),
                    ('She _____ (just/receive) the test results.', 'has just received'),
                    ('They _____ (treat) this disease many times.', 'have treated'),
                ],
                2: [
                    ('I have studied medicine for 5 years.', 'Present Perfect', ['Present Perfect', 'Past Perfect', 'Future Perfect', 'Present Simple']),
                    ('She had taken the medicine before she felt better.', 'Past Perfect', ['Present Perfect', 'Past Perfect', 'Past Simple', 'Future Perfect']),
                    ('By tomorrow, they will have finished.', 'Future Perfect', ['Future Simple', 'Future Perfect', 'Present Perfect', 'Future Continuous']),
                    ('The hospital has treated thousands of patients.', 'Present Perfect', ['Present Perfect', 'Past Simple', 'Present Simple', 'Past Perfect']),
                    ('He had worked as a surgeon before retiring.', 'Past Perfect', ['Past Simple', 'Past Perfect', 'Present Perfect', 'Past Continuous']),
                    ('Have you ever visited a cardiologist?', 'Present Perfect', ['Present Simple', 'Present Perfect', 'Past Simple', 'Past Perfect']),
                ],
                3: [
                    ('By the end of the day, she _____ (see) 30 patients.', 'will have seen'),
                    ('The doctors _____ (already/leave) when I arrived.', 'had already left'),
                    ('I _____ (not/finish) the report yet.', 'have not finished'),
                    ('By next month, we _____ (complete) the course.', 'will have completed'),
                    ('She _____ (take) her medicine before eating.', 'had taken'),
                ],
                4: [
                    ('She _____ three operations this week.', 'has performed', ['performed', 'has performed', 'had performed', 'will perform']),
                    ('By the time you arrive, I _____ the report.', 'will have finished', ['finish', 'have finished', 'will have finished', 'had finished']),
                    ('He _____ a doctor for 20 years before retiring.', 'had been', ['was', 'has been', 'had been', 'is']),
                    ('I _____ to that hospital before.', 'have never been', ['never went', 'have never been', 'had never been', 'never go']),
                ],
                5: [
                    ('Translate: "I have studied medicine for 3 years. I have learned a lot about the human body."', 'AI_EVALUATED'),
                    ('Translate: "By the time the doctor arrived, the patient had already recovered."', 'AI_EVALUATED'),
                    ('Translate: "By next year, I will have completed my medical degree."', 'AI_EVALUATED'),
                ],
                6: [  # Doctors vocabulary
                    ('tools', 'asboblar'),
                    ('to diagnose', 'tashxis qo\'yish'),
                    ('to treat', 'davolash'),
                    ('medical conditions', 'tibbiy sharoitlar'),
                    ('treatments', 'muolajalar'),
                    ('medical staff', 'tibbiyot xodimlari'),
                    ('nursing homes', 'qariyalar uylari'),
                    ('to recover', 'sog\'ayish'),
                    ('rely on', 'tayanish'),
                    ('patients', 'bemorlar'),
                    ('surgeon', 'jarroh'),
                    ('Hippocratic Oath', 'Gippokrat qasamyodi'),
                    ('fever', 'isitma'),
                    ('cough', 'yo\'tal'),
                ],
                7: [
                    ('hypertension', 'high blood pressure'),
                    ('tachycardia', 'fast heart rate'),
                    ('bradycardia', 'slow heart rate'),
                    ('hypothermia', 'low body temperature'),
                    ('hyperthermia', 'high body temperature'),
                    ('anemia', 'deficiency of red blood cells'),
                    ('arrhythmia', 'irregular heartbeat'),
                    ('hypoxia', 'deficiency of oxygen'),
                ],
                8: [
                    ('Have you ever _____ this symptom before?', 'experienced'),
                    ('The doctor _____ all the tests by now.', 'has completed'),
                    ('I _____ any improvement yet.', 'haven\'t seen'),
                    ('By the time she arrived, they _____ the surgery.', 'had started'),
                    ('She _____ in this hospital since 2015.', 'has worked'),
                ],
                9: [
                    ('Find synonyms for: examined, treated, recovered, completed', 'AI_EVALUATED'),
                    ('Find synonyms for: worked, studied, arrived, finished', 'AI_EVALUATED'),
                ],
                10: [
                    ('Have you ever been hospitalized? What happened?', 'AI_EVALUATED'),
                    ('Have you ever had surgery?', 'AI_EVALUATED'),
                    ('What medical check-ups have you had recently?', 'AI_EVALUATED'),
                    ('Have you ever visited a specialist?', 'AI_EVALUATED'),
                    ('What vaccinations have you received?', 'AI_EVALUATED'),
                ],
                11: [
                    ('Talk about a time when you or a family member was ill. What happened? How was the treatment? What have you learned? Speak for 2 minutes.', 'AI_EVALUATED'),
                ],
                12: [
                    ('Write a role-play dialogue (150-200 words) between a doctor and a patient. Situation: A mother brings her 5-year-old daughter who has a fever. Include: greeting, asking about symptoms, examination, diagnosis, and prescription.', 'AI_EVALUATED'),
                ],
                13: [
                    ('Watch the video about "Doctors and Their Achievements" and retell what medical breakthroughs have been achieved.', 'AI_EVALUATED'),
                ],
            },
        }
        
        # Create questions for units 4-15 with similar structure
        for unit_num in range(4, 16):
            all_questions[unit_num] = self.get_unit_questions(unit_num)
        
        # Now create all questions in database
        for unit_num, tasks in all_questions.items():
            unit = Unit.objects.get(number=unit_num)
            for task_num, questions in tasks.items():
                task = Task.objects.get(unit=unit, number=task_num)
                for i, q in enumerate(questions, 1):
                    if len(q) == 2:  # Simple question
                        TaskQuestion.objects.create(
                            task=task,
                            question_text=q[0],
                            correct_answer=q[1],
                            order=i
                        )
                    elif len(q) == 3:  # With options
                        TaskQuestion.objects.create(
                            task=task,
                            question_text=q[0],
                            correct_answer=q[1],
                            options=q[2],
                            order=i
                        )
            self.stdout.write(self.style.SUCCESS(f'✓ Unit {unit_num} questions'))
    
    def get_unit_questions(self, unit_num):
        """Get questions for units 4-15"""
        questions = {
            4: {  # Perfect Continuous
                1: [
                    ('She _____ (work) as a nurse for 10 years.', 'has been working'),
                    ('They _____ (wait) for 2 hours when he arrived.', 'had been waiting'),
                    ('By next month, I _____ (study) medicine for 3 years.', 'will have been studying'),
                    ('The patient _____ (take) this medication since January.', 'has been taking'),
                    ('He _____ (practice) surgery for 20 years before retiring.', 'had been practicing'),
                ],
                2: [
                    ('She has been working here for 5 years.', 'Present Perfect Continuous', ['Present Continuous', 'Present Perfect Continuous', 'Past Perfect Continuous', 'Future Perfect Continuous']),
                    ('They had been waiting for an hour.', 'Past Perfect Continuous', ['Past Continuous', 'Past Perfect Continuous', 'Present Perfect Continuous', 'Past Perfect']),
                    ('By 2025, I will have been studying for 6 years.', 'Future Perfect Continuous', ['Future Continuous', 'Future Perfect', 'Future Perfect Continuous', 'Present Perfect Continuous']),
                ],
                3: [
                    ('How long _____ (you/study) English?', 'have you been studying'),
                    ('She _____ (work) all day and is very tired.', 'has been working'),
                    ('They _____ (live) here since 2010.', 'have been living'),
                ],
                4: [
                    ('I _____ for three hours.', 'have been studying', ['study', 'have studied', 'have been studying', 'am studying']),
                    ('She _____ all morning.', 'has been working', ['works', 'has worked', 'has been working', 'is working']),
                ],
                5: [
                    ('Translate: "I have been studying medicine for 3 years."', 'AI_EVALUATED'),
                    ('Translate: "She had been working as a nurse before she became a doctor."', 'AI_EVALUATED'),
                ],
                6: [  # Medical University vocabulary
                    ('prominent', 'ko\'zga ko\'ringan'),
                    ('prestigious establishment', 'nufuzli muassasa'),
                    ('medical education', 'tibbiy ta\'lim'),
                    ('medical science', 'tibbiyot fani'),
                    ('extensive clinical and laboratory base', 'keng klinik va laboratoriya bazasi'),
                    ('pediatric faculty', 'pediatriya fakulteti'),
                    ('bio-medical faculty', 'biotibbiyot fakulteti'),
                    ('annual admission', 'yillik qabul'),
                    ('glorious', 'ulug\'vor'),
                    ('deep pedagogical and scientific traditions', 'chuqur pedagogik va ilmiy an\'analar'),
                    ('auxiliary services', 'yordamchi xizmatlar'),
                    ('medical assistance', 'tibbiy yordam'),
                ],
                7: [
                    ('chronic disease', 'a disease that lasts long'),
                    ('acute illness', 'a disease that comes suddenly'),
                    ('terminal illness', 'a disease that cannot be cured'),
                    ('contagious disease', 'a disease that spreads'),
                ],
                8: [
                    ('The patient _____ (suffer) from headaches for weeks.', 'has been suffering'),
                    ('How long _____ (you/feel) this pain?', 'have you been feeling'),
                ],
                9: [('Find synonyms for: working, studying, waiting, suffering', 'AI_EVALUATED')],
                10: [
                    ('How long have you been studying medicine?', 'AI_EVALUATED'),
                    ('What have you been working on lately?', 'AI_EVALUATED'),
                ],
                11: [('Talk about your medical studies. How long have you been studying? What have you been focusing on?', 'AI_EVALUATED')],
                12: [('Write a medical school letter of recommendation (150-200 words). Include: introduction of the student, academic achievements, personal qualities, and why they would make a good doctor.', 'AI_EVALUATED')],
                13: [('Watch the video about chronic diseases and explain treatments.', 'AI_EVALUATED')],
            },
            5: {  # Passive Simple
                1: [
                    ('The patient _____ (examine) by the doctor every week.', 'is examined'),
                    ('The medicine _____ (prescribe) yesterday.', 'was prescribed'),
                    ('The operation _____ (perform) next Monday.', 'will be performed'),
                    ('Many diseases _____ (cure) with antibiotics.', 'are cured'),
                    ('The diagnosis _____ (confirm) by the specialist.', 'was confirmed'),
                ],
                2: [
                    ('The patient is examined by the doctor.', 'Present Simple Passive', ['Present Simple Active', 'Present Simple Passive', 'Past Simple Passive', 'Future Simple Passive']),
                    ('The surgery was performed yesterday.', 'Past Simple Passive', ['Present Simple Passive', 'Past Simple Passive', 'Past Simple Active', 'Future Simple Passive']),
                ],
                3: [
                    ('Change to passive: The doctor examines the patient.', 'The patient is examined by the doctor'),
                    ('Change to passive: The nurse gave the injection.', 'The injection was given by the nurse'),
                ],
                4: [
                    ('The operation _____ by Dr. Smith.', 'was performed', ['performed', 'was performed', 'is performing', 'performs']),
                    ('English _____ in many countries.', 'is spoken', ['speaks', 'spoke', 'is spoken', 'is speaking']),
                ],
                5: [
                    ('Translate: "The patient is examined by the doctor every day."', 'AI_EVALUATED'),
                    ('Translate: "The medicine was prescribed by the physician."', 'AI_EVALUATED'),
                ],
                6: [  # Tashkent Medical Academy vocabulary
                    ('a renowned institution', 'taniqli muassasa'),
                    ('highly skilled healthcare professionals', 'yuqori malakali sog\'liqni saqlash mutaxassislari'),
                    ('to contribute', 'hissa qo\'shish'),
                    ('inception', 'boshlanishi'),
                    ('significant progress', 'sezilarli taraqqiyot'),
                    ('various disciplines', 'turli fanlar'),
                    ('to enroll', 'ro\'yxatdan o\'tish'),
                    ('clinical experience', 'klinik tajriba'),
                    ('international standards', 'xalqaro standartlar'),
                    ('human health', 'inson salomatligi'),
                    ('academic goals', 'akademik maqsadlar'),
                    ('extracurricular activities', 'darsdan tashqari mashg\'ulotlar'),
                ],
                7: [
                    ('ambulance', 'a vehicle for transporting sick people'),
                    ('stretcher', 'a frame for carrying patients'),
                    ('wheelchair', 'a chair with wheels'),
                ],
                8: [
                    ('The hospital _____ (build) in 1990.', 'was built'),
                    ('The new wing _____ (open) next year.', 'will be opened'),
                ],
                9: [('Find passive forms for: examine, treat, prescribe, diagnose', 'AI_EVALUATED')],
                10: [
                    ('How are patients treated in your country?', 'AI_EVALUATED'),
                    ('What procedures are commonly performed?', 'AI_EVALUATED'),
                ],
                11: [('Describe a medical procedure using passive voice.', 'AI_EVALUATED')],
                12: [('Write an essay (150-200 words) about "Why I chose medical school". Include your motivation, what inspired you, challenges you expect, and your goals.', 'AI_EVALUATED')],
                13: [('Watch the video and describe using passive voice.', 'AI_EVALUATED')],
            },
            6: {  # Passive Continuous
                1: [
                    ('The patient _____ (examine) right now.', 'is being examined'),
                    ('The surgery _____ (perform) when I arrived.', 'was being performed'),
                    ('New treatments _____ (develop) by researchers.', 'are being developed'),
                    ('The medicine _____ (test) when the error was found.', 'was being tested'),
                ],
                2: [
                    ('The patient is being examined now.', 'Present Continuous Passive', ['Present Simple Passive', 'Present Continuous Passive', 'Past Continuous Passive', 'Future Continuous Passive']),
                    ('The surgery was being performed.', 'Past Continuous Passive', ['Present Continuous Passive', 'Past Continuous Passive', 'Past Simple Passive', 'Present Perfect Passive']),
                ],
                3: [
                    ('Change to passive: They are treating the patient.', 'The patient is being treated'),
                    ('Change to passive: The doctors were discussing the case.', 'The case was being discussed'),
                ],
                4: [('The new hospital _____ now.', 'is being built', ['builds', 'is built', 'is being built', 'was built'])],
                5: [('Translate: "The patient is being examined by the doctor now."', 'AI_EVALUATED')],
                6: [  # Medical education in Uzbekistan vocabulary
                    ('medical personnel', 'tibbiyot xodimlari'),
                    ('pharmacist', 'farmatsevt'),
                    ('curriculum', 'o\'quv reja'),
                    ('syllabuses', 'o\'quv dasturlari'),
                    ('to be approved', 'tasdiqlanishi kerak'),
                    ('administrative affairs', 'ma\'muriy ishlar'),
                    ('pre-clinical training', 'klinikadan oldingi tayyorgarlik'),
                    ('general subjects', 'umumiy fanlar'),
                    ('clinical subjects', 'klinik mavzular'),
                    ('surgery', 'jarrohlik'),
                    ('obstetrics', 'akusherlik'),
                    ('to acquire', 'egallash'),
                    ('to work as interns', 'stajyor sifatida ishlash'),
                ],
                7: [
                    ('ICU', 'Intensive Care Unit'),
                    ('ER', 'Emergency Room'),
                    ('OR', 'Operating Room'),
                ],
                8: [('While the patient _____ (operate on), complications arose.', 'was being operated on')],
                9: [('Find passive continuous forms for: treat, examine, operate', 'AI_EVALUATED')],
                10: [('What research is being conducted in medicine today?', 'AI_EVALUATED')],
                11: [('Describe a procedure you observed using passive continuous.', 'AI_EVALUATED')],
                12: [('Write a Medical School Letter of Intent (150-200 words). Include: why you want to attend this specific school, what you can contribute, your career goals, and why you are a good fit.', 'AI_EVALUATED')],
                13: [('Watch the video and describe what was being shown.', 'AI_EVALUATED')],
            },
            7: {  # Passive Perfect
                1: [
                    ('The patient _____ (treat) successfully.', 'has been treated'),
                    ('The surgery _____ (complete) before they arrived.', 'had been completed'),
                    ('By next week, all patients _____ (vaccinate).', 'will have been vaccinated'),
                ],
                2: [('The patient has been treated.', 'Present Perfect Passive', ['Present Perfect Active', 'Present Perfect Passive', 'Past Perfect Passive', 'Future Perfect Passive'])],
                3: [('Change to passive: They have examined the patient.', 'The patient has been examined')],
                4: [('The medicine _____ already.', 'has been given', ['gave', 'has given', 'has been given', 'is given'])],
                5: [('Translate: "The patient has been treated successfully."', 'AI_EVALUATED')],
                6: [  # Medical education in USA vocabulary
                    ('basic subjects', 'asosiy fanlar'),
                    ('deep knowledge', 'chuqur bilim'),
                    ('to make top grades', 'yuqori darajalarni olish'),
                    ('pathologic physiology', 'patologik fiziologiya'),
                    ('to deal with patients', 'bemorlar bilan muomala qilish'),
                    ('to come in touch', 'aloqaga kirishish'),
                    ('anesthesiology', 'anesteziologiya'),
                    ('dermatology', 'dermatologiya'),
                    ('internal medicine', 'ichki kasalliklar tibbiyoti'),
                    ('preventive medicine', 'profilaktik tibbiyot'),
                    ('field of medicine', 'tibbiyot sohasi'),
                    ('to pay additional fees', 'qo\'shimcha to\'lovlarni to\'lash'),
                ],
                7: [
                    ('vaccination', 'giving a vaccine'),
                    ('immunization', 'making immune'),
                ],
                8: [('By the time we arrived, the operation _____ (finish).', 'had been finished')],
                9: [('Find passive perfect forms for: treat, examine, complete', 'AI_EVALUATED')],
                10: [('What medical advances have been made recently?', 'AI_EVALUATED')],
                11: [('Talk about what has been achieved in medicine.', 'AI_EVALUATED')],
                12: [('Write an essay (150-200 words) about "Medical Education in the USA". Include: structure of medical education, duration, requirements, and differences from your country.', 'AI_EVALUATED')],
                13: [('Watch the video about achievements and describe what has been accomplished.', 'AI_EVALUATED')],
            },
            8: {  # Sequence of Tenses
                1: [
                    ('He said that he _____ (be) a doctor.', 'was'),
                    ('She told me that she _____ (work) at the hospital.', 'worked'),
                    ('The doctor said the patient _____ (recover) soon.', 'would recover'),
                    ('They explained they _____ (perform) the surgery.', 'had performed'),
                ],
                2: [('He said, "I am a doctor." - He said he _____ a doctor.', 'was', ['is', 'was', 'will be', 'had been'])],
                3: [
                    ('"I work here." → She said she _____ there.', 'worked'),
                    ('"I will call you." → He said he _____ me.', 'would call'),
                ],
                4: [('She said she _____ the doctor the day before.', 'had seen', ['saw', 'has seen', 'had seen', 'sees'])],
                5: [('Translate the reported speech: "He said he was a doctor."', 'AI_EVALUATED')],
                6: [  # Medical education in UK vocabulary
                    ('the average pay', 'o\'rtacha ish haqi'),
                    ('governing body of the medical profession', 'tibbiyot kasbining boshqaruv organi'),
                    ('premedical training', 'tibbiygacha tayyorgarlik'),
                    ('human morphology', 'inson morfologiyasi'),
                    ('medical procedures', 'tibbiy muolajalar'),
                    ('to be well prepared', 'yaxshi tayyorgarlik ko\'rish'),
                    ('free medical care', 'bepul tibbiy yordam'),
                    ('private doctors', 'xususiy shifokorlar'),
                    ('alternative medicine', 'muqobil tibbiyot'),
                    ('homeopathy', 'gomeopatiya'),
                    ('acupuncture', 'nina bilan davolash'),
                    ('life expectancy', 'umr ko\'rish davomiyligi'),
                    ('heart disease', 'yurak kasalligi'),
                ],
                7: [
                    ('reporting verb', 'a verb to introduce reported speech'),
                    ('time marker', 'a word indicating when'),
                ],
                8: [
                    ('She said she _____ (be) tired.', 'was'),
                    ('He told me he _____ (go) to the hospital.', 'had gone'),
                ],
                9: [('Find the correct sequence of tenses for given sentences', 'AI_EVALUATED')],
                10: [('What did your doctor tell you at your last visit?', 'AI_EVALUATED')],
                11: [('Retell a conversation with a doctor using reported speech.', 'AI_EVALUATED')],
                12: [('Write a Letter of Interest about medical education (150-200 words). Include: your interest in the program, relevant experience, what you hope to learn, and how it fits your career goals.', 'AI_EVALUATED')],
                13: [('Watch the video and report what was said.', 'AI_EVALUATED')],
            },
            9: {  # Direct and Reported Speech
                1: [
                    ('"I am a doctor." → He said he _____ a doctor.', 'was'),
                    ('"I work here." → She said she _____ there.', 'worked'),
                    ('"I will call you." → He said he _____ me.', 'would call'),
                    ('"I have finished." → She said she _____.', 'had finished'),
                ],
                2: [('"I am studying."', 'She said she was studying.', ['She said she is studying.', 'She said she was studying.', 'She said she had studied.', 'She said she studies.'])],
                3: [
                    ('"I can help." → He said he _____ help.', 'could'),
                    ('"I must take medicine." → He said he _____ take medicine.', 'had to'),
                ],
                4: [('She said, "I _____ the exam."', 'had passed', ['pass', 'passed', 'had passed', 'have passed'])],
                5: [('Translate: "She said she was a nurse."', 'AI_EVALUATED')],
                6: [  # World Health Organization vocabulary
                    ('World Health Organization', 'Jahon Sog\'liqni saqlash tashkiloti'),
                    ('to ratify', 'ratifikatsiya qilish'),
                    ('the attainment', 'erishish'),
                    ('mental', 'ruhiy, aqliy'),
                    ('social well-being', 'ijtimoiy farovonlik'),
                    ('to eradicate', 'yo\'q qilish'),
                    ('sanitation', 'sanitariya'),
                    ('epidemic warnings', 'epidemiya haqida ogohlantirishlar'),
                    ('plague', 'vabo'),
                    ('cholera', 'vabo'),
                    ('smallpox', 'chechak'),
                    ('vaccines', 'vaksinalar'),
                    ('morbidity', 'kasallanish'),
                ],
                7: [
                    ('announce', 'make known publicly'),
                    ('declare', 'state officially'),
                    ('explain', 'make clear'),
                ],
                8: [('He said, "I am sick." → He said he _____ sick.', 'was')],
                9: [('Transform direct speech to reported speech', 'AI_EVALUATED')],
                10: [('What advice did your parents give about health?', 'AI_EVALUATED')],
                11: [('Report a conversation about health.', 'AI_EVALUATED')],
                12: [('Write a Cover Letter for World Health Organization (WHO) (150-200 words). Include: why you want to work at WHO, your relevant skills and experience, what you can contribute, and your passion for global health.', 'AI_EVALUATED')],
                13: [('Watch the video and report the main points.', 'AI_EVALUATED')],
            },
            10: {  # Interrogative and Imperative - History of Medicine
                1: [  # Change to Indirect Speech (10 questions from textbook)
                    ('"Are there any more files?" He asked. "Yes, sir," said the peon. → He asked...', 'if there were any more files. The peon replied that there were.'),
                    ('The teacher said to Rano, "Did you break the window pane?" "No," said Rano. → The teacher asked...', 'Rano if she had broken the window pane. Rano said she had not.'),
                    ('"If you find my answers satisfactory, will you give me five rupees?" said the astrologer. → The astrologer asked...', 'if he would give him five rupees if he found his answers satisfactory.'),
                    ('I said to him, "Do you want to go to Khiva?" He said, "No, Karim." → I asked him...', 'if he wanted to go to Khiva. He said no.'),
                    ('Rashid said to me, "Does Mohina still play?" I said, "Yes, sir." → Rashid asked me...', 'if Mohina still played. I said yes.'),
                    ('Malik said to her, "Has Salomat invited you to dinner?" → Malik asked her...', 'if Salomat had invited her to dinner.'),
                    ('I said to her, "Did you enjoy the film?" She said, "No." → I asked her...', 'if she had enjoyed the film. She said no.'),
                    ('Sabrina said, "Sitora, do you see what I see?" Sitora said, "Yes." → Sabrina asked Sitora...', 'if she saw what she saw. Sitora said yes.'),
                    ('He said, "Do you not like it?" She said, "Yes." → He asked...', 'if she did not like it. She said yes.'),
                    ('She said to me, "Shall we ever see each other again?" I said, "Perhaps, never." → She asked me...', 'if they would ever see each other again. I said perhaps never.'),
                ],
                2: [  # Change to Indirect Speech - Medical questions (8 questions from textbook)
                    ('"What is your name?" asked the doctor. → Indirect speech:', 'The doctor asked what my name was.'),
                    ('"What kind of medicine did you take yesterday?" cardiologist asked me. → Indirect speech:', 'The cardiologist asked me what kind of medicine I had taken the day before.'),
                    ('"Are you feeling better now?" he asked her. → Indirect speech:', 'He asked her if she was feeling better then.'),
                    ('"Why didn\'t you take all the treatments yesterday?" he asked her. → Indirect speech:', 'He asked her why she hadn\'t taken all the treatments the day before.'),
                    ('"You need to take more vitamins?" he asked his son. → Indirect speech:', 'He asked his son if he needed to take more vitamins.'),
                    ('"What are you doing here?" asked the receptionist. → Indirect speech:', 'The receptionist asked what I was doing there.'),
                    ('"Have you seen the doctor?" she asked me. → Indirect speech:', 'She asked me if I had seen the doctor.'),
                    ('"Where did you put my medicine?" asked my mother. → Indirect speech:', 'My mother asked where I had put her medicine.'),
                ],
                3: [  # Change direct speech into reported speech - Requests/Commands (15 questions from textbook)
                    ('"Please help me carry this" She asked me...', 'to help her carry that.'),
                    ('"Please come early" She...', 'asked me to come early.'),
                    ('"Please buy some milk" She...', 'asked me to buy some milk.'),
                    ('"Could you please open the window?" She...', 'asked me to open the window.'),
                    ('"Could you bring the book tonight?" She...', 'asked me to bring the book that night.'),
                    ('"Can you help me with my homework, please?" She...', 'asked me to help her with her homework.'),
                    ('"Would you bring me a cup of coffee, please?" She...', 'asked me to bring her a cup of coffee.'),
                    ('"Would you mind passing the salt?" She...', 'asked me to pass the salt.'),
                    ('"Would you mind lending me a pencil?" She...', 'asked me to lend her a pencil.'),
                    ('"I was wondering if you could possibly tell me the time?" She...', 'asked me to tell her the time.'),
                    ('"Do your homework!" She told me...', 'to do my homework.'),
                    ('"Go to bed!" She...', 'told me to go to bed.'),
                    ('"Don\'t be late!" She...', 'told me not to be late.'),
                    ('"Don\'t smoke!" She...', 'told me not to smoke.'),
                    ('"Tidy your room!" She...', 'told me to tidy my room.'),
                ],
                4: [  # Choose the best answer (from textbook Task 4)
                    ('The teacher promised ___.', 'we would learn three English songs', ['that we can learn three English songs', 'if we learn three English songs', 'we would learn three English songs', 'whether we would learn three English songs']),
                    ('Botir asked Nafisa ___ (Have you seen any interesting comedy lately?)', 'if she had seen any interesting comedy lately', ['if he will see an interesting film', 'if he saw an interesting comedy lately', 'what comedy Noila saw lately', 'if she had seen any interesting comedy lately']),
                    ('Nodir wonders ___ in the tree. (Did you see a bird?)', 'if I had seen a bird', ['if I saw a bird', 'that I saw a bird', 'if I had seen a bird', 'whether I see a bird']),
                    ('Sunnat asked if ___ (Have you received my telegram?)', 'Nilufar had received his telegram', ['Nilufar had received his telegram', 'Nilufar has received his telegram', 'Nilufar would receive his telegram', 'Nilufar will receive his telegram']),
                    ('Aziza asked me ___ (Write down my address)', 'to write down her address', ['he wrote down my address', 'to write down her address', 'he had written her address', 'she writes down her address']),
                    ('He said, "I\'m very busy today." He said ___.', 'he was very busy that day', ['he had been very busy that day', 'he is very busy today', 'he was very busy that day', 'I\'m very busy today']),
                    ('Laylo said, "Where have you been yesterday?" Laylo asked ___.', 'where she had been the day before', ['where she had been the day before', 'where she had been yesterday', 'where she was the day before', 'where she could be the day before']),
                    ('He thought: "What am I going to do?" He thought ___.', 'what he was going to do', ['what was he going to do', 'what he was going to do', 'what he is going to do', 'if he was going to do']),
                    ('Mother asked me ___ (about spending money)', 'if I had spent all the money', ['why I have spent all the money', 'that I had spent all the money', 'if I had spent all the money', 'when I spend all the money']),
                    ('"Don\'t play in the street!" My mother told me ___.', 'not to play in the street', ['don\'t play in the street', 'to play in the street', 'she should play in the street', 'not to play in the street']),
                    ('Amir asked Guli ___ (Don\'t forget to bring my book)', 'not to forget to bring his book', ['that she didn\'t forget to bring his book', 'that she doesn\'t bring his book', 'not to forget to bring his book', 'not to forget to bring her book']),
                ],
                5: [('Translate the reported question and command', 'AI_EVALUATED')],
                6: [  # History of medicine vocabulary
                    ('prehistoric skulls', 'tarixdan oldingi kalla suyaklari'),
                    ('to trephine', 'trefin qilish'),
                    ('surgical procedure', 'jarrohlik muolajasi'),
                    ('empirical medicine', 'empirik tibbiyot'),
                    ('embalming', 'balzamlash'),
                    ('dietary restrictions', 'ovqatlanish cheklovlari'),
                    ('sanitary measures', 'sanitariya choralari'),
                    ('vital function', 'hayotiy funktsiya'),
                    ('vascular systems', 'qon tomir tizimlari'),
                    ('a regimen of diet', 'ovqatlanish rejimi'),
                    ('dissections of animals', 'hayvonlarni kesib o\'rganish'),
                    ('the valves of the veins', 'tomirlarning klapanlari'),
                ],
                7: [
                    ('interrogative', 'relating to questions'),
                    ('imperative', 'relating to commands'),
                ],
                8: [('"Where is the hospital?" → He asked where the hospital _____.', 'was')],
                9: [('Transform questions to reported speech', 'AI_EVALUATED')],
                10: [('What questions do doctors usually ask patients?', 'AI_EVALUATED')],
                11: [('Practice asking and answering medical questions.', 'AI_EVALUATED')],
                12: [('Write a Medical Discharge Letter (150-200 words). Include: patient information, diagnosis, treatment received, medications prescribed, follow-up instructions, and doctor signature.', 'AI_EVALUATED')],
                13: [('Watch the video and report questions and instructions.', 'AI_EVALUATED')],
            },
            11: {  # Subjunctive Mood
                1: [
                    ('I wish I _____ (be) a doctor.', 'were'),
                    ('If I _____ (have) more time, I would study more.', 'had'),
                    ('The doctor suggested he _____ (take) rest.', 'take'),
                    ('I wish she _____ (can) recover faster.', 'could'),
                ],
                2: [('I wish I were a doctor.', 'Subjunctive', ['Indicative', 'Subjunctive', 'Imperative', 'Conditional'])],
                3: [
                    ('If he _____ (be) here, he would help.', 'were'),
                    ('It is essential that the patient _____ (follow) treatment.', 'follow'),
                ],
                4: [('I wish I _____ more about medicine.', 'knew', ['know', 'knew', 'known', 'knowing'])],
                5: [('Translate: "I wish I were a doctor."', 'AI_EVALUATED')],
                6: [  # Modern Medicine vocabulary
                    ('the circulation of the blood', 'qon aylanishi'),
                    ('resistance', 'qarshilik'),
                    ('quinine', 'xinin'),
                    ('a triumph over malaria', 'bezgak ustidan g\'alaba'),
                    ('capillary system of the blood', 'qonning kapillyar tizimi'),
                    ('scurvy', 'iskorbit'),
                    ('science of immunization', 'immunizatsiya fani'),
                    ('germs', 'mikroblar'),
                    ('inoculation', 'emlash'),
                    ('chemotherapy', 'kimyoterapiya'),
                    ('hormone imbalance', 'gormonlar muvozanati'),
                    ('organ transplantation', 'organ transplantatsiyasi'),
                ],
                7: [
                    ('hypothetical', 'based on assumption'),
                    ('conditional', 'depending on circumstances'),
                ],
                8: [('I would go to hospital if I _____ (feel) worse.', 'felt')],
                9: [('Identify subjunctive mood in sentences', 'AI_EVALUATED')],
                10: [('What do you wish you knew more about in medicine?', 'AI_EVALUATED')],
                11: [('Talk about what you would do if you were a famous doctor.', 'AI_EVALUATED')],
                12: [('Write an academic essay (150-200 words) about "Modern Medicine: Advantages and Challenges". Include: introduction, main body with examples, and conclusion.', 'AI_EVALUATED')],
                13: [('Watch the video and discuss what should be improved.', 'AI_EVALUATED')],
            },
            12: {  # Indicative and Imperative
                1: [
                    ('_____ (take) your medicine twice a day.', 'Take'),
                    ('_____ (not/forget) your appointment.', 'Don\'t forget'),
                    ('_____ (rest) well before surgery.', 'Rest'),
                    ('_____ (drink) plenty of water.', 'Drink'),
                ],
                2: [
                    ('Take your medicine!', 'Imperative', ['Indicative', 'Subjunctive', 'Imperative', 'Conditional']),
                    ('She takes medicine every day.', 'Indicative', ['Indicative', 'Subjunctive', 'Imperative', 'Conditional']),
                ],
                3: [
                    ('_____ (call) the doctor if symptoms persist.', 'Call'),
                    ('_____ (not/skip) doses.', 'Don\'t skip'),
                ],
                4: [('_____ quiet in the hospital.', 'Be', ['Is', 'Be', 'Being', 'Been'])],
                5: [('Translate the commands: "Take medicine. Don\'t smoke."', 'AI_EVALUATED')],
                6: [  # Healthcare in Uzbekistan vocabulary
                    ('quality of healthcare', 'sog\'liqni saqlash sifati'),
                    ('upward trend', 'ko\'tarilish tendentsiyasi'),
                    ('global rankings', 'global reytinglar'),
                    ('public healthcare providers', 'davlat sog\'liqni saqlash provayderlari'),
                    ('unsafe practices', 'xavfli amaliyotlar'),
                    ('health expenditure', 'sog\'liqni saqlash xarajatlari'),
                    ('healthcare availability', 'sog\'liqni saqlash mavjudligi'),
                    ('healthcare access', 'sog\'liqni saqlashga kirish'),
                    ('maternal and infant mortality', 'onalar va chaqaloqlar o\'limi'),
                    ('life expectancy', 'umr ko\'rish davomiyligi'),
                    ('to implement reforms', 'islohotlarni amalga oshirish'),
                    ('beneficial', 'foydali'),
                ],
                7: [
                    ('indicative mood', 'states facts'),
                    ('imperative mood', 'gives commands'),
                ],
                8: [('_____ (follow) the prescribed diet.', 'Follow')],
                9: [('Identify mood in given sentences', 'AI_EVALUATED')],
                10: [('What instructions do doctors give patients?', 'AI_EVALUATED')],
                11: [('Give instructions on maintaining good health.', 'AI_EVALUATED')],
                12: [('Write an essay (150-200 words) about "Healthcare System in Uzbekistan: 7 Key Facts". Include: achievements, challenges, reforms, and your opinion on improvements needed.', 'AI_EVALUATED')],
                13: [('Watch the video and list the health instructions.', 'AI_EVALUATED')],
            },
            13: {  # Gerund
                1: [
                    ('_____ (smoke) is harmful to health.', 'Smoking'),
                    ('She enjoys _____ (help) patients.', 'helping'),
                    ('He is good at _____ (diagnose) diseases.', 'diagnosing'),
                    ('The doctor recommended _____ (exercise) regularly.', 'exercising'),
                ],
                2: [
                    ('Smoking is harmful.', 'Subject', ['Subject', 'Object', 'Complement', 'Modifier']),
                    ('I enjoy swimming.', 'Object', ['Subject', 'Object', 'Complement', 'Modifier']),
                ],
                3: [
                    ('She avoided _____ (eat) unhealthy food.', 'eating'),
                    ('He finished _____ (examine) the patient.', 'examining'),
                ],
                4: [('_____ is good for health.', 'Walking', ['Walk', 'Walking', 'To walk', 'Walked'])],
                5: [('Translate: "Smoking is bad for health."', 'AI_EVALUATED')],
                6: [  # Scientists vocabulary
                    ('smallpox vaccine', 'chechakka qarshi emlash'),
                    ('the polio vaccine', 'poliomielitga qarshi emlash'),
                    ('a fatal ailment', 'halokatli kasallik'),
                    ('an antidote for smallpox', 'chechak uchun antidot'),
                    ('lethal', 'halokatli'),
                    ('dreaded disease', 'qo\'rqinchli kasallik'),
                    ('the vaccination mandatory', 'majburiy emlash'),
                    ('mass inoculations', 'ommaviy emlashlar'),
                    ('anopheles species of mosquitoes', 'chivinlarning anofeles turlari'),
                    ('stagnant water', 'turg\'un suv'),
                    ('enzyme lysosome', 'lizosoma fermenti'),
                    ('strep throat', 'tomoq kasalligi'),
                ],
                7: [('gerund', 'a verb form ending in -ing used as a noun')],
                8: [('They discussed _____ (perform) the surgery.', 'performing')],
                9: [('Find gerunds in the given text', 'AI_EVALUATED')],
                10: [('What do you enjoy doing to stay healthy?', 'AI_EVALUATED')],
                11: [('Talk about healthy activities using gerunds.', 'AI_EVALUATED')],
                12: [('Write an essay (150-200 words) about "5 Scientists Who Saved Millions of Lives with Their Inventions". Choose one scientist (e.g., Pasteur, Jenner, Fleming) and describe their contribution to medicine.', 'AI_EVALUATED')],
                13: [('Watch the video and describe activities using gerunds.', 'AI_EVALUATED')],
            },
            14: {  # Infinitive
                1: [
                    ('She wants _____ (become) a surgeon.', 'to become'),
                    ('He decided _____ (study) medicine.', 'to study'),
                    ('The doctor asked me _____ (wait).', 'to wait'),
                    ('It is important _____ (take) medicine on time.', 'to take'),
                ],
                2: [('She wants to become a doctor.', 'Full infinitive', ['Bare infinitive', 'Full infinitive', 'Gerund', 'Participle'])],
                3: [
                    ('She learned _____ (perform) surgery.', 'to perform'),
                    ('He hopes _____ (recover) soon.', 'to recover'),
                ],
                4: [('I need _____ the doctor.', 'to see', ['see', 'to see', 'seeing', 'saw'])],
                5: [('Translate: "I want to become a doctor."', 'AI_EVALUATED')],
                6: [  # Hippocrates vocabulary
                    ('superstition', 'xurofot'),
                    ('the punishment of Gods', 'xudolarning jazosi'),
                    ('a natural cause', 'tabiiy sabab'),
                    ('chest', 'ko\'krak qafasi'),
                    ('accurate prognosis', 'aniq prognoz'),
                    ('the nature of respiration', 'nafas olishning tabiati'),
                    ('appearance of sputum', 'balg\'amning ko\'rinishi'),
                    ('affection of the whole organism', 'butun tanaga zarar yetkazish'),
                ],
                7: [('infinitive', 'the base form of a verb with "to"')],
                8: [('The nurse promised _____ (call) me.', 'to call')],
                9: [('Find infinitives in the given text', 'AI_EVALUATED')],
                10: [('What do you want to achieve in medicine?', 'AI_EVALUATED')],
                11: [('Talk about your goals using infinitives.', 'AI_EVALUATED')],
                12: [('Write a Medical Scientist Cover Letter (150-200 words). Include: your interest in the position, relevant qualifications, research experience, and why you would be a good fit for the role.', 'AI_EVALUATED')],
                13: [('Watch the video and describe what doctors planned to do.', 'AI_EVALUATED')],
            },
            15: {  # Participle
                1: [
                    ('The _____ (operate) surgeon is skilled.', 'operating'),
                    ('The _____ (break) bone needs surgery.', 'broken'),
                    ('Having _____ (examine) the patient, the doctor prescribed medicine.', 'examined'),
                    ('The _____ (recover) patient was discharged.', 'recovering'),
                ],
                2: [
                    ('The broken bone was treated.', 'Past participle', ['Present participle', 'Past participle', 'Perfect participle', 'Gerund']),
                    ('The operating surgeon is skilled.', 'Present participle', ['Present participle', 'Past participle', 'Perfect participle', 'Gerund']),
                ],
                3: [
                    ('The medicine _____ (prescribe) by the doctor helped.', 'prescribed'),
                    ('The _____ (tire) nurse finished her shift.', 'tired'),
                ],
                4: [('The _____ patient was taken to ER.', 'injured', ['injure', 'injuring', 'injured', 'injury'])],
                5: [('Translate: "The broken bone was treated."', 'AI_EVALUATED')],
                6: [  # Avicenna vocabulary
                    ('sum up', 'xulosa qilish'),
                    ('display', 'ko\'rsatish'),
                    ('uncommon ability', 'g\'ayrioddiy qobiliyat'),
                    ('merchants', 'savdogarlar'),
                    ('world renown', 'dunyoga mashhur'),
                    ('comprehensive work', 'keng qamrovli ish'),
                    ('remedy', 'chora'),
                    ('admixtures', 'aralashmalar'),
                    ('the inception of bacteriology', 'bakteriologiyaning paydo bo\'lishi'),
                    ('valid', 'yaroqli'),
                    ('gastric diseases', 'oshqozon kasalliklari'),
                    ('a correct regimen', 'to\'g\'ri rejim'),
                ],
                7: [
                    ('present participle', 'verb form ending in -ing'),
                    ('past participle', 'verb form often ending in -ed'),
                ],
                8: [('Being _____ (train) well, she handled the emergency.', 'trained')],
                9: [('Find participles in the given text', 'AI_EVALUATED')],
                10: [('Describe a medical situation using participles.', 'AI_EVALUATED')],
                11: [('Talk about procedures using participles.', 'AI_EVALUATED')],
                12: [('Write an article (100-150 words) about Abu Ali Ibn Sina (Avicenna). Include: when and where he was born, his major contributions to medicine, his famous works (e.g., The Canon of Medicine), and his legacy.', 'AI_EVALUATED')],
                13: [('Watch the video and describe using participles.', 'AI_EVALUATED')],
            },
        }
        return questions.get(unit_num, {})
