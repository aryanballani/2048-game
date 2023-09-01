import numpy as np
import random
import model.constant as constant

# initializes the Board and returns the Board as well as the GameEnd Boolean
def startGame():
    Board = np.zeros((constant.GridSize, constant.GridSize), dtype = int)       # initializing Board
    # Board = np.array([[16,8,0,2],
    #                   [2,2,4,2],
    #                   [4,0,0,0],
    #                   [2,0,2,0]])
    firstTwoPosition = random.randint(0,pow(constant.GridSize, 2)-1)             # randomly generated position for the first 2
    Board[firstTwoPosition//4, firstTwoPosition%4] = 2                           
    print("The commands are as follows:\nSwipe Up : Press 'w' or 'W'\nSwipe Down : Press 's' or 'S'\nSwipe Left : Press 'a' or 'A'\nSwipe Right : Press 'd' or 'D'")
    print("Starting Game...")
    return Board, False

# checks the state of the Board to determine if you have Won, Lost or none:
# return gameEnd boolean, i.e, True when Won/Lost, False otherwise
def checkState(board):
    zeroCount = 0
    gameLost = True
    for i in range(constant.GridSize):
        for j in range(constant.GridSize):
            if (board[i, j] == 2048):
                print("You have WON")
                return True

    zeroCount = countZeroes(board) # checking if there is any zero present in the matrix
    gameLost = checkAdjecentCell(board) # checking if any move will work
    
    if (zeroCount == 0 and gameLost == True):
        print("You have LOST") 
        return True

# -Geneartes a random block (2 or 4 according to the ProbabilityOfTwo from constant.py)
# -if the board has space, add the generated block to a random empty location
def addBlock(board):
    # Generate 2 or 4 according to probabilty 
    number = random.randint(1, 10)
    if (number <= 10*constant.ProbabilityOfTwo):
        number = 2
    else:
        number = 4
    
    # if there is space, add the generated number
    if (countZeroes(board) > 0):
        addNumToEmptyBlock(board, number)
               
# Helper for addBlock, re-shuffles the position if the previous position was not empty
def addNumToEmptyBlock(board, num):
    position = random.randint(0, pow(constant.GridSize, 2)-1)
    r = position//4
    c = position%4
    if (board[r,c] == 0):
        board[r,c] = num
    else:
        addNumToEmptyBlock(board, num)

# Swipe Left
def moveLeft(Board):
    for i in range(0, constant.GridSize):
        packRow(Board[i], 0, constant.GridSize-1)
        for j in range(1, constant.GridSize):
            if (Board[i,j] == Board[i,j-1]):
                Board[i, j-1] = 2*Board[i, j-1]
                Board[i, j] = 0
                shiftRow(Board[i], j, constant.GridSize-1)

# Swipe Right
def moveRight(Board):
    tempBoard = flipBoard(Board)
    moveLeft(tempBoard)
    Board = flipBoard(tempBoard)
   

# Swipe Up
def moveUp(Board):
    tempBoard = transposeBoard(Board)
    moveLeft(tempBoard)
    Board = transposeBoard(tempBoard)


# Swipe Down
def moveDown(Board):
    tempBoard = transposeBoard(Board)
    tempBoard = flipBoard(tempBoard)
    moveLeft(tempBoard)
    tempBoard = flipBoard(tempBoard)
    Board = transposeBoard(tempBoard)


#HELPERS

# shifts a given row from start till the end towards the left, filling up empty space
# DOESN'T MERGE any blocks
def packRow(row, start, end):
    if (start == end):
        return
    nonZeroIndex = -1
    for i in range(start, end+1):
        if (row[i] != 0):
            nonZeroIndex = i
            break
    if (nonZeroIndex == -1):
        start = end-1
    else:
        temp = row[nonZeroIndex]
        row[nonZeroIndex] = row[start]
        row[start] = temp
    packRow(row, start+1, end)


# shifts a given row from start till the end towards the left, filling up empty 
# space and merging the same adjecent blocks (if any)
def shiftRow(row, start, end):
    if (start == end):
        row[start] = 0
        return
    
    if (row[start] == row[start+1]):
        row[start] = 2*row[start]
        shiftRow(row, start+1, end)
    
    temp = row[start]
    row[start] = row[start+1]
    row[start+1] = temp

    shiftRow(row, start+1, end)

# Takes in a board object and returns the **same object** after flipping the matrix
def flipBoard(board):
    for i in range(constant.GridSize):
        board[i] = board[i][::-1]
    return board

# Takes in a board object and returns the **same object** after transposing the matrix
def transposeBoard(board):
    temp = np.copy(board)
    for i in range(constant.GridSize):
        for j in range(constant.GridSize):
            board[i, j] = temp[j,i]
    return board

# Helper for checkState, counts the number of zeroes/ empty tiles on the board
def countZeroes(Board):
    count = 0
    for i in range(constant.GridSize):
        for j in range(constant.GridSize):
            if (Board[i, j] == 0):          
                count = count + 1
    return count

# Helper for checkState, return TRUE only if there is no possible move FALSE otherwise
def checkAdjecentCell(Board):
    endingNum = constant.GridSize-1
    for i in range(endingNum+1):
        for j in range(endingNum+1):
            if (i < endingNum and j < endingNum and ((Board[i, j] == Board[i, j+1]) or (Board[i, j] == Board[i+1, j]))):
                    return False
            elif (i == endingNum and j < endingNum and Board[i, j] == Board[i, j+1]):
                    return False
            elif (i < endingNum and j == endingNum and Board[i, j] == Board[i+1, j]):
                    return False
            else:
                 continue
    return True
        