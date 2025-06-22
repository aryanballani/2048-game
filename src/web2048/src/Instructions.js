function Instructions() {
    return (
        <div style={{ maxWidth: 400, margin: "0 auto 20px auto", background: "#f9f9f9", padding: 16, borderRadius: 8 }}>
            <h2>How to Play</h2>
            <ul style={{ textAlign: "left" }}>
                <li>Use <b>Arrow keys</b> or <b>ASWD</b> keys to move the tiles.</li>
                <li>When two tiles with the same number touch, they merge into one!</li>
                <li>Try to reach the <b>2048</b> tile.</li>
                <li>The game ends when no more moves are possible.</li>
            </ul>
        </div>
    );
}

export default Instructions;