import React, { useEffect, useState } from "react";
import axios from "axios";

const API_BASE = "https://square-subastas.onrender.com";

export default function App() {
  const [auctions, setAuctions] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [startingPrice, setStartingPrice] = useState("");

  const fetchAuctions = async () => {
    try {
      const res = await axios.get(`${API_BASE}/auctions/`);
      setAuctions(res.data);
    } catch (err) {
      console.error("Error fetching auctions", err);
    }
  };

  const createAuction = async () => {
    try {
      await axios.post(`${API_BASE}/auctions/`, {
        title,
        description,
        starting_price: parseFloat(startingPrice)
      });
      setTitle("");
      setDescription("");
      setStartingPrice("");
      fetchAuctions();
    } catch (err) {
      console.error("Error creating auction", err);
    }
  };

  const deleteAuction = async (id) => {
    try {
      await axios.delete(`${API_BASE}/auctions/${id}`);
      fetchAuctions();
    } catch (err) {
      console.error("Error deleting auction", err);
    }
  };

  useEffect(() => {
    fetchAuctions();
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1 style={{ fontSize: "24px", fontWeight: "bold" }}>📊 Panel Admin - Subastas</h1>

      <h2 style={{ marginTop: "20px" }}>➕ Crear nueva subasta</h2>
      <input placeholder="Título" value={title} onChange={(e) => setTitle(e.target.value)} />
      <input placeholder="Descripción" value={description} onChange={(e) => setDescription(e.target.value)} />
      <input placeholder="Precio inicial" type="number" value={startingPrice} onChange={(e) => setStartingPrice(e.target.value)} />
      <button onClick={createAuction}>Crear</button>

      <h2 style={{ marginTop: "20px" }}>📦 Lista de subastas</h2>
      <ul>
        {auctions.map((a) => (
          <li key={a.id}>
            <strong>{a.title}</strong> - {a.description} - 💰 {a.starting_price}
            <button onClick={() => deleteAuction(a.id)} style={{ marginLeft: "10px", color: "red" }}>Eliminar</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
