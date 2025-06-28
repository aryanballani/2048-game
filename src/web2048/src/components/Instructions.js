import '../style/Instructions.css';

function Instructions() {
    return (
        <div className="instructions-container">
            <h2 className="instructions-title">How to Play</h2>
            <ul className="instructions-list">
                <li>
                    Use <b>Arrow keys</b> or <b>ASWD</b> keys to move the tiles. (Swipe on mobile)
                </li>
                <li>
                    When two tiles with the same number touch, they merge into one!
                </li>
                <li>
                    Try to reach the <b>2048</b> tile.
                </li>
                <li>
                    The game ends when no more moves are possible.
                </li>
            </ul>
        </div>
    );
}

export default Instructions;