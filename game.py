import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_player_move(board):
    while True:
        try:
            move = input("Enter your move (row,col e.g., 1,1): ")
            row, col = map(int, move.split(','))
            if board[row - 1][col - 1] == " ":
                return row - 1, col - 1
            else:
                print("This spot is already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Please use the format row,col (e.g., 1,1).")

def get_computer_move(board):
    empty_cells = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                empty_cells.append((r, c))
    return random.choice(empty_cells)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # X is the player, O is the computer

    while True:
        print_board(board)
        if current_player == "X":
            row, col = get_player_move(board)
            board[row][col] = "X"
            if is_winner(board, "X"):
                print_board(board)
                print("Congratulations! You win!")
                break
            current_player = "O"
        else:
            print("Computer's turn...")
            row, col = get_computer_move(board)
            board[row][col] = "O"
            if is_winner(board, "O"):
                print_board(board)
                print("Sorry, you lose. The computer wins.")
                break
            current_player = "X"

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
