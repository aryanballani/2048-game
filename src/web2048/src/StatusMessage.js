function StatusMessage({ gameWon, gameOver }) {
    return (
        <>
            {gameWon && (
                <h2>
                    Congratulations! You have finished the game! <br />
                    You can keep going or refresh the page to start a new game.
                </h2>
            )}
            {gameOver && <h2>Game Over!</h2>}
        </>
    );
}

export default StatusMessage;