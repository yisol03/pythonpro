import random

def instructions():
		print("\n\tWelcome to the world's greatest game!")
		print("\tThis will be a showdown between your human brain and my silicon processor.")
		print("\n\n\tYou will make your move known by entering a number, 0 - 8.")
		print("\tThe number will correspond to the board position as illustrated:")
		print("\n\t\t\t\t\t0 | 1 | 2")
		print("\t\t\t\t\t---------")
		print("\t\t\t\t\t3 | 4 | 5")
		print("\t\t\t\t\t---------")
		print("\t\t\t\t\t6 | 7 | 8")
		print("\n\tPrepare yourself, human. The ultimate battle is about to begin.")
		
def choose_first_player():
    while True:
        choice = input("Do you require the first move? (y / n): ").strip().lower()
        if choice in ["y", "n"]:
            if choice == "y":
                return "X", "O"
            else:
                return "O", "X"
            
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def player_move(board, player):
    while True:
        try:
            move = int(input(f"Where will you move? <0 - 8>: "))
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = player
                break
            else:
                print("Invalid input or already selected location. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def computer_move(board, computer, player):
    best_score = -float("inf")
    best_move = None

    for move in range(9):
        if board[move] == " ":
            board[move] = computer
            score = minimax(board, 0, False, computer, player)
            board[move] = " "

            if score > best_score:
                best_score = score
                best_move = move

    board[best_move] = computer

def minimax(board, depth, is_maximizing, computer, player):
    if check_winner(board, computer):
        return 1
    elif check_winner(board, player):
        return -1
    elif " " not in board:
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for move in range(9):
            if board[move] == " ":
                board[move] = computer
                score = minimax(board, depth + 1, False, computer, player)
                board[move] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in range(9):
            if board[move] == " ":
                board[move] = player
                score = minimax(board, depth + 1, True, computer, player)
                board[move] = " "
                best_score = min(score, best_score)
        return best_score

def main():
    instructions()
    player, computer = choose_first_player()
    board = [" "] * 9
    print_board(board)

    while True:
        if player == "X":
            player_move(board, player)
            print_board(board)

            if check_winner(board, player):
                print("Player Win!")
                break
            elif " " not in board:
                print("Draw!")
                break

            computer_move(board, computer, player)
            print_board(board)

            if check_winner(board, computer):
                print("Computer Win")
                break
            elif " " not in board:
                print("Draw")
                break
        else:
            computer_move(board, computer, player)
            print_board(board)

            if check_winner(board, computer):
                print("Computer Win!")
                break
            elif " " not in board:
                print("Draw")
                break

            player_move(board, player)
            print_board(board)

            if check_winner(board, player):
                print("Player Win!")
                break
            elif " " not in board:
                print("Draw")
                break

if __name__ == "__main__":
    main()
