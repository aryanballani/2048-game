import React, { useEffect, useState } from "react";

const API_URL = "http://localhost:8000"; // Change to your backend URL when deployed

function App() {
  const [board, setBoard] = useState([]);
  const [gameOver, setGameOver] = useState(false);

  // Start a new game on mount
  useEffect(() => {
    fetch(`${API_URL}/start`, { method: "POST" })
      .then(res => res.json())
      .then(data => {
        setBoard(data.board);
        setGameOver(data.game_over);
      });
  }, []);

  const handleMove = (direction) => {
    fetch(`${API_URL}/move`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(direction)
    })
      .then(res => res.json())
      .then(data => {
        setBoard(data.board);
        setGameOver(data.game_over);
      });
  };

  const renderBoard = () => (
    <table>
      <tbody>
        {board.map((row, i) => (
          <tr key={i}>
            {row.map((cell, j) => (
              <td key={j} style={{ width: 50, height: 50, textAlign: "center", border: "1px solid #ccc" }}>
                {cell !== 0 ? cell : ""}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );

  return (
    <div style={{ textAlign: "center" }}>
      <h1>2048 Game</h1>
      {renderBoard()}
      <div style={{ margin: 20 }}>
        <button onClick={() => handleMove("up")}>Up</button>
        <button onClick={() => handleMove("left")}>Left</button>
        <button onClick={() => handleMove("down")}>Down</button>
        <button onClick={() => handleMove("right")}>Right</button>
      </div>
      {gameOver && <h2>Game Over!</h2>}
    </div>
  );
}

export default App;