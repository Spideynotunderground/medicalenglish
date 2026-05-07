import { useState, useEffect } from 'react'
import { User, Award, Zap, Flame, CheckCircle } from 'lucide-react'
import { useAuthStore } from '../store'
import api from '../services/api'
import toast from 'react-hot-toast'

export default function Profile() {
  const { user, updateUser } = useAuthStore()
  const [form, setForm] = useState({
    first_name: '',
    last_name: '',
    email: ''
  })
  const [saving, setSaving] = useState(false)
  const [stats, setStats] = useState(null)
  
  useEffect(() => {
    if (user) {
      setForm({
        first_name: user.first_name || '',
        last_name: user.last_name || '',
        email: user.email || ''
      })
    }
    
    api.get('/dashboard/').then(res => {
      setStats(res.data.stats)
    })
  }, [user])
  
  const handleSave = async () => {
    setSaving(true)
    try {
      const res = await api.patch('/profile/', form)
      updateUser(res.data)
      toast.success('Saqlandi!')
    } catch (err) {
      toast.error('Xatolik yuz berdi')
    } finally {
      setSaving(false)
    }
  }
  
  if (!user) return null
  
  const levelProgress = (user.points % 500) / 500 * 100
  
  return (
    <div className="max-w-2xl mx-auto animate-fade-in">
      {/* Profile header */}
      <div className="card-colored bg-gradient-to-r from-blue-500 to-purple-600 text-white mb-6">
        <div className="flex items-center gap-4">
          <div className="w-20 h-20 rounded-2xl bg-white/20 flex items-center justify-center text-3xl font-bold">
            {user.first_name?.[0] || user.username[0].toUpperCase()}
          </div>
          <div>
            <h1 className="text-2xl font-bold">{user.first_name || user.username}</h1>
            <p className="text-white/80">@{user.username}</p>
            <div className="flex items-center gap-4 mt-2 text-sm">
              <span className="flex items-center gap-1">
                <Award className="w-4 h-4" /> Level {user.level}
              </span>
              <span className="flex items-center gap-1">
                <Zap className="w-4 h-4" /> {user.points} ball
              </span>
              <span className="flex items-center gap-1">
                <Flame className="w-4 h-4" /> {user.streak} kun streak
              </span>
            </div>
          </div>
        </div>
        
        {/* Level progress */}
        <div className="mt-4 pt-4 border-t border-white/20">
          <div className="flex justify-between text-sm mb-1">
            <span>Level {user.level}</span>
            <span>Level {user.level + 1}</span>
          </div>
          <div className="h-2 bg-white/20 rounded-full overflow-hidden">
            <div className="h-full bg-white rounded-full" style={{ width: `${levelProgress}%` }} />
          </div>
          <p className="text-xs text-white/60 mt-1">
            Keyingi levelga {500 - (user.points % 500)} ball qoldi
          </p>
        </div>
      </div>
      
      {/* Stats */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">
        <div className="card text-center">
          <Award className="w-6 h-6 text-yellow-500 mx-auto mb-1" />
          <div className="text-2xl font-bold stat-number">{user.level}</div>
          <div className="text-xs text-gray-500">Daraja</div>
        </div>
        <div className="card text-center">
          <Zap className="w-6 h-6 text-blue-500 mx-auto mb-1" />
          <div className="text-2xl font-bold stat-number">{user.points}</div>
          <div className="text-xs text-gray-500">Ball</div>
        </div>
        <div className="card text-center">
          <Flame className="w-6 h-6 text-orange-500 mx-auto mb-1" />
          <div className="text-2xl font-bold stat-number">{user.streak}</div>
          <div className="text-xs text-gray-500">Streak</div>
        </div>
        <div className="card text-center">
          <CheckCircle className="w-6 h-6 text-green-500 mx-auto mb-1" />
          <div className="text-2xl font-bold stat-number">{stats?.completed_tasks || 0}</div>
          <div className="text-xs text-gray-500">Bajarilgan</div>
        </div>
      </div>
      
      {/* Progress */}
      {stats && (
        <div className="card mb-6">
          <h3 className="font-semibold mb-3">Umumiy progress</h3>
          <div className="flex justify-between text-sm mb-2">
            <span>{stats.completed_tasks} / {stats.total_tasks} topshiriq</span>
            <span className="font-medium text-blue-600">{stats.progress_percent}%</span>
          </div>
          <div className="progress-bar">
            <div className="progress-fill" style={{ width: `${stats.progress_percent}%` }} />
          </div>
        </div>
      )}
      
      {/* Edit form */}
      <div className="card">
        <h3 className="font-semibold mb-4 flex items-center gap-2">
          <User className="w-5 h-5" />
          Ma'lumotlarni tahrirlash
        </h3>
        
        <div className="space-y-4">
          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Ism</label>
              <input
                type="text"
                value={form.first_name}
                onChange={(e) => setForm({ ...form, first_name: e.target.value })}
                className="input"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Familiya</label>
              <input
                type="text"
                value={form.last_name}
                onChange={(e) => setForm({ ...form, last_name: e.target.value })}
                className="input"
              />
            </div>
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
            <input
              type="email"
              value={form.email}
              onChange={(e) => setForm({ ...form, email: e.target.value })}
              className="input"
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Login</label>
            <input
              type="text"
              value={user.username}
              className="input bg-gray-50 cursor-not-allowed"
              disabled
            />
          </div>
          
          <button onClick={handleSave} disabled={saving} className="btn btn-primary">
            {saving ? 'Saqlanmoqda...' : 'Saqlash'}
          </button>
        </div>
      </div>
    </div>
  )
}
