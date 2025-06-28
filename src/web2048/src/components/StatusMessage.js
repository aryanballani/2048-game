import "../style/StatusMessage.css";

function StatusMessage({ gameWon, gameOver }) {
    return (
        <>
            {gameWon && (
                <div className="status-message">
                    <h2>
                        Congratulations! You have finished the game! <br />
                        You can keep going or refresh the page to start a new game.
                    </h2>
                </div>
            )}
            {gameOver && (
                <div className="status-message">
                    <h2>Game Over!</h2>
                </div>
            )}
        </>
    );
}

export default StatusMessage;