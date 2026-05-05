import { useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { Menu, X, BookOpen, User, LogOut } from 'lucide-react'
import { useAuthStore } from '../store'

export default function Navbar() {
  const [open, setOpen] = useState(false)
  const { user, isAuthenticated, logout } = useAuthStore()
  const location = useLocation()
  
  const links = [
    { to: '/', label: 'Bosh sahifa' },
    { to: '/units', label: 'Mavzular' },
    { to: '/vocabulary', label: 'Lug\'at' },
    { to: '/leaderboard', label: 'Reyting' },
  ]
  
  const isActive = (path) => location.pathname === path
  
  return (
    <nav className="bg-white border-b border-gray-200 sticky top-0 z-50">
      <div className="container">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center gap-2">
            <BookOpen className="w-6 h-6 text-primary-500" />
            <span className="font-semibold text-gray-900 hidden sm:block">Medical English</span>
          </Link>
          
          {/* Desktop menu */}
          <div className="hidden md:flex items-center gap-1">
            {links.map(link => (
              <Link
                key={link.to}
                to={link.to}
                className={`px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                  isActive(link.to)
                    ? 'bg-primary-50 text-primary-600'
                    : 'text-gray-600 hover:bg-gray-50'
                }`}
              >
                {link.label}
              </Link>
            ))}
          </div>
          
          {/* User section */}
          <div className="hidden md:flex items-center gap-3">
            {isAuthenticated ? (
              <>
                <div className="flex items-center gap-4 text-sm">
                  <span className="badge badge-yellow">🔥 {user?.streak || 0}</span>
                  <span className="badge badge-blue">⭐ {user?.points || 0}</span>
                </div>
                <Link to="/profile" className="flex items-center gap-2 text-sm text-gray-600 hover:text-gray-900">
                  <User className="w-5 h-5" />
                  {user?.username}
                </Link>
                <button onClick={logout} className="p-2 text-gray-400 hover:text-gray-600">
                  <LogOut className="w-5 h-5" />
                </button>
              </>
            ) : (
              <>
                <Link to="/login" className="btn btn-outline text-sm">Kirish</Link>
                <Link to="/register" className="btn btn-primary text-sm">Ro'yxatdan o'tish</Link>
              </>
            )}
          </div>
          
          {/* Mobile menu button */}
          <button onClick={() => setOpen(!open)} className="md:hidden p-2">
            {open ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>
        
        {/* Mobile menu */}
        {open && (
          <div className="md:hidden py-4 border-t">
            <div className="flex flex-col gap-1">
              {links.map(link => (
                <Link
                  key={link.to}
                  to={link.to}
                  onClick={() => setOpen(false)}
                  className={`px-3 py-2 rounded-lg text-sm font-medium ${
                    isActive(link.to)
                      ? 'bg-primary-50 text-primary-600'
                      : 'text-gray-600'
                  }`}
                >
                  {link.label}
                </Link>
              ))}
              
              {isAuthenticated ? (
                <>
                  <div className="flex gap-2 px-3 py-2">
                    <span className="badge badge-yellow">🔥 {user?.streak || 0}</span>
                    <span className="badge badge-blue">⭐ {user?.points || 0}</span>
                  </div>
                  <Link to="/profile" onClick={() => setOpen(false)} className="px-3 py-2 text-sm text-gray-600">
                    Profil
                  </Link>
                  <button onClick={() => { logout(); setOpen(false) }} className="px-3 py-2 text-sm text-red-600 text-left">
                    Chiqish
                  </button>
                </>
              ) : (
                <div className="flex gap-2 px-3 pt-2">
                  <Link to="/login" onClick={() => setOpen(false)} className="btn btn-outline text-sm flex-1">Kirish</Link>
                  <Link to="/register" onClick={() => setOpen(false)} className="btn btn-primary text-sm flex-1">Ro'yxatdan o'tish</Link>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </nav>
  )
}
