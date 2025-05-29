# Cross Game or Tic-Tac-Toe Game
# a. Desc -> Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1
# is the Computer and the Player 2 is the user. Player 1 take Random Cell that is
# the Column and Row.
# b. I/P -> Take User Input for the Cell i.e. Col and Row to Mark the ‘X’
# c. Logic -> The User or the Computer can only take the unoccupied cell. The Game
# is played till either wins or till draw...
# d. O/P -> Print the Col and the Cell after every step.
# e. Hint -> The Hints is provided in the Logic. Use Functions for the Logic…


import random

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),         
    (0, 3, 6), (1, 4, 7), (2, 5, 8),          
    (0, 4, 8), (2, 4, 6)
]

def print_board(board):
    symbols = [str(i) if square == "" else square for i, square in enumerate(board)]
    line = "---|---|---"
    print(f" {symbols[0]} | {symbols[1]} | {symbols[2]}")
    print(line)
    print(f" {symbols[3]} | {symbols[4]} | {symbols[5]}")
    print(line)
    print(f" {symbols[6]} | {symbols[7]} | {symbols[8]}\n")

def winner(board, mark):
    return any(all(board[i] == mark for i in line) for line in WIN_LINES)

def board_full(board):
    return all(square != "" for square in board)

def get_free_squares(board):
    return [i for i, square in enumerate(board) if square == ""]

def tic_tac_toe():
    board = [""] * 9  
    human, computer = "X", "O"
    turn = "human"

    print("Welcome to the game .")
    print_board(board)

    while True:
        if turn == "human":
            try:
                move = int(input("Your move (0-8): "))
            except ValueError:
                print("Enter a NUMBER between 0 and 8.")
                continue
            if move not in range(9) or board[move] != "":
                print("That square’s taken or out of range, try again.")
                continue
            board[move] = human
            turn = "computer"
        else:
            move = random.choice(get_free_squares(board))
            print(f"Computer chooses {move}")
            board[move] = computer
            turn = "human"

        print_board(board)

        if winner(board, human):
            print("Congratulations, you win!")
            break
        if winner(board, computer):
            print("Computer wins. Better luck next time!")
            break
        if board_full(board):
            print("It’s a draw.")
            break

if __name__ == "__main__":
    tic_tac_toe()
