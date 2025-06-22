
function GameBoard({ board }) {
  if (!Array.isArray(board) || board.length === 0) {
    return <p>Loading board...</p>;
  }
  return (
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
  );
}

export default GameBoard;