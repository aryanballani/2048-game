# 2048-game
### What is the Game?
2048 is a single-player sliding block puzzle game designed by Italian web developer Gabriele Cirulli. The game's objective is to slide numbered tiles on a grid to combine them to create a tile with the number 2048.
## Additional Features
My version of 2048 is developed such that:
- The board could be made for N x N, by changing the number in '\application\model\constant'
- The probability of giving out *twos* after each move can be changed by changing the number in '\application\model\constant'

## How to Play
The set of instructions you nedd to play the game are as follows:
- Swipe up: Press 'w' or 'W'
- Swipe Down Press 's' or 'S'
- Swipe Left Press 'a' or 'A'
- Swipe Right Press 'd' or 'D'

If the swipe is valid, i.e., the state of the Board changes, all the tiles on the Board will move in the direction of the swipe and merge if they are slide towards the same numbered tile.

Eg.-

 `Board = ` $\begin{bmatrix}16&8&4&2\\4&8&2&0\\0&0&0&0\\0&0&0&0\end{bmatrix}$ ----Swipe Left----> $\begin{bmatrix}16&8&4&2\\4&8&2&0\\0&0&0&0\\0&0&0&0\end{bmatrix}$

Here left swipe is redundant, since the state of the board remains the same and nothing moves and/or merges, but if :

`Board = ` $\begin{bmatrix}16&8&4&2\\4&8&2&0\\0&0&0&0\\0&0&0&0\end{bmatrix}$ ----Swipe Up----> $\begin{bmatrix}16&16&4&2\\4&0&2&0\\0&0&0&0\\0&0&2&0\end{bmatrix}$

Here the `8` in `(1,2)` and `(2,2)` merge to become a `16`, and a new tile is generated at a random empty position.

                    
## Requirements to Run the Game
You need Python3 to run this application on your system.

If you have the NumPy library then you are all set, otherwise, I have set up a virtual environment for you with NumPy library installed already.

## How to Run (If you don't have NumpPy installed): 
- On your terminal, after you are inside '\application', you need to activate the virtual environment.
- To activate the virtual environment, write ' \env\Scripts\activate ' on your terminal.
- There should now be " (env) " written on the left most side of your terminal, indicating that the environment is now active.
- Now, you should be able to run the program after going inside \application\ui using the command ' py console2048.py '


## PHASES
- **Phase 1** : Developing a console-based version of 2048 using python
- **Phase 2** : Developing a Graphical User Interface version of 2048 using python
  
****Current Status: Phase 2 in progress***
