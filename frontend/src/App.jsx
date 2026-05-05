import { useEffect } from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import { useAuthStore } from './store'

import Layout from './components/Layout'
import Home from './pages/Home'
import Login from './pages/Login'
import Register from './pages/Register'
import Units from './pages/Units'
import UnitDetail from './pages/UnitDetail'
import TaskPage from './pages/TaskPage'
import Vocabulary from './pages/Vocabulary'
import Leaderboard from './pages/Leaderboard'
import Profile from './pages/Profile'
import About from './pages/About'
import Author from './pages/Author'
import Contact from './pages/Contact'
import News from './pages/News'

function ProtectedRoute({ children }) {
  const { isAuthenticated } = useAuthStore()
  return isAuthenticated ? children : <Navigate to="/login" />
}

export default function App() {
  const { initAuth } = useAuthStore()
  
  useEffect(() => {
    initAuth()
  }, [])
  
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="login" element={<Login />} />
        <Route path="register" element={<Register />} />
        <Route path="units" element={<Units />} />
        <Route path="units/:id" element={<UnitDetail />} />
        <Route path="task/:id" element={<ProtectedRoute><TaskPage /></ProtectedRoute>} />
        <Route path="vocabulary" element={<Vocabulary />} />
        <Route path="leaderboard" element={<Leaderboard />} />
        <Route path="profile" element={<ProtectedRoute><Profile /></ProtectedRoute>} />
        <Route path="about" element={<About />} />
        <Route path="author" element={<Author />} />
        <Route path="contact" element={<Contact />} />
        <Route path="news" element={<News />} />
        
        {/* Placeholder routes - redirect to home */}
        <Route path="independent" element={<About />} />
        <Route path="idioms" element={<Vocabulary />} />
        <Route path="phrasal-verbs" element={<Vocabulary />} />
        <Route path="test" element={<Units />} />
        <Route path="exam" element={<Units />} />
      </Route>
    </Routes>
  )
}
