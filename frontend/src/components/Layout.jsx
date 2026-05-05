import { Outlet, useLocation } from 'react-router-dom'
import Header from './Header'
import Sidebar from './Sidebar'
import Footer from './Footer'
import Slider from './Slider'

export default function Layout() {
  const location = useLocation()
  
  // Pages that don't need sidebar
  const noSidebarPages = ['/login', '/register']
  const showSidebar = !noSidebarPages.includes(location.pathname)
  
  // Show slider only on home page
  const showSlider = location.pathname === '/'
  
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      
      {/* Full-width Slider - only on home page */}
      {showSlider && (
        <div className="shadow-2xl">
          <Slider />
        </div>
      )}
      
      {/* Spacer between header/slider and content */}
      <div className="h-10"></div>
      
      {/* Main content area */}
      <div className="flex-1 container mb-16">
        <div className="flex gap-8">
          {/* Sidebar - hidden on mobile and auth pages */}
          {showSidebar && (
            <div className="hidden lg:block">
              <Sidebar />
            </div>
          )}
          
          {/* Main content */}
          <main className={`flex-1 min-w-0 ${showSidebar ? '' : 'max-w-2xl mx-auto'}`}>
            <Outlet />
          </main>
        </div>
      </div>
      
      <Footer />
    </div>
  )
}
