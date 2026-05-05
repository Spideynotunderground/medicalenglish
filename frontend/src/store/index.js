import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import api from '../services/api'

export const useAuthStore = create(
  persist(
    (set, get) => ({
      user: null,
      token: null,
      isAuthenticated: false,
      
      login: async (username, password) => {
        const res = await api.post('/auth/login/', { username, password })
        const { access, refresh } = res.data
        localStorage.setItem('refresh_token', refresh)
        api.defaults.headers.common['Authorization'] = `Bearer ${access}`
        
        const userRes = await api.get('/profile/')
        set({ user: userRes.data, token: access, isAuthenticated: true })
        return userRes.data
      },
      
      register: async (data) => {
        await api.post('/auth/register/', data)
      },
      
      logout: () => {
        localStorage.removeItem('refresh_token')
        delete api.defaults.headers.common['Authorization']
        set({ user: null, token: null, isAuthenticated: false })
      },
      
      updateUser: (data) => set({ user: { ...get().user, ...data } }),
      
      fetchUser: async () => {
        try {
          const res = await api.get('/profile/')
          set({ user: res.data })
        } catch (e) {
          get().logout()
        }
      },
      
      initAuth: () => {
        const token = get().token
        if (token) {
          api.defaults.headers.common['Authorization'] = `Bearer ${token}`
          get().fetchUser()
        }
      }
    }),
    { name: 'auth-storage', partialize: (state) => ({ token: state.token }) }
  )
)
