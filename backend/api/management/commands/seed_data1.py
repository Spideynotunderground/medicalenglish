"""
Unit 1: Introducing myself - Simple Tenses in the Active Voice
"""

UNIT_1_DATA = {
    'unit': {
        'number': 1,
        'title': 'Introducing myself',
        'description': 'Simple Tenses in the Active Voice'
    },
    'tasks': {
        # Task 1: Fill in the blanks - Past tense medical verbs (15 questions from textbook)
        1: [
            ('He _____ (receive) a new kidney from his brother.', 'received'),
            ('He _____ (strain) his back lifting the table.', 'strained'),
            ('She _____ (recover) from her concussion in a few days.', 'recovered'),
            ('It was so hot standing in the sun that he _____ (faint).', 'fainted'),
            ('The doctors decided that her condition _____ (require) surgery.', 'required'),
            ('She _____ (suffer) from poor circulation, which made her feel the cold.', 'suffered'),
            ('She _____ (adapt) well to her new diet.', 'adapted'),
            ('The embryo _____ (develop) quite normally in spite of the mother\'s illness.', 'developed'),
            ('His tibia _____ (fracture) in two places.', 'fractured'),
            ('The patient _____ (react) badly to the penicillin.', 'reacted'),
            ('The nurse _____ (weigh) the baby on the scales.', 'weighed'),
            ('The treatment _____ (prolong) her life by three years.', 'prolonged'),
            ('Playing football only _____ (aggravate) his knee injury.', 'aggravated'),
            ('The doctor _____ (examine) the boy\'s throat.', 'examined'),
            ('His hands _____ (tremble) with the cold.', 'trembled'),
        ],
        
        # Task 2: Identify the tense - Present Simple or Future Simple (7 questions from textbook)
        2: [
            ('They will visit you before Christmas.', 'Future Simple', ['Present Simple', 'Future Simple']),
            ('I have a few dollars you can borrow.', 'Present Simple', ['Present Simple', 'Future Simple']),
            ('The man believes anyone can be a king.', 'Present Simple', ['Present Simple', 'Future Simple']),
            ('Are you happy?', 'Present Simple', ['Present Simple', 'Future Simple']),
            ('We watch football games at school every Friday.', 'Present Simple', ['Present Simple', 'Future Simple']),
            ('I will allow him to pursue the project.', 'Future Simple', ['Present Simple', 'Future Simple']),
            ('We will have sashimi for dinner later.', 'Future Simple', ['Present Simple', 'Future Simple']),
        ],
        
        # Task 3: Fill in - Simple Past/Present/Future - Murod story (textbook Task 4)
        3: [
            ('Murod _____ (be) a salesman.', 'is'),
            ('Every day he _____ (call) people up and _____ (offer) them products.', 'calls, offers'),
            ('He _____ (be) really good at it, too.', 'is'),
            ('He always _____ (talk) about how much he _____ (love) his job.', 'talks, loves'),
            ('When people _____ (hear) this they _____ (be) usually very surprised.', 'hear, are'),
            ('"_____ (be) you serious?" they _____ (ask).', 'Are, ask'),
            ('"Most people _____ (not like) to sell stuff!"', 'do not like'),
            ('"This guy _____ (hate) to do it, and that guy _____ (not like) it…"', 'hates, does not like'),
            ('To that Murod generally _____ (reply)...', 'replies'),
            ('"In the past I _____ (work) very hard but I _____ (not get) any sales."', 'worked, did not get'),
            ('"So I _____ (not like) my job at all."', 'did not like'),
            ('"Then I _____ (learn) about how to sell, and _____ (practice) a lot."', 'learned, practiced'),
            ('"I _____ (practice) so much that it _____ (become) easy for me."', 'practiced, became'),
            ('"I _____ (start) to make more and more sales."', 'started'),
            ('"My boss _____ (love) it and he _____ (increase) my salary."', 'loved, increased'),
            ('"Now I _____ (be) very good at it, and I _____ (have) a lot of fun."', 'am, have'),
            ('"I _____ (help) people buy the stuff they _____ (need)."', 'help, need'),
            ('"_____ (you work) as a salesman forever?" people _____ (ask) him.', 'Will you work, ask'),
            ('"I _____ (not know)," Murod _____ (reply).', 'do not know, replies'),
            ('He _____ (think) that he _____ (have) to wait and see.', 'thinks, has'),
            ('"Maybe I _____ (continue) to work as a salesman," he _____ (say).', 'will continue, says'),
            ('"And maybe I _____ (change) my profession."', 'will change'),
            ('"It _____ (depend) on what I _____ (prefer)."', 'depends, prefer'),
            ('"But for now, I _____ (be) happy!"', 'am'),
        ],
        
        # Task 4: Choose the correct answer - Crossword/Multiple choice
        4: [
            ('Which tense: "I study medicine every day"?', 'Present Simple', ['Present Simple', 'Past Simple', 'Future Simple', 'Present Continuous']),
            ('Which tense: "She visited the doctor yesterday"?', 'Past Simple', ['Present Simple', 'Past Simple', 'Future Simple', 'Present Perfect']),
            ('Which tense: "They will graduate next year"?', 'Future Simple', ['Present Simple', 'Past Simple', 'Future Simple', 'Present Continuous']),
            ('Which tense: "The patient takes medicine daily"?', 'Present Simple', ['Present Simple', 'Past Simple', 'Future Simple', 'Present Perfect']),
            ('Which tense: "We examined the patient yesterday"?', 'Past Simple', ['Present Simple', 'Past Simple', 'Future Simple', 'Present Continuous']),
            ('Which tense: "He will become a doctor"?', 'Future Simple', ['Present Simple', 'Past Simple', 'Future Simple', 'Present Perfect']),
            ('Which tense: "Doctors help people"?', 'Present Simple', ['Present Simple', 'Past Simple', 'Future Simple', 'Present Continuous']),
            ('Which tense: "The surgery lasted 3 hours"?', 'Past Simple', ['Present Simple', 'Past Simple', 'Future Simple', 'Present Perfect']),
        ],
        
        # Task 5: Read and translate - INTRODUCING MYSELF text (AI evaluated)
        5: [
            ('My name is Aziz Karimov. I am from Bukhara. I am 17 years old. I was born on the 17th of September in Samarkand, which is considered to be one of the ancient cities in Uzbekistan.', 'AI_EVALUATED'),
            ('Now I am a first-year student of the Medical Educational Establishment. I was working hard during the whole year having extra lessons in Physics, Biology, and English because the competition was very high.', 'AI_EVALUATED'),
            ('A good doctor must have not only deep knowledge of a particular field of medicine. He must love people and have a kind heart.', 'AI_EVALUATED'),
            ('My working day begins early because the classes start at half past 8. So, I get up at 7 o\'clock. First of all, I make my bed, do my morning exercises and go to the bathroom.', 'AI_EVALUATED'),
        ],
        
        # Task 6: Topical vocabulary (13 items from textbook)
        6: [
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
        
        # Task 7: Match words with definitions (8 items from textbook)
        7: [
            ('biology', 'the study of living organisms, divided into many specialized fields'),
            ('medical', 'relating to the science of medicine, or to the treatment of illness and injuries'),
            ('disease', 'a disorder of structure or function in a human, animal, or plant'),
            ('histology', 'the study of the microscopic structure of tissues'),
            ('hospital', 'an institution providing medical and surgical treatment and nursing care'),
            ('doctor', 'a qualified practitioner of medicine; a physician'),
            ('anatomy', 'the branch of science concerned with the bodily structure of humans and animals'),
            ('textbook', 'a book used as a standard work for the study of a particular subject'),
        ],
        
        # Task 8: Insert the missing words (6 questions from textbook)
        8: [
            ('_____ must have not only deep knowledge of a particular field of medicine.', 'A good doctor'),
            ('When I have _____ I watch TV, listen to the music or visit my friends or they come to visit me.', 'spare time'),
            ('My working day begins _____ because the classes start at half past 8.', 'early'),
            ('I consider that physical exercises are _____ for the protection of my health against diseases.', 'a good remedy'),
            ('We have several _____ and a lecture every day.', 'practical classes'),
            ('Medical students _____ that it is not easy to be a good specialist.', 'must remember'),
        ],
        
        # Task 9: Find synonyms (AI evaluated - 8 words)
        9: [
            ('a long way', 'AI_EVALUATED'),
            ('hard', 'AI_EVALUATED'),
            ('medical science', 'AI_EVALUATED'),
            ('discipline', 'AI_EVALUATED'),
            ('dormitory', 'AI_EVALUATED'),
            ('dreadful', 'AI_EVALUATED'),
            ('include', 'AI_EVALUATED'),
            ('defense', 'AI_EVALUATED'),
        ],
        
        # Task 10: Conversation questions (20 questions from textbook)
        10: [
            ('How old are you?', 'AI_EVALUATED'),
            ('What would you like to be?', 'AI_EVALUATED'),
            ('Where are you from?', 'AI_EVALUATED'),
            ('When and where were you born?', 'AI_EVALUATED'),
            ('How many persons are there in your family?', 'AI_EVALUATED'),
            ('What is your mother\'s name?', 'AI_EVALUATED'),
            ('What is your father\'s name?', 'AI_EVALUATED'),
            ('How old is your father?', 'AI_EVALUATED'),
            ('What is your mother\'s occupation?', 'AI_EVALUATED'),
            ('What is your father doing for living?', 'AI_EVALUATED'),
            ('Do you have brothers or sisters?', 'AI_EVALUATED'),
            ('How old are your sisters and brothers?', 'AI_EVALUATED'),
            ('How many children does your sister/brother have?', 'AI_EVALUATED'),
            ('When does your working day begin?', 'AI_EVALUATED'),
            ('What do you do in the morning?', 'AI_EVALUATED'),
            ('When do you leave your home?', 'AI_EVALUATED'),
            ('How many classes do you have every day?', 'AI_EVALUATED'),
            ('What subjects do you study?', 'AI_EVALUATED'),
            ('What do you do after classes?', 'AI_EVALUATED'),
            ('When do you go to bed?', 'AI_EVALUATED'),
        ],
        
        # Task 11: Speaking practice - Talk about dream job (AI evaluated)
        11: [
            ('Talk about your dream job – Doctor. You should say: what it is, what it is like, what qualification you need for this job, explain why you think it is perfect. Speak for 2 minutes.', 'AI_EVALUATED'),
        ],
        
        # Task 12: Writing task - Essay (AI evaluated)
        12: [
            ('Write an essay (150-200 words) about "Why I want to become a doctor". Include: your motivation for choosing medicine, what qualities a good doctor should have, your future goals and plans.', 'AI_EVALUATED'),
        ],
        
        # Task 13: Video retelling (AI evaluated)
        13: [
            ('Watch the video "I am a medical student" and retell what it is about. Describe: what the video shows, what you learned from it, how it relates to your own experience.', 'AI_EVALUATED'),
        ],
    },
    'video_url': 'https://www.youtube.com/watch?v=WaZcBJZCwqA'
}
