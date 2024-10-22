# TicTacToe AI Game

Welcome to the **TicTacToe AI Game**! This is a Python-based Tic-Tac-Toe game where you can play against an AI opponent. The AI is programmed to make intelligent moves using minimax algorithm, providing a challenging experience for the player.

## Features

- Single-player mode: Play against the AI
- The AI uses the **Minimax Algorithm** for optimal moves
- Simple command-line interface (CLI)
- Clear game instructions and prompts

## How to Play

The game is played on a 3x3 grid. Players take turns to place their mark (either 'X' or 'O') in one of the empty spaces. The first player to align three marks horizontally, vertically, or diagonally wins the game. If all spaces are filled and no one has won, the game results in a draw.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/TicTacToe.git
    cd TicTacToe
    ```

2. Ensure you have Python 3.x installed on your system. If not, download it [here](https://www.python.org/downloads/).

3. No external libraries are required. The game runs on basic Python, so no additional dependencies need to be installed.

## How to Run the Game

1. Navigate to the directory where you cloned the project.
2. Run the `tictactoe.py` file:

    ```bash
    python3 tictactoe.py
    ```

3. Follow the on-screen instructions to start playing against the AI.

## Game Controls

- Enter a number between 1 and 9 to place your mark on the board.
    - The board layout corresponds to numbers as follows:

      ```
      1 | 2 | 3
      ---------
      4 | 5 | 6
      ---------
      7 | 8 | 9
      ```

- The player is 'X', and the AI is 'O'.
- The game will display the current board after each move and announce the winner or if it’s a draw.

## Example Game

```bash
Welcome to Tic-Tac-Toe!
Player X, choose a position (1-9): 5
 O |   |  
---------
 X | O |  
---------
   |   | X
