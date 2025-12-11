empty = " . "
player1 = "🔴"
player2 = "🔵"

ROWS = 6
COLS = 7

board = [[empty for _ in range(COLS)] for _ in range(ROWS)]


def print_board():
    print("  " + "   ".join(str(i) for i in range(1, COLS + 1)))
    print("+" + "---+" * COLS)
    for r in range(ROWS):
        row_str = "| " + " | ".join(board[r][c] for c in range(COLS)) + " |"
        print(row_str)
        print("+" + "---+" * COLS)


def mark(col, player):
    # col er 0..6
    for row in range(ROWS - 1, -1, -1):  # 5,4,3,2,1,0
        if board[row][col] == empty:
            board[row][col] = player
            return True
    print("Den kolonne er fuld. Vælg en anden.")
    return False


def board_full():
    for c in range(COLS):
        if board[0][c] == empty:
            return False
    return True


def check_for_win(player):
    # Horizontal →
    for row in range(ROWS):
        for col in range(COLS - 3):
            if (board[row][col] == player and
                board[row][col + 1] == player and
                board[row][col + 2] == player and
                board[row][col + 3] == player):
                return True

    # Vertical ↓
    for row in range(ROWS - 3):
        for col in range(COLS):
            if (board[row][col] == player and
                board[row + 1][col] == player and
                board[row + 2][col] == player and
                board[row + 3][col] == player):
                return True

    # Diagonal ↘ (ned-højre)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (board[row][col] == player and
                board[row + 1][col + 1] == player and
                board[row + 2][col + 2] == player and
                board[row + 3][col + 3] == player):
                return True

    # Diagonal ↗ (op-højre)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if (board[row][col] == player and
                board[row - 1][col + 1] == player and
                board[row - 2][col + 2] == player and
                board[row - 3][col + 3] == player):
                return True

    return False


def get_move(player_name):
    while True:
        inp = input(f"{player_name} vælg kolonne (1-7): ").strip()
        if not inp.isdigit():
            print("Skriv et tal fra 1 til 7.")
            continue

        col = int(inp)
        if col < 1 or col > 7:
            print("Vælg en kolonne fra 1 til 7.")
            continue

        return col - 1  # til 0..6


def game_loop():
    print_board()

    while True:
        # Player 1
        col = get_move("Player 1 🔴")
        if mark(col, player1):
            print_board()
            if check_for_win(player1):
                print("🔴 HAR VUNDET SPILLET!")
                break
            if board_full():
                print("UAFGJORT! Brættet er fyldt.")
                break

        # Player 2
        col = get_move("Player 2 🔵")
        if mark(col, player2):
            print_board()
            if check_for_win(player2):
                print("🔵 HAR VUNDET SPILLET!")
                break
            if board_full():
                print("UAFGJORT! Brættet er fyldt.")
                break


game_loop()
