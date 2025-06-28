import React, { useEffect, useState, useCallback } from "react";
import GameBoard from "./components/GameBoard";
import Instructions from "./components/Instructions";
import StatusMessage from "./components/StatusMessage";
import "./style/App.css";

const API_URL = process.env.REACT_APP_MODEL_2048_API_URL ||"https://two048-game-backend-6fz6.onrender.com";

const KEY_TO_DIRECTION = {
  ArrowUp: "up",
  ArrowDown: "down",
  ArrowLeft: "left",
  ArrowRight: "right",
  w: "up",
  a: "left",
  s: "down",
  d: "right",
  W: "up",
  A: "left",
  S: "down",
  D: "right",
};

function App() {
  const [board, setBoard] = useState([]);
  const [gameOver, setGameOver] = useState(false);
  const [gameWon, setGameWon] = useState(false);

  // Start a new game on mount
  useEffect(() => {
    fetch(`${API_URL}/start`, { method: "POST" })
      .then(res => {
        return res.json();
      })
      .then(data => {
        setBoard(data.board);
        setGameOver(data.game_over);
        setGameWon(data.game_won);
      })
      .catch(err => {
        console.error("Error fetching /start:", err);
      });
  }, []);

  const handleMove = useCallback((direction) => {
    if (gameOver) return;
    fetch(`${API_URL}/move`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(direction)
    })
      .then(res => res.json())
      .then(data => {
        setBoard(data.board);
        setGameOver(data.game_over);
        setGameWon(data.game_won);
      });
  }, [gameOver]);

  // Keyboard event listener
  useEffect(() => {
    const handleKeyDown = (e) => {
      const direction = KEY_TO_DIRECTION[e.key];
      if (direction) {
        handleMove(direction);
        e.preventDefault();
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [handleMove]);

  return (
    <div style={{ textAlign: "center" }}>
      <h1>2048 Game</h1>
      <Instructions />
      <GameBoard board={board} />
      <StatusMessage gameWon={gameWon} gameOver={gameOver} />
    </div>
  );
}

export default App;