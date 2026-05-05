import { BookOpen, Award, Users, Zap, Sparkles, Brain, Mic, PenTool, Video, MessageSquare } from 'lucide-react'

export default function Home() {
  return (
    <div className="space-y-8 animate-fade-in">
      {/* Stats */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {[
          { icon: BookOpen, value: '15', label: 'Mavzular', gradient: 'from-blue-500 to-indigo-600', bg: 'bg-blue-50', shadow: 'shadow-blue-500/20' },
          { icon: Zap, value: '195', label: 'Topshiriqlar', gradient: 'from-amber-500 to-orange-600', bg: 'bg-amber-50', shadow: 'shadow-amber-500/20' },
          { icon: Award, value: '13', label: 'Topshiriq turi', gradient: 'from-purple-500 to-pink-600', bg: 'bg-purple-50', shadow: 'shadow-purple-500/20' },
          { icon: Users, value: '1.2K+', label: 'Foydalanuvchilar', gradient: 'from-emerald-500 to-teal-600', bg: 'bg-emerald-50', shadow: 'shadow-emerald-500/20' },
        ].map((stat, i) => (
          <div key={i} className={`bg-white rounded-2xl p-6 text-center shadow-xl ${stat.shadow} border border-gray-100 hover:scale-105 transition-transform cursor-pointer`}>
            <div className={`w-14 h-14 mx-auto mb-4 rounded-2xl bg-gradient-to-br ${stat.gradient} flex items-center justify-center shadow-lg`}>
              <stat.icon className="w-7 h-7 text-white" />
            </div>
            <div className={`text-3xl font-black bg-gradient-to-r ${stat.gradient} bg-clip-text text-transparent`}>{stat.value}</div>
            <div className="text-sm text-gray-500 font-medium mt-1">{stat.label}</div>
          </div>
        ))}
      </div>
      
      {/* Features */}
      <div className="grid md:grid-cols-3 gap-5">
        <div className="bg-white rounded-2xl p-6 shadow-xl shadow-blue-500/10 border border-gray-100 hover:shadow-2xl transition-shadow group">
          <div className="w-12 h-12 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
            <BookOpen className="w-6 h-6 text-white" />
          </div>
          <h3 className="font-bold text-lg mb-2 text-gray-800">Mavzular</h3>
          <p className="text-gray-500 text-sm leading-relaxed">15 ta mavzu bo'yicha tuzilgan darslar. Har bir mavzuda 13 ta interaktiv topshiriq.</p>
        </div>
        
        <div className="bg-white rounded-2xl p-6 shadow-xl shadow-purple-500/10 border border-gray-100 hover:shadow-2xl transition-shadow group">
          <div className="w-12 h-12 bg-gradient-to-br from-purple-500 to-pink-600 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
            <Brain className="w-6 h-6 text-white" />
          </div>
          <h3 className="font-bold text-lg mb-2 text-gray-800">AI Baholash</h3>
          <p className="text-gray-500 text-sm leading-relaxed">Speaking, Writing, Translation kabi topshiriqlar sun'iy intellekt yordamida baholanadi.</p>
        </div>
        
        <div className="bg-white rounded-2xl p-6 shadow-xl shadow-amber-500/10 border border-gray-100 hover:shadow-2xl transition-shadow group">
          <div className="w-12 h-12 bg-gradient-to-br from-amber-500 to-orange-600 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
            <Award className="w-6 h-6 text-white" />
          </div>
          <h3 className="font-bold text-lg mb-2 text-gray-800">Reyting</h3>
          <p className="text-gray-500 text-sm leading-relaxed">Ball to'plang, darajangizni oshiring va liderlar qatoridan joy oling.</p>
        </div>
      </div>
      
      {/* Task types */}
      <div className="bg-white rounded-2xl p-6 shadow-xl border border-gray-100">
        <div className="flex items-center gap-3 mb-6">
          <div className="w-10 h-10 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center">
            <Sparkles className="w-5 h-5 text-white" />
          </div>
          <h3 className="font-bold text-xl text-gray-800">Topshiriq turlari</h3>
        </div>
        
        <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
          {[
            { name: 'Fill in the blanks', ai: false },
            { name: 'Identify tense', ai: false },
            { name: 'Matching', ai: false },
            { name: 'Verb forms', ai: false },
            { name: 'Vocabulary', ai: false },
            { name: 'Crossword', ai: false },
            { name: 'Insert words', ai: false },
            { name: 'Translation', ai: true, icon: PenTool },
            { name: 'Synonyms', ai: true, icon: Sparkles },
            { name: 'Conversation', ai: true, icon: MessageSquare },
            { name: 'Speaking', ai: true, icon: Mic },
            { name: 'Writing', ai: true, icon: PenTool },
            { name: 'Video retelling', ai: true, icon: Video },
          ].map((type, i) => (
            <div 
              key={i} 
              className={`p-4 rounded-xl text-sm font-medium transition-all hover:scale-105 cursor-pointer ${
                type.ai 
                  ? 'bg-gradient-to-br from-purple-50 to-pink-50 text-purple-700 border-2 border-purple-200 shadow-lg shadow-purple-500/10' 
                  : 'bg-gray-50 text-gray-600 border border-gray-200 hover:bg-gray-100'
              }`}
            >
              <div className="flex items-center gap-2">
                {type.ai && type.icon && <type.icon className="w-4 h-4" />}
                <span>{type.name}</span>
              </div>
              {type.ai && (
                <span className="inline-flex items-center gap-1 mt-2 text-xs bg-gradient-to-r from-purple-500 to-pink-500 text-white px-2 py-0.5 rounded-full">
                  <Brain className="w-3 h-3" /> AI
                </span>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
