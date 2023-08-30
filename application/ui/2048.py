import sys
sys.path.append('../')
import model.workingModel as workingModel

# Global matrix board
# we will treat 0 as empty space on board
Board, gameEnd= workingModel.startGame()      
print(Board)

def listenCommand(command, board):
    if (command in ('a', 'A')) :
        workingModel.moveLeft(board)
    elif (command in ('s', 'S')) :
        workingModel.moveDown(board)
    elif (command in ('d', 'D')) :
        workingModel.moveRight(board)
    elif (command in ('w', 'W')) :
        workingModel.moveUp(board)
    else:
        command = input("Invalid Command. Try Again:")
        listenCommand(command, board)


while(gameEnd != True):
    command = input("Next Command:")
    listenCommand(command, Board)
    workingModel.addBlock(Board)       # adds either 2 or 4 to the Board at random, if there is space
    print(Board)
    gameEnd = workingModel.checkState(Board, gameEnd)




print("GAME OVER")

