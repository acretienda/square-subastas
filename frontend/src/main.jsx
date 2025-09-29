import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home'
import AdminPanel from './pages/AdminPanel'
import UserPanel from './pages/UserPanel'

function App() {
  return (
    <BrowserRouter>
      <nav style={{display: 'flex', gap: '1rem', marginBottom: '1rem'}}>
        <Link to="/">Inicio</Link>
        <Link to="/admin">Admin</Link>
        <Link to="/user">Usuario</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/admin" element={<AdminPanel />} />
        <Route path="/user" element={<UserPanel />} />
      </Routes>
    </BrowserRouter>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />)
