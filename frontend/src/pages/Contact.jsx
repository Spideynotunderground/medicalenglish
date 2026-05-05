import { useState } from 'react'
import { Mail, Phone, MapPin, Send, CheckCircle } from 'lucide-react'
import toast from 'react-hot-toast'

export default function Contact() {
  const [form, setForm] = useState({ name: '', email: '', message: '' })
  const [sent, setSent] = useState(false)
  const [loading, setLoading] = useState(false)
  
  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    
    // Simulate sending
    await new Promise(r => setTimeout(r, 1000))
    
    setSent(true)
    setLoading(false)
    toast.success('Xabar yuborildi!')
  }
  
  if (sent) {
    return (
      <div className="animate-fade-in">
        <div className="card text-center py-12">
          <div className="w-20 h-20 mx-auto bg-green-100 rounded-full flex items-center justify-center mb-4">
            <CheckCircle className="w-10 h-10 text-green-500" />
          </div>
          <h2 className="text-xl font-bold mb-2">Xabar yuborildi!</h2>
          <p className="text-gray-600 mb-4">Tez orada siz bilan bog'lanamiz.</p>
          <button onClick={() => setSent(false)} className="btn btn-primary">
            Yana xabar yuborish
          </button>
        </div>
      </div>
    )
  }
  
  return (
    <div className="animate-fade-in">
      <div className="card bg-gradient-to-r from-green-500 to-teal-600 text-white mb-6">
        <h1 className="text-2xl font-bold mb-2">Bog'lanish</h1>
        <p className="text-white/80">Savollaringiz bo'lsa, biz bilan bog'laning</p>
      </div>
      
      <div className="grid md:grid-cols-3 gap-4 mb-6">
        <div className="card text-center">
          <div className="w-12 h-12 mx-auto bg-blue-100 rounded-xl flex items-center justify-center mb-3">
            <Mail className="w-6 h-6 text-blue-600" />
          </div>
          <h3 className="font-semibold mb-1">Email</h3>
          <a href="mailto:info@efms.uz" className="text-sm text-blue-600">info@efms.uz</a>
        </div>
        
        <div className="card text-center">
          <div className="w-12 h-12 mx-auto bg-green-100 rounded-xl flex items-center justify-center mb-3">
            <Phone className="w-6 h-6 text-green-600" />
          </div>
          <h3 className="font-semibold mb-1">Telefon</h3>
          <a href="tel:+998901234567" className="text-sm text-green-600">+998 90 123 45 67</a>
        </div>
        
        <div className="card text-center">
          <div className="w-12 h-12 mx-auto bg-orange-100 rounded-xl flex items-center justify-center mb-3">
            <MapPin className="w-6 h-6 text-orange-600" />
          </div>
          <h3 className="font-semibold mb-1">Manzil</h3>
          <p className="text-sm text-gray-600">Buxoro shahri</p>
        </div>
      </div>
      
      <div className="card">
        <h3 className="font-semibold mb-4">Xabar yuborish</h3>
        
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="grid md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Ismingiz</label>
              <input
                type="text"
                value={form.name}
                onChange={(e) => setForm({ ...form, name: e.target.value })}
                className="input"
                placeholder="Ismingiz"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
              <input
                type="email"
                value={form.email}
                onChange={(e) => setForm({ ...form, email: e.target.value })}
                className="input"
                placeholder="email@example.com"
                required
              />
            </div>
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Xabar</label>
            <textarea
              value={form.message}
              onChange={(e) => setForm({ ...form, message: e.target.value })}
              className="input min-h-[120px]"
              placeholder="Xabaringizni yozing..."
              required
            />
          </div>
          
          <button type="submit" disabled={loading} className="btn btn-primary">
            {loading ? (
              <>
                <div className="animate-spin w-4 h-4 border-2 border-white border-t-transparent rounded-full"></div>
                Yuborilmoqda...
              </>
            ) : (
              <>
                <Send className="w-4 h-4" />
                Yuborish
              </>
            )}
          </button>
        </form>
      </div>
    </div>
  )
}
