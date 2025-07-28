# Tic-Tac-Toe Game

A simple command-line implementation of the classic Tic-Tac-Toe game written in Python. Play against a computer opponent in this traditional 3x3 grid game.

## Features

- Interactive command-line interface
- Player vs Computer gameplay
- Easy-to-understand board visualization
- Input validation and error handling
- Random computer moves
- Win/Draw detection

## Requirements

- Python 3.x
- No additional packages required

## Installation

1. Clone this repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Run the game:
```bash
python game.py
```

## How to Play

1. The game is played on a 3x3 grid
2. You play as 'X' and the computer plays as 'O'
3. Enter your moves using row,column coordinates (e.g., "1,1" for the top-left corner)
4. The coordinate system works as follows:
   ```
   1,1 | 1,2 | 1,3
   ---------------
   2,1 | 2,2 | 2,3
   ---------------
   3,1 | 3,2 | 3,3
   ```
5. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins
6. If all cells are filled and no player has won, the game is a draw

## Game Rules

- Players take turns placing their marks ('X' or 'O') on empty cells
- You cannot place a mark on an already occupied cell
- The game ends when either:
  - A player gets three marks in a row (win)
  - All cells are filled (draw)

## Code Structure

- `print_board(board)`: Displays the current game board
- `is_winner(board, player)`: Checks if the specified player has won
- `is_board_full(board)`: Checks if the board is completely filled
- `get_player_move(board)`: Handles player input and move validation
- `get_computer_move(board)`: Generates computer's move
- `play_game()`: Main game loop
