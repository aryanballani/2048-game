import React, { useEffect, useState, useCallback } from "react";

const API_URL = "http://127.0.0.1:8000";

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
      .then(res => res.json())
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

  const renderBoard = () => (
    Array.isArray(board) && board.length > 0 ? (
      <table style={{ margin: "0 auto" }}>
        <tbody>
          {board.map((row, i) => (
            <tr key={i}>
              {row.map((cell, j) => (
                <td key={j} style={{ width: 50, height: 50, textAlign: "center", border: "1px solid #ccc", fontSize: 24 }}>
                  {cell !== 0 ? cell : ""}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    ) : (
      <p>Loading board...</p>
    )
  );

  return (
    <div style={{ textAlign: "center" }}>
      <h1>2048 Game</h1>
      <div style={{ maxWidth: 400, margin: "0 auto 20px auto", background: "#f9f9f9", padding: 16, borderRadius: 8 }}>
        <h2>How to Play</h2>
        <ul style={{ textAlign: "left" }}>
          <li>Use <b>Arrow keys</b> or <b>WASD</b> keys to move the tiles.</li>
          <li>When two tiles with the same number touch, they merge into one!</li>
          <li>Try to reach the <b>2048</b> tile.</li>
          <li>The game ends when no more moves are possible.</li>
        </ul>
      </div>
      {renderBoard()}
      {gameWon && <h2>Congratulations! You have finished the game! <br /> 
                  You can keep going or refresh the page to start a new game.</h2>}
      {gameOver && <h2>Game Over!</h2>}
    </div>
  );
}

export default App;