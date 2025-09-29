import React, { useState, useEffect } from 'react'
import axios from 'axios'

export default function UserPanel() {
  const [auctions, setAuctions] = useState([])
  const API_URL = import.meta.env.VITE_API_BASE_URL

  useEffect(() => {
    axios.get(`${API_URL}/auctions/`)
      .then(res => setAuctions(res.data.auctions))
      .catch(() => setAuctions([]))
  }, [])

  return (
    <div>
      <h2>Panel de Usuario</h2>
      <ul>
        {auctions.map((a, i) => (
          <li key={i}>{a.title || 'Subasta sin título'}</li>
        ))}
      </ul>
    </div>
  )
}
