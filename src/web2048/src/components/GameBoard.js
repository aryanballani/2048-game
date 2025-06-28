import "../style/GameBoard.css";

function GameBoard({ board }) {
  if (!Array.isArray(board) || board.length === 0) {
    return <p>Loading board...The backend is hosted on Render free tier😅, Hence the cold start.</p>;
  }
  return (
    <table className="game-board-table">
      <tbody>
        {board.map((row, i) => (
          <tr key={i}>
            {row.map((cell, j) => (
              <td key={j}>
                {cell !== 0 ? cell : ""}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default GameBoard;