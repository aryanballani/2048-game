import sys
sys.path.append('../')

import numpy as np
import model.workingModel as workingModel
import model.constant as constant

# Global matrix board
# we will treat 0 as empty space on board
Board, gameEnd= workingModel.startGame()
# prevBoard = np.zeros((constant.GridSize, constant.GridSize), dtype=int)  
prevBoard = np.copy(Board)
print(Board)


# HELPERS ---------------------------------------------------------------------------------
def boardStateNotSame(board, prevboard):
    for i in range(constant.GridSize):
        for j in range(constant.GridSize):
            if (board[i, j] != prevboard[i, j]):
                return True
    return False

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
#-------------------------------------------------------------------------------------------

while(gameEnd != True):
    command = input("Next Command:")
    prevBoard = np.copy(Board)
    listenCommand(command, Board)
    if (boardStateNotSame(Board, prevBoard)):
        workingModel.addBlock(Board)       # adds either 2 or 4 to the Board at random, if there is space
    print(Board)
    gameEnd = workingModel.checkState(Board)




print("GAME OVER")



