# ==========================================
# TASK 1: TIC-TAC-TOE USING MINIMAX
# ==========================================

# Board
board = [" "] * 9

# Winning combinations
WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


# ------------------------------------------
# Display board
# ------------------------------------------
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


# ------------------------------------------
# Check winner
# ------------------------------------------
def check_winner():
    for a, b, c in WINNING_COMBINATIONS:

        if board[a] == board[b] == board[c] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


# ------------------------------------------
# Minimax Algorithm
# ------------------------------------------
def minimax(is_maximizing):

    result = check_winner()

    # Terminal state
    if result == "X":
        return 1

    if result == "O":
        return -1

    if result == "Draw":
        return 0

    # MAX player = AI
    if is_maximizing:

        best_score = float("-inf")

        for i in range(9):

            if board[i] == " ":

                # AI makes move
                board[i] = "X"

                score = minimax(False)

                # Undo move
                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    # MIN player = Human
    else:

        best_score = float("inf")

        for i in range(9):

            if board[i] == " ":

                # Human makes move
                board[i] = "O"

                score = minimax(True)

                # Undo move
                board[i] = " "

                best_score = min(best_score, score)

        return best_score


# ------------------------------------------
# Find best move for AI
# ------------------------------------------
def best_move():

    best_score = float("-inf")
    move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "X"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


# ------------------------------------------
# Game
# ------------------------------------------
print("TIC-TAC-TOE")
print("You = O")
print("AI  = X")

while True:

    print_board()

    # Human move
    position = int(input("Enter your position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid move!")
        continue

    board[position] = "O"

    result = check_winner()

    if result:
        print_board()

        if result == "Draw":
            print("Game Draw!")
        else:
            print(result, "wins!")

        break

    # AI move
    ai_move = best_move()
    board[ai_move] = "X"

    print("AI selected position:", ai_move + 1)

    result = check_winner()

    if result:
        print_board()

        if result == "Draw":
            print("Game Draw!")
        else:
            print(result, "wins!")

        break