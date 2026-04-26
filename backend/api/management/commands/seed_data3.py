"""
Unit 3: Doctors - Perfect Tenses in the Active Voice
"""

UNIT_3_DATA = {
    'unit': {
        'number': 3,
        'title': 'Doctors',
        'description': 'Perfect Tenses in the Active Voice'
    },
    'tasks': {
        # Task 1: Fill in the correct form of Present Perfect (14 questions from textbook)
        1: [
            ('(to be) I have _____ sick for a month.', 'been'),
            ('(to eat) Ella has _____ eggs for breakfast since she was 10.', 'eaten'),
            ('(to feel) Juan has _____ nauseous since 8:30am.', 'felt'),
            ('(to have) We _____ _____ the flu for one day.', 'have had'),
            ('(to do) They have _____ their homework together every night this week.', 'done'),
            ('(to have) They _____ _____ cancer for two years.', 'have had'),
            ('(to have) She _____ _____ an earache since last night.', 'has had'),
            ('(to feel) Farah and Abdul _____ _____ sick since Tuesday.', 'have felt'),
            ('(to be) John _____ _____ vomiting for two hours.', 'has been'),
            ('(to live) We _____ _____ in Indonesia since 2009.', 'have lived'),
            ('(to have) He _____ _____ a brain tumor since 2010.', 'has had'),
            ('(to have) You and I _____ _____ a cold for three days.', 'have had'),
            ('(to feel) I _____ _____ dizzy since I got pregnant.', 'have felt'),
            ('(to cook) Peter _____ _____ dinner for his wife since she got pregnant.', 'has cooked'),
        ],
        
        # Task 2: Past Perfect - Reading comprehension and exercises (7 questions from textbook)
        2: [
            ('How long had I saved money before I booked my trip to Paris in 2012?', '5 years'),
            ('How many years had I studied French before I visited Paris?', '2 years'),
            ('What are some places I had toured before I left Paris?', 'The Eiffel Tower, Notre Dame Cathedral, Luxembourg Gardens'),
            ('Before I visited Paris, where had I seen those places?', 'on television'),
            ('Rewrite as negative: I had never seen such beautiful sights before I visited Paris.', 'I had seen such beautiful sights before I visited Paris.'),
            ('Rewrite as Yes/No Question: I had studied French for 2 years before I visited Paris.', 'Had I studied French for 2 years before I visited Paris?'),
            ('Rewrite as WH-Question: By the time I left Paris, I had toured many beautiful places.', 'What had I toured by the time I left Paris?'),
        ],
        
        # Task 3: Future Perfect - What will Aziza have done by wedding (10 questions from textbook)
        3: [
            ('(+) send wedding invitations - Will she have done this by her wedding?', 'Yes, she will have sent wedding invitations.'),
            ('(+) order a photographer - Will she have done this?', 'Yes, she will have ordered a photographer.'),
            ('(+) try on her wedding dress - Will she have done this?', 'Yes, she will have tried on her wedding dress.'),
            ('(+) find a place for the wedding reception - Will she have done this?', 'Yes, she will have found a place for the wedding reception.'),
            ('(+) book hotel rooms for wedding guests - Will she have done this?', 'Yes, she will have booked hotel rooms for wedding guests.'),
            ('(-) regret her decision - Will she have done this?', 'No, she will not have regretted her decision.'),
            ('(-) receive wedding gifts - Will she have done this?', 'No, she will not have received wedding gifts.'),
            ('(-) change her surname - Will she have done this?', 'No, she will not have changed her surname.'),
            ('(-) leave for her honeymoon - Will she have done this?', 'No, she will not have left for her honeymoon.'),
            ('(-) move to a new place - Will she have done this?', 'No, she will not have moved to a new place.'),
        ],
        
        # Task 4: Choose the best answer - Tense identification (10 questions from textbook)
        4: [
            ('Does Mansur go to hospital every day?', 'Present Simple', ['Present Perfect', 'Past Simple', 'Present Continuous', 'Present Simple']),
            ('An apple a day keeps a doctor away.', 'Present Simple', ['Present Simple', 'Present Perfect', 'Past Simple', 'Present Continuous']),
            ('Jasur hadn\'t studied chemistry before.', 'Past Perfect', ['Present Perfect', 'Past Continuous', 'Past Simple', 'Past Perfect']),
            ('I need the blood pressure tonometer. Will you please bring it over here?', 'Future', ['Present Perfect', 'Past Perfect', 'Future', 'Present Continuous']),
            ('I don\'t go to the dentist often enough.', 'Present Simple', ['Present Perfect', 'Present Simple', 'Past Simple', 'Present Continuous']),
            ('Had you lost your mind?', 'Past Perfect', ['Past Perfect', 'Present Perfect', 'Past Continuous', 'Past Simple']),
            ('I worked in the same hospital for fifteen years.', 'Past Simple', ['Past Perfect', 'Past Simple', 'Present Simple', 'Past Continuous']),
            ('We are going to do medical practice at my uncle\'s clinic.', 'Future', ['Present Perfect', 'Future', 'Past Perfect', 'Present Continuous']),
            ('He is not listening to the lecture right now.', 'Present Continuous', ['Present Continuous', 'Past Continuous', 'Present Simple', 'Present Perfect']),
            ('He hadn\'t taken the exam on biology last year.', 'Past Perfect', ['Present Perfect', 'Past Continuous', 'Past Simple', 'Past Perfect']),
        ],
        
        # Task 5: Read and translate - DOCTORS text (AI evaluated)
        5: [
            ('Doctors considered to be next only to God. This is because they give new lives to people. They equipped with the knowledge and tools required to diagnose and treat various medical conditions.', 'AI_EVALUATED'),
            ('People rely on doctors for ensuring their health and well-being. They believe that they don\'t have to worry about any medical issue as long as they have these professionals besides them.', 'AI_EVALUATED'),
            ('The very first doctor is the general practitioner who sees the patient, tries to diagnose the patient, and sends him to the specialist doctor if necessary.', 'AI_EVALUATED'),
            ('The life of a physician/general practitioner is difficult. Often, in off-hours, he has to visit the patient, foregoing his rest, sleep, and even food.', 'AI_EVALUATED'),
            ('Doctors are a source of hope and fortitude. Even in distress, their obligation to their patient is first. He always remembers the famous Hippocratic Oath.', 'AI_EVALUATED'),
        ],
        
        # Task 6: Topical vocabulary (26 items from textbook)
        6: [
            ('tools', 'asboblar'),
            ('to diagnose', 'tashxis qo\'yish'),
            ('to treat', 'davolash'),
            ('medical conditions', 'tibbiy sharoitlar'),
            ('treatments', 'muolajalar'),
            ('medical staff', 'tibbiyot xodimlari'),
            ('nursing homes', 'qariyalar uylari'),
            ('to recover', 'sog\'ayish'),
            ('rely on', 'tayanib'),
            ('for ensuring', 'ta\'minlash uchun'),
            ('medical issue', 'tibbiy masala'),
            ('a sense of security', 'xavfsizlik hissi'),
            ('incidents', 'hodisalar'),
            ('to limelight', 'diqqat markazida bo\'lish'),
            ('public health organizations', 'davlat sog\'liqni saqlash tashkilotlari'),
            ('private practices', 'xususiy amaliyotlar'),
            ('very challenging', 'juda qiyin'),
            ('patients', 'bemorlar'),
            ('surgeon', 'jarroh'),
            ('a neurosurgeon', 'neyroxirurg'),
            ('pediatric neurosurgeon', 'bolalar neyroxirurg'),
            ('cardiologist', 'kardiolog'),
            ('immunologist', 'immunolog'),
            ('gynecologist', 'ginekolog'),
            ('Hippocratic Oath', 'Gippokrat qasamyodi'),
            ('fever', 'isitma'),
        ],
        
        # Task 7: Match the medical terms with their definitions (8 items from textbook)
        7: [
            ('patient', 'a person receiving or registered to receive medical treatment'),
            ('health', 'the state of being free from illness or injury'),
            ('surgeon', 'a medical practitioner qualified to practice surgery'),
            ('neurosurgeon', 'a surgeon specializing in surgery on the nervous system, especially the brain and spinal cord'),
            ('to diagnose', 'identify the nature of (an illness or other problem) by examination of the symptoms'),
            ('physician', 'a person qualified to practice medicine'),
            ('epidemic', 'a widespread occurrence of an infectious disease in a community at a particular time'),
            ('cough', 'expel air from the lungs with a sudden sharp sound'),
        ],
        
        # Task 8: Choose the best response to complete sentences (10 questions from textbook)
        8: [
            ('I\'m _____ for surgery tomorrow. (= having surgery)', 'going in', ['going in', 'going up', 'going out']),
            ('The tests are _____. We have to retest you.', 'inconclusive', ['incredulous', 'inconclusive', 'inclined']),
            ('Are you experiencing any _____? (= Do you feel tired?)', 'fatigue', ['dizziness', 'pain', 'fatigue']),
            ('Please _____ me (= let me know) of any changes in your condition.', 'notify/inform', ['notify/inform', 'note', 'review']),
            ('When there is a decrease in or disappearance of signs and symptoms of cancer, you can say that the cancer is in _____.', 'remission', ['regression', 'remittance', 'remission']),
            ('How _____ is this treatment? (= how well does this treatment work?)', 'effective', ['affected', 'effective', 'ineffectual']),
            ('I have a strange _____ (= red patches) on my skin.', 'rash', ['rash', 'rush', 'reach']),
            ('This won\'t _____ long. (= This won\'t require a lot of time.)', 'take', ['do', 'take', 'make']),
            ('Your regular doctor is often referred to as your "_____ care doctor."', 'primary', ['primal', 'primary', 'principal']),
            ('Most operations are not emergencies and are considered _____ surgery.', 'elective', ['choosy', 'picked', 'elective']),
        ],
        
        # Task 9: Fill in blanks with have or feel (6 questions from textbook)
        9: [
            ('Amir: Hi Bobir. How are you? Bobir: I _____ terrible.', 'feel'),
            ('Amir: What\'s the matter? Bobir: I _____ a headache and a sore throat.', 'have'),
            ('Amir: That\'s too bad. Do you _____ a cold?', 'have'),
            ('Bobir: Yes. I _____ an appointment to see the doctor today.', 'have'),
            ('Amir: Well, I hope you _____ better.', 'feel'),
            ('Bobir: Thanks. I hope I will _____ well soon.', 'feel'),
        ],
        
        # Task 10: Conversation questions (11 questions from textbook)
        10: [
            ('What are some of the qualities that make a good doctor?', 'AI_EVALUATED'),
            ('How important is empathy in the practice of medicine?', 'AI_EVALUATED'),
            ('What role does communication play in being a good doctor?', 'AI_EVALUATED'),
            ('How can doctors balance the need to provide high-quality care with the demands of a busy schedule?', 'AI_EVALUATED'),
            ('What impact can a good doctor have on a patient\'s overall health and well-being?', 'AI_EVALUATED'),
            ('What are some of the challenges that doctors face when it comes to staying up-to-date with the latest medical research?', 'AI_EVALUATED'),
            ('What are some examples of good doctors who have made significant contributions to the field of medicine?', 'AI_EVALUATED'),
            ('How important is cultural competency in providing good medical care?', 'AI_EVALUATED'),
            ('What role can technology play in helping doctors to provide better care?', 'AI_EVALUATED'),
            ('What are some of the ethical considerations that doctors must take into account when providing care?', 'AI_EVALUATED'),
            ('What advice would you give to someone who is looking for a good doctor?', 'AI_EVALUATED'),
        ],
        
        # Task 11: Speaking practice - Describe feeling younger/older (AI evaluated)
        11: [
            ('Describe a time when you felt younger or older than you actually were. You should say: when and where it was, what you think made you feel that way, how long the feeling lasted, say whether it was a pleasant feeling or not. Speak for 2 minutes.', 'AI_EVALUATED'),
        ],
        
        # Task 12: Writing task - Role-plays (AI evaluated)
        12: [
            ('Write a dialogue for one of these role-play situations: Role-play 1: Participants: Doctor, Mother, Daughter (age 5 years old). Location: Patient\'s house. Situation: Doctor makes a house call and has to diagnose what is wrong with the little girl. OR Role-play 2: Participants: Chemist, patient. Location: Chemist\'s shop. Situation: The patient has come for some medicine with a prescription, but the chemist cannot read the doctor\'s handwriting. Use medical vocabulary from this unit.', 'AI_EVALUATED'),
        ],
        
        # Task 13: Video retelling - Visiting the doctor (AI evaluated)
        13: [
            ('Watch the video "Visiting the doctor" and retell what it is about. Describe: the main points discussed, medical terminology used, and what you learned about doctor-patient communication.', 'AI_EVALUATED'),
        ],
    },
    'video_url': 'https://www.youtube.com/watch?v=bFx6WOwXLBE'
}
