import { Calendar, ChevronRight, Bell } from 'lucide-react'

const news = [
  {
    id: 1,
    title: 'Platforma rasman ishga tushirildi!',
    date: '2025-01-15',
    excerpt: 'English for Medical Students platformasi barcha talabalar uchun ochiq.',
    featured: true
  },
  {
    id: 2,
    title: 'AI baholash tizimi qo\'shildi',
    date: '2025-06-20',
    excerpt: 'Endi speaking, writing va translation topshiriqlarni AI baholaydi.'
  },
  {
    id: 3,
    title: 'Yangi mavzular qo\'shildi',
    date: '2025-09-01',
    excerpt: '5 ta yangi mavzu va 65 ta yangi topshiriq qo\'shildi.'
  },
  {
    id: 4,
    title: 'Mobil versiya tayyorlanmoqda',
    date: '2025-12-15',
    excerpt: 'Tez orada Android va iOS ilovalari chiqariladi.'
  }
]

export default function News() {
  return (
    <div className="animate-fade-in">
      <div className="rounded-2xl p-6 shadow-xl shadow-orange-500/20 bg-gradient-to-r from-orange-500 to-red-600 text-white mb-6">
        <h1 className="text-2xl font-bold mb-2 flex items-center gap-2">
          <Bell className="w-6 h-6" />
          Yangiliklar va e'lonlar
        </h1>
        <p className="text-white/80">Platforma yangiliklari va muhim e'lonlar</p>
      </div>
      
      {/* Featured news */}
      {news.filter(n => n.featured).map(item => (
        <div key={item.id} className="card mb-6 border-l-4 border-l-orange-500 bg-orange-50">
          <span className="badge badge-yellow mb-2">Muhim</span>
          <h2 className="text-lg font-bold mb-2">{item.title}</h2>
          <p className="text-gray-600 text-sm mb-3">{item.excerpt}</p>
          <div className="flex items-center gap-2 text-xs text-gray-500">
            <Calendar className="w-4 h-4" />
            {new Date(item.date).toLocaleDateString('uz-UZ')}
          </div>
        </div>
      ))}
      
      {/* Other news */}
      <h3 className="font-semibold mb-3">Barcha yangiliklar</h3>
      <div className="space-y-3">
        {news.filter(n => !n.featured).map(item => (
          <div key={item.id} className="card flex items-center gap-4">
            <div className="w-12 h-12 rounded-xl bg-gray-100 flex items-center justify-center text-xl flex-shrink-0">
              📰
            </div>
            <div className="flex-1 min-w-0">
              <h3 className="font-medium truncate">{item.title}</h3>
              <div className="flex items-center gap-2 text-xs text-gray-500 mt-1">
                <Calendar className="w-3 h-3" />
                {new Date(item.date).toLocaleDateString('uz-UZ')}
              </div>
            </div>
            <ChevronRight className="w-5 h-5 text-gray-400 flex-shrink-0" />
          </div>
        ))}
      </div>
    </div>
  )
}
