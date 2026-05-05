import { Users, Globe, Scale, Building, Heart } from 'lucide-react'

export default function Footer() {
  return (
    <footer className="bg-gradient-to-br from-gray-900 via-indigo-950 to-gray-900 text-white mt-10">
      {/* Stats bar */}
      <div className="bg-gradient-to-r from-indigo-600 via-purple-600 to-indigo-600 py-5">
        <div className="container flex flex-wrap items-center justify-center gap-8 text-sm">
          <div className="flex items-center gap-3 bg-white/10 backdrop-blur-sm px-5 py-2.5 rounded-full">
            <Users className="w-5 h-5 text-amber-400" />
            <span>Foydalanuvchilar: <strong className="text-amber-400">1,247</strong> ta</span>
          </div>
          <div className="flex items-center gap-3 bg-white/10 backdrop-blur-sm px-5 py-2.5 rounded-full">
            <span className="relative flex h-3 w-3">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span>
            </span>
            <span>Online: <strong className="text-green-400">89</strong> ta</span>
          </div>
        </div>
      </div>
      
      {/* Main footer - with more top padding */}
      <div className="container pt-20 pb-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-12 p-5">
          {/* Logo & description */}
          <div>
            <div className="flex items-center gap-4 mb-6">
              <div className="w-14 h-14 bg-gradient-to-br from-amber-400 to-orange-500 rounded-xl flex items-center justify-center shadow-lg">
                <svg className="w-8 h-8 text-white" fill="none" stroke="currentColor" strokeWidth={2} viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                </svg>
              </div>
              <span className="font-bold text-xl">Medical English</span>
            </div>
            <p className="text-gray-400 text-sm leading-relaxed">
              Tibbiyot talabalari uchun ingliz tili o'rganish platformasi. Zamonaviy va interaktiv ta'lim usullari.
            </p>
          </div>
          
          {/* Hamkorlar */}
          <div>
            <h4 className="font-semibold mb-6 flex items-center gap-3 text-lg">
              <div className="w-9 h-9 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center">
                <Building className="w-5 h-5 text-white" />
              </div>
              Hamkorlar
            </h4>
            <ul className="space-y-4 text-sm text-gray-400">
              <li className="hover:text-white transition-colors cursor-pointer">Buxoro davlat tibbiyot instituti</li>
              <li className="hover:text-white transition-colors cursor-pointer">Buxoro davlat universiteti</li>
              <li className="hover:text-white transition-colors cursor-pointer">Samarqand davlat tibbiyot universiteti</li>
            </ul>
          </div>
          
          {/* Boshqa manbalar */}
          <div>
            <h4 className="font-semibold mb-6 flex items-center gap-3 text-lg">
              <div className="w-9 h-9 bg-gradient-to-br from-purple-500 to-pink-600 rounded-lg flex items-center justify-center">
                <Globe className="w-5 h-5 text-white" />
              </div>
              Foydali havolalar
            </h4>
            <ul className="space-y-4 text-sm text-gray-400">
              <li><a href="#" className="hover:text-purple-400 transition-colors">HEMIS tizimi</a></li>
              <li><a href="#" className="hover:text-purple-400 transition-colors">Edu.uz</a></li>
              <li><a href="#" className="hover:text-purple-400 transition-colors">Ziyo.uz</a></li>
            </ul>
          </div>
          
          {/* Qonunchilik */}
          <div>
            <h4 className="font-semibold mb-6 flex items-center gap-3 text-lg">
              <div className="w-9 h-9 bg-gradient-to-br from-emerald-500 to-teal-600 rounded-lg flex items-center justify-center">
                <Scale className="w-5 h-5 text-white" />
              </div>
              Huquqiy hujjatlar
            </h4>
            <ul className="space-y-4 text-sm text-gray-400">
              <li><a href="#" className="hover:text-emerald-400 transition-colors">Foydalanish shartlari</a></li>
              <li><a href="#" className="hover:text-emerald-400 transition-colors">Maxfiylik siyosati</a></li>
              <li><a href="#" className="hover:text-emerald-400 transition-colors">Mualliflik huquqi</a></li>
            </ul>
          </div>
        </div>
      </div>
      
      {/* Copyright */}
      <div className="border-t border-white/10 py-6">
        <div className="container flex flex-col md:flex-row items-center justify-between gap-4 text-sm text-gray-500">
          <p>© 2025 English for Medical Students. Barcha huquqlar himoyalangan.</p>
          <p className="flex items-center gap-2">
            Made with <Heart className="w-4 h-4 text-red-500 fill-red-500" /> in Uzbekistan
          </p>
        </div>
      </div>
    </footer>
  )
}
