import { GraduationCap, BookOpen, Award, Mail } from 'lucide-react'

export default function Author() {
  return (
    <div className="animate-fade-in">
      <div className="card-colored bg-gradient-to-r from-purple-500 to-pink-600 text-white mb-6">
        <h1 className="text-2xl font-bold mb-2">Muallif haqida</h1>
        <p className="text-white/80">Platforma muallifi va ilmiy rahbar</p>
      </div>
      
      <div className="card mb-6">
        <div className="flex flex-col md:flex-row items-center md:items-start gap-6">
          <div className="w-32 h-32 rounded-2xl bg-gradient-to-br from-purple-100 to-pink-100 flex items-center justify-center">
            <GraduationCap className="w-16 h-16 text-purple-500" />
          </div>
          <div className="text-center md:text-left">
            <h2 className="text-xl font-bold mb-1">S.Dj. Mukhamedjanova</h2>
            <p className="text-gray-600 mb-3">Buxoro davlat tibbiyot instituti o'qituvchisi</p>
            <div className="flex flex-wrap gap-2 justify-center md:justify-start">
              <span className="badge badge-purple">PhD</span>
              <span className="badge badge-blue">English Teacher</span>
              <span className="badge badge-green">Researcher</span>
            </div>
          </div>
        </div>
      </div>
      
      <div className="grid md:grid-cols-2 gap-4 mb-6">
        <div className="card">
          <h3 className="font-semibold mb-3 flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-blue-500" />
            Ilmiy faoliyat
          </h3>
          <ul className="space-y-2 text-sm text-gray-600">
            <li>• Tibbiy ingliz tili metodikasi bo'yicha tadqiqotlar</li>
            <li>• 10+ ilmiy maqola va tezislar</li>
            <li>• Xalqaro konferensiyalarda ishtirok</li>
            <li>• "English for Medical Students" o'quv qo'llanma muallifi</li>
          </ul>
        </div>
        
        <div className="card">
          <h3 className="font-semibold mb-3 flex items-center gap-2">
            <Award className="w-5 h-5 text-yellow-500" />
            Yutuqlar
          </h3>
          <ul className="space-y-2 text-sm text-gray-600">
            <li>• IELTS sertifikati (C1)</li>
            <li>• "Yilning eng yaxshi o'qituvchisi" mukofoti</li>
            <li>• Innovatsion ta'lim texnologiyalari bo'yicha grant</li>
          </ul>
        </div>
      </div>
      
      <div className="card">
        <h3 className="font-semibold mb-4">Tasdiqlash</h3>
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
          <p className="text-sm text-gray-700">
            Ushbu platforma <strong>Buxoro davlat tibbiyot instituti</strong> Ilmiy kengashi 
            tomonidan tasdiqlangan.
          </p>
          <p className="text-sm text-gray-500 mt-2">
            Bayonnoma № 11, 30.03.2025
          </p>
        </div>
        
        <div className="mt-4 flex items-center gap-4">
          <Mail className="w-5 h-5 text-gray-400" />
          <a href="mailto:info@efms.uz" className="text-blue-600 hover:underline">
            info@efms.uz
          </a>
        </div>
      </div>
    </div>
  )
}
