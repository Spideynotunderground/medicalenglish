from django.conf import settings
import re
import random


class AIService:
    """AI evaluation service for various task types"""
    
    _client = None
    
    @classmethod
    def get_client(cls):
        if cls._client:
            return cls._client
        try:
            from openai import OpenAI
            api_key = getattr(settings, 'OPENAI_API_KEY', '')
            if not api_key:
                print("[AI] No API key found!")
                return None
            cls._client = OpenAI(api_key=api_key)
            print("[AI] OpenAI client created successfully")
            return cls._client
        except Exception as e:
            print(f"[AI] OpenAI client error: {e}")
            return None
    
    @staticmethod
    def mock_result():
        """Return mock result when AI unavailable"""
        score = random.randint(50, 85)
        return {'score': score, 'feedback': f'AI baholash hozircha mavjud emas. Test natijasi: {score}%'}
    
    @classmethod
    def evaluate(cls, task, answers):
        """Route to appropriate evaluator based on task type"""
        print(f"[AI] Evaluating task type: {task.task_type}")
        print(f"[AI] Answers received: {answers}")
        
        evaluators = {
            'translation': cls.evaluate_translation,
            'synonyms': cls.evaluate_synonyms,
            'speaking': cls.evaluate_speaking,
            'writing': cls.evaluate_writing,
            'conversation': cls.evaluate_conversation,
            'video': cls.evaluate_video,
        }
        
        evaluator = evaluators.get(task.task_type)
        if evaluator:
            return evaluator(task, answers)
        print(f"[AI] No evaluator for task type: {task.task_type}")
        return cls.mock_result()
    
    @classmethod
    def evaluate_translation(cls, task, answers):
        """Evaluate English to Uzbek translations, feedback in Uzbek"""
        client = cls.get_client()
        if not client:
            return cls.mock_result()
        
        # Build Q&A pairs from questions and answers
        questions = task.questions.all().order_by('order')
        qa_pairs = []
        
        for q in questions:
            # Try different key formats - frontend might send q.id as number or string
            student_answer = answers.get(str(q.id), '') or answers.get(q.id, '') or answers.get(f"q_{q.id}", '')
            if student_answer:
                qa_pairs.append({
                    'original': q.question_text,
                    'translation': student_answer
                })
        
        if not qa_pairs:
            return {'score': 0, 'feedback': 'Javob topilmadi. Iltimos, tarjimani kiriting.'}
        
        # Format for AI
        formatted_qa = ""
        for i, qa in enumerate(qa_pairs, 1):
            formatted_qa += f"\n{i}-gap:\nINGLIZCHA: {qa['original']}\nTALABA TARJIMASI: {qa['translation']}\n"
        
        total_sentences = len(questions)
        answered_sentences = len(qa_pairs)
        
        prompt = f"""Siz ingliz tili o'qituvchisisiz. Talabaning ingliz-o'zbek tarjimalarini QATTIQ tekshiring.

TARJIMALAR:
{formatted_qa}

JAMI: {answered_sentences}/{total_sentences} gap tarjima qilingan

BAHOLASH QOIDALARI:
- Tarjima O'ZBEK tilida bo'lishi SHART
- Ma'no to'liq va to'g'ri bo'lishi kerak
- Grammatik to'g'rilik muhim
- Ingliz tilidagi javob: 0 ball
- Ma'no to'liq noto'g'ri: 0 ball
- Ma'no qisman to'g'ri: 50 ball
- Ma'no to'liq to'g'ri: 100 ball

MUHIM: To'g'ri tarjimani YOZMA! Faqat xato yoki to'g'ri ekanligini ayting.

JAVOB FORMATI:
Score: [FAQAT RAQAM - 0 dan 100 gacha]%

Feedback:
[Har bir gap uchun ALOHIDA QATORDA yozing]

1-gap: ✅ yoki ❌ [qisqa izoh - xato bo'lsa nimasi noto'g'ri]

2-gap: ✅ yoki ❌ [qisqa izoh]

...

Umumiy xulosa: [1-2 gap bilan umumiy baho]

MISOL:
Score: 50%

Feedback:
1-gap: ✅ To'g'ri tarjima qilingan.

2-gap: ❌ Tarjima yo'q.

3-gap: ❌ "medicine" so'zi noto'g'ri tarjima qilingan.

4-gap: ✅ To'g'ri.

Umumiy xulosa: 4 ta gapdan 2 tasi to'g'ri tarjima qilingan. Tibbiy atamalarni yaxshiroq o'rganing."""

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            result = cls.parse_response(response.choices[0].message.content)
            print(f"[AI] Translation result: {result}")
            return result
        except Exception as e:
            print(f"[AI] Translation evaluation error: {e}")
            return cls.mock_result()
    
    @classmethod
    def evaluate_synonyms(cls, task, answers):
        """Evaluate English synonyms - student must provide English synonyms, feedback in Uzbek"""
        client = cls.get_client()
        if not client:
            return cls.mock_result()
        
        questions = task.questions.all().order_by('order')
        qa_pairs = []
        
        for idx, q in enumerate(questions, 1):
            student_answer = answers.get(str(q.id), '') or answers.get(q.id, '') or answers.get(f"q_{q.id}", '')
            qa_pairs.append({
                'number': idx,
                'word': q.question_text,
                'synonyms': student_answer if student_answer else '(javob berilmagan)'
            })
        
        if not any(qa['synonyms'] != '(javob berilmagan)' for qa in qa_pairs):
            return {'score': 0, 'feedback': 'Javob topilmadi.'}
        
        formatted_qa = ""
        for qa in qa_pairs:
            formatted_qa += f"\n{qa['number']}. So'z: \"{qa['word']}\"\n   Talaba javobi: {qa['synonyms']}\n"
        
        total_words = len(questions)
        answered_words = sum(1 for qa in qa_pairs if qa['synonyms'] != '(javob berilmagan)')
        
        prompt = f"""Siz ingliz tili o'qituvchisisiz. Talabaning sinonim javoblarini tekshiring.

SO'ZLAR VA JAVOBLAR:
{formatted_qa}

JAMI: {answered_words}/{total_words} so'zga javob berilgan

BAHOLASH QOIDALARI:
- Sinonimlar FAQAT ingliz tilida bo'lishi SHART
- Har bir so'z uchun kamida 1-2 ta to'g'ri sinonim kerak
- Sinonimlar haqiqatan ham sinonim bo'lishi kerak (ma'nosi o'xshash)
- O'zbek tilidagi javob: 0 ball
- Sinonim emas (antonim, boshqa so'z): 0 ball
- Javob berilmagan: 0 ball

MUHIM: To'g'ri javoblarni YOZMA! Faqat xato yoki to'g'ri ekanligini ayting.

JAVOB FORMATI:
Score: [FAQAT RAQAM - 0 dan 100 gacha]%

Feedback:
[Har bir so'z uchun ALOHIDA QATORDA yozing]

1. "so'z": ✅ yoki ❌ [qisqa izoh - xato bo'lsa sababi]

2. "so'z": ✅ yoki ❌ [qisqa izoh]

...

Umumiy xulosa: [1-2 gap bilan umumiy baho]

MISOL:
Score: 40%

Feedback:
1. "doctor": ✅ To'g'ri sinonimlar berilgan.

2. "illness": ❌ Ingliz tilida emas, o'zbek tilida yozilgan.

3. "medicine": ❌ Javob berilmagan.

4. "hospital": ✅ To'g'ri.

Umumiy xulosa: 4 ta so'zdan 2 tasiga to'g'ri sinonim berilgan. Javoblarni ingliz tilida yozing."""

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            result = cls.parse_response(response.choices[0].message.content)
            return result
        except Exception as e:
            print(f"[AI] Synonyms evaluation error: {e}")
            return cls.mock_result()
    
    @classmethod
    def evaluate_conversation(cls, task, answers):
        """Evaluate conversation answers - must be in English, feedback in Uzbek"""
        client = cls.get_client()
        if not client:
            return cls.mock_result()
        
        questions = task.questions.all().order_by('order')
        qa_pairs = []
        
        for idx, q in enumerate(questions, 1):
            student_answer = answers.get(str(q.id), '') or answers.get(q.id, '') or answers.get(f"q_{q.id}", '')
            qa_pairs.append({
                'number': idx,
                'question': q.question_text,
                'answer': student_answer if student_answer else '(javob berilmagan)'
            })
        
        if not any(qa['answer'] != '(javob berilmagan)' for qa in qa_pairs):
            return {'score': 0, 'feedback': 'Javob topilmadi.'}
        
        formatted_qa = ""
        for qa in qa_pairs:
            formatted_qa += f"\n{qa['number']}. Savol: {qa['question']}\n   Javob: {qa['answer']}\n"
        
        total_questions = len(questions)
        answered_questions = sum(1 for qa in qa_pairs if qa['answer'] != '(javob berilmagan)')
        
        prompt = f"""Siz ingliz tili o'qituvchisisiz. Talabaning suhbat javoblarini tekshiring.

SAVOLLAR VA JAVOBLAR:
{formatted_qa}

JAMI: {answered_questions}/{total_questions} savolga javob berilgan

BAHOLASH MEZONLARI:
- Javob ingliz tilida bo'lishi SHART
- Grammatik to'g'rilik
- Savolga to'liq javob berilganmi
- Javob mazmunli va mantiqiymi

QOIDALAR:
- Ingliz tilida EMAS bo'lgan javob: 0 ball
- Bo'sh yoki juda qisqa javob: 0 ball
- Grammatik xatolar ko'p bo'lsa: maksimum 50%
- Javob berilmagan savollar: 0 ball

MUHIM: To'g'ri javobni YOZMA! Faqat xato yoki to'g'ri ekanligini ayting.

JAVOB FORMATI:
Score: [FAQAT RAQAM - 0 dan 100 gacha]%

Feedback:
[Har bir savol uchun ALOHIDA QATORDA yozing]

1-savol: ✅ yoki ❌ [qisqa izoh]

2-savol: ✅ yoki ❌ [qisqa izoh]

...

Umumiy xulosa: [1-2 gap bilan umumiy baho va tavsiya]

MISOL:
Score: 50%

Feedback:
1-savol: ✅ To'g'ri va grammatik jihatdan to'g'ri.

2-savol: ❌ Ingliz tilida emas.

3-savol: ❌ Javob berilmagan.

4-savol: ⚠️ Grammatik xato bor, lekin mazmuni to'g'ri.

Umumiy xulosa: Javoblarni ingliz tilida yozing va grammatikaga e'tibor bering."""

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            result = cls.parse_response(response.choices[0].message.content)
            return result
        except Exception as e:
            print(f"[AI] Conversation evaluation error: {e}")
            return cls.mock_result()
    
    @classmethod
    def evaluate_speaking(cls, task, answers):
        """Evaluate speaking response - must be in English, feedback in Uzbek"""
        client = cls.get_client()
        if not client:
            return cls.mock_result()
        
        # Get the speaking topic from question
        question = task.questions.first()
        topic = question.question_text if question else "General topic"
        transcript = answers.get('transcript', '')
        
        if not transcript:
            return {'score': 0, 'feedback': 'Ovozli javob topilmadi. Iltimos, mikrofon orqali gapiring.'}
        
        word_count = len(transcript.split())
        
        prompt = f"""Siz ingliz tili o'qituvchisisiz. Talabaning og'zaki nutqini QATTIQ baholang.

MAVZU: {topic}
TALABA JAVOBI ({word_count} so'z): {transcript}

BAHOLASH MEZONLARI (har biri 20 ball):
1. GRAMMATIKA (20 ball): Gaplar to'g'ri tuzilganmi? Fe'l zamonlari to'g'rimi?
2. LUG'AT (20 ball): Tibbiy/mavzuga oid so'zlar ishlatilganmi?
3. MAVZUGA MOSLIK (20 ball): Javob mavzuga to'liq javob berganmi?
4. RAVONLIK (20 ball): Nutq uzluksiz va ravonmi?
5. SO'Z SONI (20 ball): Kamida 50 so'z bo'lishi kerak. {word_count} so'z = {min(20, word_count * 20 // 50)} ball

MUHIM QOIDALAR:
- Agar javob ingliz tilida EMAS bo'lsa: MAKSIMUM 20%
- Agar javob mavzuga UMUMAN mos kelmasa: MAKSIMUM 30%
- Agar juda qisqa (10 so'zdan kam): MAKSIMUM 25%
- Grammatik xatolar ko'p bo'lsa: HAR BIR xato uchun -5%

JAVOB FORMATI (aynan shu formatda):
Score: [FAQAT RAQAM]%
Feedback: [O'ZBEK TILIDA 2-3 qator. Aniq xatolarni ko'rsating va qanday yaxshilash mumkinligini ayting]

Masalan:
Score: 45%
Feedback: Grammatik xatolar: "I am want" o'rniga "I want" bo'lishi kerak. Mavzuga oid so'zlar kam ishlatilgan. Tibbiy terminlarni ko'proq qo'shing: "diagnosis", "treatment", "patient care"."""

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            result = cls.parse_response(response.choices[0].message.content)
            return result
        except Exception as e:
            print(f"[AI] Speaking evaluation error: {e}")
            return cls.mock_result()
    
    @classmethod
    def evaluate_writing(cls, task, answers):
        """Evaluate writing task - must be in English, feedback in Uzbek"""
        client = cls.get_client()
        if not client:
            return cls.mock_result()
        
        question = task.questions.first()
        prompt_text = question.question_text if question else "Write an essay"
        
        # Try multiple key formats
        essay = answers.get('essay', '')
        if not essay and question:
            essay = answers.get(str(question.id), '') or answers.get(question.id, '') or answers.get(f"q_{question.id}", '')
        
        if not essay:
            return {'score': 0, 'feedback': 'Esse topilmadi. Iltimos, matn yozing.'}
        
        word_count = len(essay.split())
        
        prompt = f"""Siz ingliz tili o'qituvchisisiz. Talabaning yozma ishini QATTIQ baholang.

TOPSHIRIQ: {prompt_text}
TALABA ESSESI ({word_count} so'z): {essay}

BAHOLASH MEZONLARI (har biri 20 ball):
1. GRAMMATIKA (20 ball): Gaplar to'g'ri tuzilganmi? Tinish belgilari to'g'rimi?
2. LUG'AT (20 ball): So'z boyligi yetarlimi? Tibbiy terminlar ishlatilganmi?
3. TUZILISH (20 ball): Kirish, asosiy qism, xulosa bormi?
4. MAVZUGA MOSLIK (20 ball): Topshiriqqa to'liq javob berganmi?
5. SO'Z SONI (20 ball): 150-200 so'z kerak. {word_count} so'z = {20 if 140 <= word_count <= 210 else (15 if 100 <= word_count <= 250 else (10 if 50 <= word_count <= 300 else 5))} ball

MUHIM QOIDALAR:
- Agar esse ingliz tilida EMAS bo'lsa: MAKSIMUM 15%
- Agar mavzuga UMUMAN mos kelmasa: MAKSIMUM 25%
- Agar juda qisqa (50 so'zdan kam): MAKSIMUM 30%
- HAR BIR grammatik xato uchun: -3%
- Tuzilish yo'q bo'lsa (faqat bir paragraf): -15%

JAVOB FORMATI (aynan shu formatda):
Score: [FAQAT RAQAM]%
Feedback: [O'ZBEK TILIDA 2-3 qator. Aniq xatolarni ko'rsating va qanday yaxshilash kerakligini ayting]

Masalan:
Score: 52%
Feedback: Grammatik xatolar: "I want become doctor" o'rniga "I want to become a doctor". Esse tuzilishi yaxshi, lekin xulosa qismi yo'q. So'z soni yetarli (165 so'z). Tibbiy terminlarni ko'proq ishlating."""

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            result = cls.parse_response(response.choices[0].message.content)
            return result
        except Exception as e:
            print(f"[AI] Writing evaluation error: {e}")
            return cls.mock_result()
    
    @classmethod
    def evaluate_video(cls, task, answers):
        """Evaluate video retelling - must be in English, feedback in Uzbek"""
        client = cls.get_client()
        if not client:
            return cls.mock_result()
        
        question = task.questions.first()
        topic = question.question_text if question else "Video retelling"
        
        # Try multiple key formats
        retelling = answers.get('retelling', '')
        if not retelling and question:
            retelling = answers.get(str(question.id), '') or answers.get(question.id, '') or answers.get(f"q_{question.id}", '')
        
        if not retelling:
            return {'score': 0, 'feedback': 'Video haqida hikoya topilmadi.'}
        
        word_count = len(retelling.split())
        
        prompt = f"""Siz ingliz tili o'qituvchisisiz. Talabaning video qayta hikoyasini QATTIQ baholang.

VIDEO MAVZUSI: {topic}
TALABA HIKOYASI ({word_count} so'z): {retelling}

BAHOLASH MEZONLARI (har biri 25 ball):
1. GRAMMATIKA (25 ball): Gaplar to'g'ri tuzilganmi?
2. LUG'AT (25 ball): Tibbiy/mavzuga oid so'zlar ishlatilganmi?
3. MAZMUN (25 ball): Video mazmunini to'g'ri tushunib yetkazganmi?
4. SO'Z SONI (25 ball): Kamida 80 so'z kerak. {word_count} so'z = {min(25, word_count * 25 // 80)} ball

MUHIM QOIDALAR:
- Agar hikoya ingliz tilida EMAS bo'lsa: MAKSIMUM 15%
- Agar mavzuga UMUMAN mos kelmasa: MAKSIMUM 20%
- Agar juda qisqa (30 so'zdan kam): MAKSIMUM 25%
- HAR BIR grammatik xato uchun: -4%

JAVOB FORMATI:
Score: [FAQAT RAQAM]%
Feedback: [O'ZBEK TILIDA 2-3 qator. Aniq xatolarni ko'rsating]"""

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            result = cls.parse_response(response.choices[0].message.content)
            return result
        except Exception as e:
            print(f"[AI] Video evaluation error: {e}")
            return cls.mock_result()
    
    @staticmethod
    def parse_response(content):
        """Extract score and feedback from AI response"""
        print(f"[AI] Parsing response: {content[:300]}...")
        
        # Find score
        score_match = re.search(r'Score:\s*(\d+)%?', content, re.IGNORECASE)
        score = int(score_match.group(1)) if score_match else 50
        
        # Find feedback - everything after "Feedback:"
        feedback_match = re.search(r'Feedback:\s*(.+)', content, re.IGNORECASE | re.DOTALL)
        if feedback_match:
            feedback = feedback_match.group(1).strip()
        else:
            # If no explicit feedback label, use everything after score
            feedback = re.sub(r'Score:\s*\d+%?\s*', '', content).strip()
        
        # Clean up feedback
        feedback = feedback[:1000]  # Limit length
        
        return {'score': min(max(score, 0), 100), 'feedback': feedback}
