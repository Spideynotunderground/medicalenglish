import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { ChevronLeft, ChevronRight, ArrowRight, Sparkles, Brain, Trophy } from 'lucide-react'

const slides = [
  {
    title: 'Tibbiyot ingliz tilini o\'rganing',
    subtitle: '15 ta mavzu, 195 ta topshiriq bilan to\'liq kurs',
    bg: 'from-violet-600 via-purple-600 to-indigo-700',
    icon: Sparkles,
    accent: 'from-pink-500 to-rose-500'
  },
  {
    title: 'AI bilan baholash',
    subtitle: 'Sun\'iy intellekt yordamida javoblaringiz baholanadi',
    bg: 'from-cyan-500 via-blue-600 to-indigo-700',
    icon: Brain,
    accent: 'from-cyan-400 to-blue-500'
  },
  {
    title: 'Reytingda o\'z o\'rningizni toping',
    subtitle: 'Ball yig\'ing va liderlar qatoridan joy oling',
    bg: 'from-amber-500 via-orange-600 to-red-600',
    icon: Trophy,
    accent: 'from-yellow-400 to-amber-500'
  }
]

export default function Slider() {
  const [currentSlide, setCurrentSlide] = useState(0)
  
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentSlide(prev => (prev + 1) % slides.length)
    }, 5000)
    return () => clearInterval(timer)
  }, [])
  
  const prevSlide = () => setCurrentSlide(prev => (prev - 1 + slides.length) % slides.length)
  const nextSlide = () => setCurrentSlide(prev => (prev + 1) % slides.length)
  
  const CurrentIcon = slides[currentSlide].icon
  
  return (
    <div className="relative w-full overflow-hidden">
      {/* Background with animated gradient */}
      <div className={`bg-gradient-to-r ${slides[currentSlide].bg} transition-all duration-700`}>
        {/* Decorative elements */}
        <div className="absolute inset-0 overflow-hidden">
          <div className="absolute -top-40 -right-40 w-80 h-80 bg-white/10 rounded-full blur-3xl"></div>
          <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-white/10 rounded-full blur-3xl"></div>
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-white/5 rounded-full blur-3xl"></div>
        </div>
        
        <div className="container relative py-16 md:py-20">
          <div className="flex items-center justify-between gap-8">
            <div className="flex-1 text-white max-w-2xl">
              <h2 className="text-3xl md:text-5xl font-black mb-4 leading-tight drop-shadow-lg">
                {slides[currentSlide].title}
              </h2>
              <p className="text-lg md:text-xl text-white/90 mb-8">
                {slides[currentSlide].subtitle}
              </p>
              <Link 
                to="/units" 
                className={`inline-flex items-center gap-3 bg-gradient-to-r ${slides[currentSlide].accent} text-white font-bold px-8 py-4 rounded-2xl shadow-2xl hover:scale-105 transition-all group`}
              >
                <span className="text-lg">Boshlash</span>
                <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </Link>
            </div>
            
            {/* Icon display */}
            <div className="hidden md:flex items-center justify-center">
              <div className="relative">
                <div className="w-48 h-48 bg-white/10 backdrop-blur-sm rounded-3xl flex items-center justify-center border border-white/20 shadow-2xl">
                  <CurrentIcon className="w-24 h-24 text-white/80" />
                </div>
                <div className="absolute -inset-4 bg-gradient-to-r from-white/20 to-transparent rounded-3xl blur-xl -z-10"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      {/* Controls */}
      <button 
        onClick={prevSlide} 
        className="absolute left-4 md:left-8 top-1/2 -translate-y-1/2 w-12 h-12 bg-white/20 hover:bg-white/30 backdrop-blur-sm rounded-full flex items-center justify-center text-white transition-all hover:scale-110 border border-white/20"
      >
        <ChevronLeft className="w-6 h-6" />
      </button>
      <button 
        onClick={nextSlide} 
        className="absolute right-4 md:right-8 top-1/2 -translate-y-1/2 w-12 h-12 bg-white/20 hover:bg-white/30 backdrop-blur-sm rounded-full flex items-center justify-center text-white transition-all hover:scale-110 border border-white/20"
      >
        <ChevronRight className="w-6 h-6" />
      </button>
      
      {/* Dots */}
      <div className="absolute bottom-6 left-1/2 -translate-x-1/2 flex gap-3">
        {slides.map((_, i) => (
          <button
            key={i}
            onClick={() => setCurrentSlide(i)}
            className={`h-3 rounded-full transition-all duration-300 ${
              i === currentSlide 
                ? 'w-10 bg-white shadow-lg' 
                : 'w-3 bg-white/40 hover:bg-white/60'
            }`}
          />
        ))}
      </div>
    </div>
  )
}
