import { Link, useLocation } from 'react-router-dom'
import { Menu, X, LogIn, User, LogOut, Flame, Star } from 'lucide-react'
import { useState } from 'react'
import { useAuthStore } from '../store'

export default function Header() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const { user, isAuthenticated, logout } = useAuthStore()
  const location = useLocation()
  
  const isActive = (path) => location.pathname === path
  
  const navLinks = [
    { to: '/', label: 'Bosh sahifa' },
    { to: '/about', label: 'Platforma haqida' },
    { to: '/units', label: 'Mavzular' },
    { to: '/leaderboard', label: 'Foydalanuvchilar' },
    { to: '/news', label: "Yangiliklar" },
    { to: '/author', label: 'Muallif haqida' },
    { to: '/contact', label: "Bog'lanish" },
  ]
  
  return (
    <header className="bg-gradient-to-r from-indigo-900 via-purple-900 to-indigo-900">
      {/* Row 1: Social icons */}
      <div className="border-b border-white/10">
        <div className="container flex items-center justify-end py-2.5 gap-2">
          <a href="#" className="w-9 h-9 bg-gradient-to-br from-blue-400 to-blue-600 hover:scale-110 rounded-lg flex items-center justify-center transition-all shadow-lg shadow-blue-500/30">
            <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.562 8.161c-.18 1.897-.962 6.502-1.359 8.627-.168.9-.5 1.201-.82 1.23-.697.064-1.226-.461-1.901-.903-1.056-.692-1.653-1.123-2.678-1.799-1.185-.781-.417-1.21.258-1.911.177-.184 3.247-2.977 3.307-3.23.007-.032.015-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.139-5.062 3.345-.479.329-.913.489-1.302.481-.428-.009-1.252-.242-1.865-.442-.751-.244-1.349-.374-1.297-.789.027-.216.324-.437.893-.663 3.498-1.524 5.831-2.529 6.998-3.015 3.333-1.386 4.025-1.627 4.477-1.635.099-.002.321.023.465.141.121.099.154.232.17.324.015.092.034.303.019.468z"/></svg>
          </a>
          <a href="#" className="w-9 h-9 bg-gradient-to-br from-blue-500 to-blue-700 hover:scale-110 rounded-lg flex items-center justify-center transition-all shadow-lg shadow-blue-500/30">
            <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
          </a>
          <a href="#" className="w-9 h-9 bg-gradient-to-br from-pink-500 via-red-500 to-yellow-500 hover:scale-110 rounded-lg flex items-center justify-center transition-all shadow-lg shadow-pink-500/30">
            <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          </a>
          <a href="#" className="w-9 h-9 bg-gradient-to-br from-blue-600 to-blue-800 hover:scale-110 rounded-lg flex items-center justify-center transition-all shadow-lg shadow-blue-500/30">
            <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
          </a>
        </div>
      </div>
      
      {/* Row 2: Logo + Title + Login (3 columns) */}
      <div className="border-b border-white/10">
        <div className="container py-6">
          <div className="grid grid-cols-3 items-center">
            {/* Col 1: Logo */}
            <div className="justify-self-start">
              <Link to="/" className="block group">
                <div className="w-20 h-20 bg-gradient-to-br from-amber-400 via-orange-500 to-red-500 rounded-2xl flex items-center justify-center shadow-2xl shadow-orange-500/40 group-hover:scale-105 transition-transform relative overflow-hidden">
                  <div className="absolute inset-0 bg-white/20 rounded-2xl"></div>
                  <svg className="w-12 h-12 text-white relative z-10" fill="none" stroke="currentColor" strokeWidth={2} viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                  </svg>
                  <div className="absolute -top-1 -right-1 w-7 h-7 bg-gradient-to-br from-green-400 to-emerald-600 rounded-full flex items-center justify-center shadow-lg border-2 border-white">
                    <span className="text-white text-sm font-bold">+</span>
                  </div>
                </div>
              </Link>
            </div>
            
            {/* Col 2: Title */}
            <div className="text-center">
              <h1 className="text-3xl md:text-4xl font-black tracking-wide bg-gradient-to-r from-white via-blue-100 to-white bg-clip-text text-transparent drop-shadow-lg">
                ENGLISH FOR
              </h1>
              <h1 className="text-3xl md:text-4xl font-black tracking-wide bg-gradient-to-r from-white via-blue-100 to-white bg-clip-text text-transparent drop-shadow-lg">
                MEDICAL STUDENTS
              </h1>
              <h2 className="text-xl md:text-2xl font-bold tracking-widest bg-gradient-to-r from-amber-400 via-orange-400 to-yellow-400 bg-clip-text text-transparent mt-1">
                PLATFORMASI
              </h2>
            </div>
            
            {/* Col 3: Login */}
            <div className="justify-self-end">
              {isAuthenticated ? (
                <div className="flex items-center gap-3">
                  <div className="hidden sm:flex items-center gap-1 bg-gradient-to-r from-orange-500 to-red-500 px-3 py-1.5 rounded-full shadow-lg">
                    <Flame className="w-4 h-4 text-white" />
                    <span className="text-white text-sm font-bold">{user?.streak || 0}</span>
                  </div>
                  <div className="hidden sm:flex items-center gap-1 bg-gradient-to-r from-yellow-400 to-amber-500 px-3 py-1.5 rounded-full shadow-lg">
                    <Star className="w-4 h-4 text-white" />
                    <span className="text-white text-sm font-bold">{user?.points || 0}</span>
                  </div>
                  <Link to="/profile" className="flex items-center gap-2 text-white hover:text-amber-300 transition-colors">
                    <div className="w-10 h-10 bg-gradient-to-br from-purple-500 to-pink-500 rounded-full flex items-center justify-center">
                      <User className="w-5 h-5 text-white" />
                    </div>
                  </Link>
                  <button onClick={logout} className="text-white/60 hover:text-white transition-colors">
                    <LogOut className="w-5 h-5" />
                  </button>
                </div>
              ) : (
                <Link to="/login" className="group flex items-center gap-2 bg-gradient-to-r from-amber-400 via-orange-500 to-red-500 hover:from-amber-500 hover:via-orange-600 hover:to-red-600 text-white font-semibold px-6 py-3 rounded-xl shadow-lg shadow-orange-500/30 transition-all hover:scale-105">
                  <LogIn className="w-5 h-5" />
                  <span>Tizimga kirish</span>
                </Link>
              )}
            </div>
          </div>
        </div>
      </div>
      
      {/* Row 3: Navigation */}
      <nav className="bg-white/5 backdrop-blur-sm">
        <div className="container">
          {/* Mobile menu button */}
          <div className="lg:hidden flex justify-center py-3">
            <button onClick={() => setMobileMenuOpen(!mobileMenuOpen)} className="p-2 text-white">
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
          
          {/* Navigation links */}
          <ul className={`${mobileMenuOpen ? 'flex' : 'hidden'} lg:flex flex-col lg:flex-row lg:items-center lg:justify-center py-2 gap-1`}>
            {navLinks.map((link, index) => (
              <li key={link.to} className="flex items-center">
                <Link
                  to={link.to}
                  onClick={() => setMobileMenuOpen(false)}
                  className={`block px-5 py-2.5 text-sm font-medium rounded-lg transition-all ${
                    isActive(link.to)
                      ? 'bg-gradient-to-r from-amber-400 to-orange-500 text-white shadow-lg'
                      : 'text-white/80 hover:text-white hover:bg-white/10'
                  }`}
                >
                  {link.label}
                </Link>
                {index < navLinks.length - 1 && (
                  <span className="hidden lg:block text-white/20 mx-1">•</span>
                )}
              </li>
            ))}
          </ul>
        </div>
      </nav>
    </header>
  )
}
