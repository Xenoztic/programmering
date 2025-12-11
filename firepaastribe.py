#variabler
empty = " . "
player1 = "🔴 "
player2 = "🔵 "


#selve boardet
board =    [[empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty]]


#printer boardet og layoutet
def print_board():
    print("|  1  |  2  |  3  |  4  |  5  |  6  |  7  |")
    print("|  _  |  _  |  _  |  _  |  _  |  _  |  _  |")
    for row in range(0, len(board)):
        for col in board[row]:
            print("| " + col, end = " ")
        print("|")




#Markøren ligger sig i bunden af den valgte kolonne og medmindre der allerede er en markør, ellers ligger markøren sig om på.
def mark(col, player):
    for row in range(5, -1, -1):  #reverse range
        if board[row][col] == empty:
            board[row][col] = player
            return True
    print("That collum is full. Choose a new collum.")  #Der er ikke flere steder at placere markører.
    return False


                    
#vores win condition, hvor playeren skal have 4 i række i enten horisontalt, vertikalt eller diagonalt.
def check_for_win(player):

    #horisontalt
    for col in range(len(board[0])):
         for row in range(len(board)):
              if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:   
                return True

    #vertikalt
    for col in range(len(board[0])):
         for row in range(len(board) - 3):
              if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player: 
                return True

    #diagonalt højre-op
    for row in range(3, len(board)):
         for col in range(len(board[0]) - 3):
              if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True

    #diagonalt højre-ned
    for col in range(len(board[0]) - 3):
         for row in range(len(board) - 3):
              if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player: 
                return True
              
    return False


#vores game loop med 2 players 
def game_loop():
    
    print_board()
    while True:
        
        user_inp = int(input("Player 🔴 >"))-1 
        mark(user_inp, player1)
        print_board()
        
        if check_for_win(player1) == True:
            print("🔴 HAS WON THE GAME!")
            break


        user_inp = int(input("Player 🔵 >"))-1 #player 2 tilføjes
        mark(user_inp, player2)
        print_board()

        if check_for_win(player2) == True:
            print("🔵 HAS WON THE GAME!")
            break
game_loop()