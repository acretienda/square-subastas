import { useEffect, useState } from 'react'

function App() {
  const [auctions, setAuctions] = useState([])

  useEffect(() => {
    fetch(import.meta.env.VITE_API_URL + "/auctions/")
      .then(res => res.json())
      .then(data => setAuctions(data))
      .catch(err => console.error("Error cargando subastas:", err))
  }, [])

  return (
    <div style={{ fontFamily: 'sans-serif', padding: '2rem' }}>
      <h1>🎉 Subastas Online</h1>
      <h2>Listado de subastas</h2>
      {auctions.length === 0 ? (
        <p>No hay subastas disponibles</p>
      ) : (
        <ul>
          {auctions.map(a => (
            <li key={a.id}>
              <strong>{a.title}</strong> - Precio inicial: {a.starting_price}
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

export default App
