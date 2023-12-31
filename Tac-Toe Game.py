# Tic-Tac-Toe Game

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("-------")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("-------")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")

# Function to check if a player has won
def check_win(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Main game loop
def play_game():
    current_player = "X"
    while True:
        print_board()
        position = int(input("Player " + current_player + ", choose a position (1-9): ")) - 1
        if board[position] == " ":
            board[position] = current_player
            if check_win(current_player):
                print_board()
                print("Player " + current_player + " wins!")
                break
            elif " " not in board:
                print_board()
                print("It's a tie!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

# Start the game
play_game()
