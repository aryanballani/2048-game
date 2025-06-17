import numpy as np
from src.model.game import Game2048

# Global matrix board
# we will treat 0 as empty space on board
game = Game2048()
Board, gameEnd= game.get_board(), game.is_game_over()
prevBoard = np.copy(Board)
print(Board)


# HELPERS ---------------------------------------------------------------------------------
def listenCommand():
    while True:
        command = input("Next Command (W/A/S/D to move, Q to quit): ")
        if command.lower() == 'q':
            print("Exiting Game...")
            return False
        elif command.lower() in ('a', 's', 'd', 'w'):
            if command.lower() == 'a':
                game.move_left()
            elif command.lower() == 's':
                game.move_down()
            elif command.lower() == 'd':
                game.move_right()
            elif command.lower() == 'w':
                game.move_up()
            return True
        else:
            print("Invalid Command. Try Again.")
#-------------------------------------------------------------------------------------------

while not gameEnd:
    if not listenCommand():
        break
    Board = game.get_board()    # adds either 2 or 4 to the Board at random, if there is space
    print(Board)
    gameEnd = game.check_state()

print("GAME OVER")



