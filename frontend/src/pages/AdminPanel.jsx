import React, { useState } from 'react'
import axios from 'axios'

export default function AdminPanel() {
  const [title, setTitle] = useState('')
  const [message, setMessage] = useState('')
  const API_URL = import.meta.env.VITE_API_BASE_URL

  const createAuction = async () => {
    try {
      const res = await axios.post(`${API_URL}/auctions/`, { title })
      setMessage(res.data.message)
    } catch (err) {
      setMessage('Error creando subasta')
    }
  }

  return (
    <div>
      <h2>Panel de Admin</h2>
      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Título de la subasta"
      />
      <button onClick={createAuction}>Crear Subasta</button>
      <p>{message}</p>
    </div>
  )
}
