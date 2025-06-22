from fastapi import FastAPI, Body
from src.model.game import Game2048
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:3000"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

game = Game2048()

@app.post("/start")
def start_game():
    game.start_game()
    return {
        "board": game.get_board().tolist(),
        "game_over": game.is_game_over(),
        "game_won": game.check_won()
    }

@app.post("/move")
def move(direction: str = Body(...)):
    if direction == "left":
        game.move_left()
    elif direction == "right":
        game.move_right()
    elif direction == "up":
        game.move_up()
    elif direction == "down":
        game.move_down()
    else:
        return {"error": "Invalid direction"}
    game.check_state()
    return {
        "board": game.get_board().tolist(),
        "game_over": game.is_game_over(),
        "game_won": game.check_won()
    }

@app.get("/state")
def get_state():
    return {
        "board": game.get_board().tolist(),
        "game_over": game.is_game_over(),
        "game_won": game.check_won()
    }