
import React, { useEffect, useState } from "react";

const API_URL = import.meta.env.VITE_API_URL;

export default function App() {
  const [auctions, setAuctions] = useState([]);

  useEffect(() => {
    fetch(`${API_URL}/auctions/`)
      .then(res => res.json())
      .then(data => setAuctions(data))
      .catch(err => console.error("Error cargando subastas:", err));
  }, []);

  const handleBid = (auctionId) => {
    console.log("💸 Pujando en subasta:", auctionId);
    alert("Puja enviada (simulada) 💸");
  };

  return (
    <div className="max-w-4xl mx-auto py-10 px-4">
      <h1 className="text-3xl font-bold mb-6 text-center text-blue-700">
        🏷️ Subastas en Vivo
      </h1>
      {auctions.length === 0 ? (
        <p className="text-gray-500 text-center">No hay subastas disponibles.</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {auctions.map((a) => (
            <div key={a.id} className="bg-white shadow-md rounded-2xl p-6">
              <h2 className="text-xl font-semibold text-gray-800">{a.title}</h2>
              <p className="text-gray-600">Precio inicial: {a.starting_price}€</p>
              <p className="text-gray-600">Estado: {a.active ? "Activa ✅" : "Cerrada ❌"}</p>
              <button
                onClick={() => handleBid(a.id)}
                className="mt-4 w-full bg-blue-600 text-white py-2 rounded-xl hover:bg-blue-700"
              >
                Pujar
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
