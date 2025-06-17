from fastapi import FastAPI, Body
from src.model.game import Game2048

app = FastAPI()
game = Game2048()

@app.post("/start")
def start_game():
    game.start_game()
    return {
        "board": game.get_board().tolist(),
        "game_over": game.is_game_over()
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
        "game_over": game.is_game_over()
    }

@app.get("/state")
def get_state():
    return {
        "board": game.get_board().tolist(),
        "game_over": game.is_game_over()
    }