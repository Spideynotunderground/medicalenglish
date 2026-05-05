import { BookOpen, Award, Users, Zap, CheckCircle, Sparkles } from 'lucide-react'

export default function About() {
  return (
    <div className="animate-fade-in">
      <div className="card bg-gradient-to-r from-blue-500 to-purple-600 text-white mb-6">
        <h1 className="text-2xl font-bold mb-2">Platforma haqida</h1>
        <p className="text-white/80">
          "English for Medical Students" - tibbiyot talabalari uchun ingliz tilini o'rgatuvchi interaktiv platforma.
        </p>
      </div>
      
      <div className="grid md:grid-cols-2 gap-4 mb-6">
        <div className="card">
          <h3 className="font-semibold mb-3 flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-blue-500" />
            Kurs tarkibi
          </h3>
          <ul className="space-y-2 text-sm text-gray-600">
            <li className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4 text-green-500" />
              15 ta mavzu bo'yicha tuzilgan darslar
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4 text-green-500" />
              Har bir mavzuda 13 ta topshiriq
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4 text-green-500" />
              Jami 195 ta topshiriq
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4 text-green-500" />
              Tibbiy lug'at - Glossariy
            </li>
          </ul>
        </div>
        
        <div className="card">
          <h3 className="font-semibold mb-3 flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-purple-500" />
            AI baholash
          </h3>
          <ul className="space-y-2 text-sm text-gray-600">
            <li className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4 text-green-500" />
              Translation - tarjima baholash
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4 text-green-500" />
              Synonyms - sinonimlar
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4 text-green-500" />
              Speaking - gapirish
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4 text-green-500" />
              Writing - yozish
            </li>
          </ul>
        </div>
      </div>
      
      <div className="card mb-6">
        <h3 className="font-semibold mb-3">Topshiriq turlari</h3>
        <div className="grid grid-cols-2 md:grid-cols-3 gap-2">
          {[
            { name: 'Fill in the blanks', desc: 'Bo\'sh joylarni to\'ldirish' },
            { name: 'Identify tense', desc: 'Grammatik zamon aniqlash' },
            { name: 'Matching', desc: 'Moslashtirish' },
            { name: 'Verb forms', desc: 'Fe\'l shakllari' },
            { name: 'Vocabulary', desc: 'Lug\'at testi' },
            { name: 'Crossword', desc: 'Krossvord' },
            { name: 'Insert words', desc: 'So\'z qo\'yish' },
            { name: 'Translation', desc: 'Tarjima (AI)', ai: true },
            { name: 'Synonyms', desc: 'Sinonimlar (AI)', ai: true },
            { name: 'Conversation', desc: 'Suhbat (AI)', ai: true },
            { name: 'Speaking', desc: 'Gapirish (AI)', ai: true },
            { name: 'Writing', desc: 'Yozish (AI)', ai: true },
            { name: 'Video retelling', desc: 'Video hikoya (AI)', ai: true },
          ].map((t, i) => (
            <div key={i} className={`p-3 rounded-lg ${t.ai ? 'bg-purple-50 border border-purple-200' : 'bg-gray-50'}`}>
              <div className="font-medium text-sm">{t.name}</div>
              <div className="text-xs text-gray-500">{t.desc}</div>
            </div>
          ))}
        </div>
      </div>
      
      <div className="card">
        <h3 className="font-semibold mb-3 flex items-center gap-2">
          <Award className="w-5 h-5 text-yellow-500" />
          Ball va reyting tizimi
        </h3>
        <p className="text-sm text-gray-600 mb-3">
          Har bir topshiriqni muvaffaqiyatli bajarsangiz ball olasiz. Ballar yig'ilishi bilan 
          darajangiz oshadi va reytingda ko'tarilasiz.
        </p>
        <div className="grid grid-cols-3 gap-3 text-center">
          <div className="bg-blue-50 p-3 rounded-lg">
            <div className="text-2xl font-bold text-blue-600">500</div>
            <div className="text-xs text-gray-500">ball = 1 level</div>
          </div>
          <div className="bg-orange-50 p-3 rounded-lg">
            <div className="text-2xl font-bold text-orange-600">7</div>
            <div className="text-xs text-gray-500">kun streak = nishon</div>
          </div>
          <div className="bg-green-50 p-3 rounded-lg">
            <div className="text-2xl font-bold text-green-600">60%</div>
            <div className="text-xs text-gray-500">o'tish balli</div>
          </div>
        </div>
      </div>
    </div>
  )
}
