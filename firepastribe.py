empty = "."
player1 = "0"
player2 = "X"

board =    [[empty, empty, empty, empty], 
            [empty, empty, empty, empty], 
            [empty, empty, empty, empty], 
            [empty, empty, empty, empty]]

def print_board():
    print("| 1 | 2 | 3 | 4 |")
    print("| _ | _ | _ | _ |")
    for row in range(0, len(board)):
        for col in board[row]:
            print("| " + col, end = " ")
        print("|")

def mark(col, player):
    for row in board:
            row[col] = player
          
#Markøren ligger sig i bunden af den valgte kolonne og medmindre der allerede er en markør, ellers ligger markøren sig om på.
def mark(col, player):
    for row in range(3, -1, -1):  #reverse range
        if board[row][col] == empty:
            board[row][col] = player
            return True
    print("That collum is full. Choose a new collum.")  #Der er ikke flere steder at placere markører.
    return False

                        
#win condition hvor playeren skal have 4 i række i enten vandret, lodret eller diagonalt.
def check_for_win(player):
    row = len(board)
    col = len(board[0])

    for r in range(row):
        for c in range(col - 3):
            if (board[row][col] == player and
                board[row][col+1] == player and
                board[row][col+2] == player and
                board[row][col] == player):

                return True
    return False 
    
    #Check columns

    #Check diagonal 1

    #Check diagonal 2


def game_loop():
    
    print_board()
    while True:
        
        user_inp = int(input("Player 1 >"))-1
        mark(user_inp, player1)
        print_board()

        user_inp = int(input("Player 2 >"))-1 #player 2 tilføjes
        mark(user_inp, player2)
        print_board()

        if check_for_win(player1):
                print("Player 1 wins!")
        else:
            print("Player 2 wins!")
            break
game_loop()