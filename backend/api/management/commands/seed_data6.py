"""
Unit 6: Medical education in Uzbekistan - Continuous Tenses in the Passive Voice
"""

UNIT_6_DATA = {
    'unit': {
        'number': 6,
        'title': 'Medical education in Uzbekistan',
        'description': 'Continuous Tenses in the Passive Voice'
    },
    'tasks': {
        # Task 1: Rewrite sentences using Present Simple Passive or Present Continuous Passive (10 questions)
        1: [
            ('They discuss profits every Monday. → Profits _____ every Monday.', 'are discussed'),
            ('They are discussing profits now. → Profits _____ now.', 'are being discussed'),
            ('She asks this student twice a week. → This student _____ twice a week.', 'is asked'),
            ('She is asking this student now. → This student _____ now.', 'is being asked'),
            ('They renovate this building once a decade. → This building _____ once a decade.', 'is renovated'),
            ('They are renovating this building now. → This building _____ now.', 'is being renovated'),
            ('Somebody is looking at me. → I _____.', 'am being looked at'),
            ('She washes her sons\' sweatshirts twice a week. → Her sons\' sweatshirts _____ twice a week.', 'are washed'),
            ('They are counting the money. → The money _____.', 'is being counted'),
            ('Someone is painting the walls. → The walls _____.', 'are being painted'),
        ],
        
        # Task 2: Match sentence beginnings to correct endings (8 questions)
        2: [
            ('The exam _____', 'is being held in the main hall.'),
            ('Three people _____', 'are being held against their will.'),
            ('The building where I work _____', 'is being renovated right now.'),
            ('When I arrived at the party, drinks _____', 'were being served.'),
            ('Dinner isn\'t ready yet. It _____', 'is still being prepared.'),
            ('In 1992 the bridge _____', 'was still being built.'),
            ('Reservations _____', 'are not being taken any more.'),
            ('A number of changes _____', 'are being made to the procedure.'),
        ],
        
        # Task 3: Choose the best option (6 questions)
        3: [
            ('Concert tickets _____ at the box office.', 'are being sold', ['being sold', 'are being sold', 'are be sold', 'are being selling']),
            ('Following yesterday\'s accident, 3 people are still _____ for minor injuries.', 'being treated', ['treated', 'being treating', 'treating', 'being treated']),
            ('Your suit is not ready yet. It _____ right now.', 'is being cleaned', ['is being cleaned', 'is being cleaning', 'is been cleaned', 'is cleaning']),
            ('I could not use my car yesterday because it _____.', 'was being serviced', ['was being serviced', 'were being serviced', 'was being service', 'was been serviced']),
            ('He left the room while the money _____.', 'was being collected', ['has being collected', 'was been collected', 'was being collected', 'was being collecting']),
            ('We couldn\'t use the bathroom while it _____.', 'was being refitted', ['was been refitted', 'was being refitted', 'is being refitted', 'was refitting']),
        ],
        
        # Task 4: Choose the correct answer - Medical advice (10 questions)
        4: [
            ('Regular exercise is _____ for the heart.', 'good', ['bad', 'good', 'dangerous', 'unnecessary']),
            ('A balanced diet should provide all the _____ needed.', 'nutrients', ['vitamins', 'nutrients', 'proteins', 'calories']),
            ('Medicines should be kept out of the reach of _____.', 'children', ['adults', 'doctors', 'children', 'nurses']),
            ('A patient in shock should be kept _____ and lying down.', 'warm', ['cold', 'warm', 'standing', 'sitting']),
            ('Not taking any exercise is an _____ way of living.', 'unhealthy', ['healthy', 'unhealthy', 'normal', 'active']),
            ('Reading in bad light can make the eyes _____.', 'ache', ['strong', 'ache', 'better', 'healthy']),
            ('A normal adult should drink about _____ litres of fluid each day.', '2.5', ['1.0', '2.5', '5.0', '0.5']),
            ('HIV can be transmitted by using _____ needles.', 'non-sterile', ['sterile', 'non-sterile', 'clean', 'new']),
            ('Bad posture can cause _____ pain.', 'back', ['head', 'back', 'stomach', 'chest']),
            ('Surgical instruments must be _____ before use.', 'sterilized', ['cleaned', 'sterilized', 'washed', 'dried']),
        ],
        
        # Task 5: Read and translate - MEDICAL EDUCATION IN UZBEKISTAN text (AI evaluated)
        5: [
            ('The main task of medicine is the care about the people\'s health. For that reason, the training of the medical personnel is very important. Medical Universities and Academies train future doctors, pharmacists, and stomatologists.', 'AI_EVALUATED'),
            ('Doctors\' training takes six years but stomatologists\' or pharmacists\' training lasts five years. The curriculum and syllabuses for these Universities are approved by the Ministry of Public Health.', 'AI_EVALUATED'),
            ('During the first two years the students of the Medical Universities have so-called pre-clinical training, which includes general subjects, as Physics, Chemistry, Anatomy, Biology and others.', 'AI_EVALUATED'),
            ('In the senior years they study clinical subjects, as Therapy, Surgery, Obstetrics, Gynaecology and others. The senior students acquire practical skills, working at hospitals, polyclinics, sanitary epidemiological stations, and chemist\'s shops.', 'AI_EVALUATED'),
            ('They acquire such practical skills, as to examine patients, to make a diagnosis, to prescribe proper treatment, and to fill in case histories. A lot of students participate in scientific societies; their dream is to become research workers in future.', 'AI_EVALUATED'),
        ],
        
        # Task 6: Topical vocabulary (19 items from textbook)
        6: [
            ('medical personnel', 'tibbiyot xodimlari'),
            ('pharmacist', 'farmatsevt'),
            ('curriculum', 'o\'quv reja'),
            ('syllabuses', 'o\'quv dasturlari'),
            ('to be approved', 'tasdiqlanishi kerak'),
            ('administrative affairs', 'ma\'muriy ishlar'),
            ('pre-clinical training', 'klinikadan oldingi tayyorgarlik'),
            ('general subjects', 'umumiy fanlar'),
            ('clinical subjects', 'klinik fanlar'),
            ('surgery', 'jarrohlik'),
            ('obstetrics', 'akusherlik'),
            ('to acquire', 'egallash'),
            ('chemist\'s shops', 'dorixona'),
            ('to examine patients', 'bemorlarni tekshirish'),
            ('to make a diagnosis', 'tashxis qo\'yish'),
            ('to prescribe proper treatment', 'to\'g\'ri davolanishni tayinlash'),
            ('to fill in case histories', 'kasallik varaqasini to\'ldirish'),
            ('to work as interns', 'stajyor sifatida ishlash'),
            ('to obtain degrees', 'ilmiy darajani olish'),
        ],
        
        # Task 7: Match words with definitions (8 questions)
        7: [
            ('pharmacist', 'a person who is professionally qualified to prepare and dispense medicinal drugs'),
            ('curriculum', 'the subjects comprising a course of study in a school or college'),
            ('treatment', 'the manner in which someone behaves toward or deals with someone or something'),
            ('laboratory', 'a room or building equipped for scientific experiments, research, or teaching'),
            ('syllabus', 'an outline of the subjects in a course of study or teaching'),
            ('specialist', 'a person highly skilled in a specific and restricted field'),
            ('candidate', 'a person who applies for a job or is nominated for election'),
            ('to prescribe', 'advise and authorize the use of a medicine or treatment for someone'),
        ],
        
        # Task 8: Choose the right word (10 questions)
        8: [
            ('Discussion between doctor and patient', 'consultation', ['collaboration', 'consultation', 'cooperation']),
            ('Physical signs of a medical problem', 'symptoms', ['variations', 'mutations', 'symptoms']),
            ('Pathogen that does not respond to antibiotics', 'virus', ['virus', 'bacteria', 'symptom']),
            ('Drugs used against bacterial infections', 'antibiotics', ['antibodies', 'antibiotics', 'antivirals']),
            ('Protects body against pathogens', 'immune system', ['immune system', 'lymphatic system', 'respiratory system']),
            ('Deals with the skin', 'Dermatology', ['Orthopedics', 'Neurology', 'Dermatology']),
            ('Deals with the nervous system', 'Neurology', ['Orthopedics', 'Neurology', 'Dermatology']),
            ('Deals with children', 'Pediatrics', ['Neurology', 'Radiology', 'Pediatrics']),
            ('Uses imaging technology', 'Radiology', ['Orthopedics', 'Dermatology', 'Radiology']),
            ('Would deal with a broken leg', 'Orthopedics', ['Orthopedics', 'Neurology', 'Radiology']),
        ],
        
        # Task 9: Read dialogue - Nurse and client at medical center (fill in based on dialogue)
        9: [
            ('What is the nurse\'s name?', 'Feruza'),
            ('How long has the nurse been working?', 'three years'),
            ('How old is the client?', '72 years old'),
            ('Why is the client at the hospital?', 'for a hip replacement'),
            ('Who will come to see the client?', 'her orthopedic surgeon'),
            ('When will the nurse be back?', 'tomorrow at 7:00 a.m.'),
        ],
        
        # Task 10: Conversation questions about medical education (AI evaluated)
        10: [
            ('Can a medical educator focus on a specific subject while teaching in Medical Education?', 'AI_EVALUATED'),
            ('What is the role of patient-centered healthcare approach in developing medical education curriculum?', 'AI_EVALUATED'),
            ('Will prioritization of AI and machine learning in higher education improve the competency of future health professionals?', 'AI_EVALUATED'),
            ('Should unconventional forms of medicine be part of national healthcare?', 'AI_EVALUATED'),
            ('What are the applications of bioinformatics in medicine?', 'AI_EVALUATED'),
            ('How to become a good learner in medical education?', 'AI_EVALUATED'),
        ],
        
        # Task 11: Speaking practice - Describe a time when you had some medicine (AI evaluated)
        11: [
            ('Describe a time when you had some medicine. You should say: when it was, what exactly happened, did you recover from it, explain how you felt after. Speak for 2 minutes.', 'AI_EVALUATED'),
        ],
        
        # Task 12: Writing task - Medical school letter of intent (AI evaluated)
        12: [
            ('Write a Medical school letter of intent (150-200 words). Include: An expression of thanks for considering your application, A recap of what you especially appreciate about their school, Updates since you last communicated with them, What you will contribute to the school, A clear statement that you will attend if admitted.', 'AI_EVALUATED'),
        ],
        
        # Task 13: Video - Medical Education (AI evaluated)
        13: [
            ('Watch the video "Medical Education" and retell: What are the main aspects of medical education discussed? What challenges are mentioned? What solutions are proposed? Summarize the key points.', 'AI_EVALUATED'),
        ],
    },
    'video_url': 'https://www.youtube.com/watch?v=zFf1y4X_uQc'
}
