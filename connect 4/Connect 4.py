# Connect 4

# The board
board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

p1win = False
p2win = False

# Shows the Board
def showBoard(board):
    for i in board:
        print(i)
        
# Player 1 playing
def p1():
    valid = False
    counter = input("Player 1, select which column from 1-7: ")
    while not valid: 
        if not counter.isdigit():
            print("Error, did not input a number")
            counter = input("Player 1, select which column from 1-7: ")
            continue
        counter = int(counter)
        if counter > 7 or counter < 1:
            print("Error, did not input a number from 1-7")
            counter = input("Player 1, select which column from 1-7: ")
            continue
        valid = True
    occupied = False
    for row in range(5, -1, -1):
        if board[row][counter-1] == " ":
            board[row][counter-1] = "X"
            occupied = True
            break
    if occupied == True:
        checkWin1(board)
        showBoard(board)
    else:
        print("Error, that row is occupied.")
        p1()

# Player 2 playing
def p2():
    valid = False
    counter = input("Player 2, select which column from 1-7: ")
    while not valid: 
        if not counter.isdigit():
            print("Error, did not input a number")
            counter = input("Player 2, select which column from 1-7: ")
            continue
        counter = int(counter)
        if counter > 7 or counter < 1:
            print("Error, did not input a number from 1-7")
            counter = input("Player 2, select which column from 1-7: ")
            continue
        valid = True
    occupied = False
    for row in range(5, -1, -1):
        if board[row][counter-1] == " ":
            board[row][counter-1] = "O"
            occupied = True
            break
    if occupied == True:
        checkWin2(board)
        showBoard(board)
    else:
        print("Error, that row is occupied.")
        p2()

# Checks if player1 has won
def checkWin1(board):
    global p1win
    # Horizontally
    for row in range(6):
        for column in range(4):
            if board[row][column] == "X" and \
            board[row][column+1] == "X" and \
            board[row][column+2] == "X" and \
            board[row][column+3] == "X":
                p1win = True
                return
    # Vertically
    for column in range(7):
        for row in range(3):
            if board[row][column] == "X" and \
            board[row+1][column] == "X" and \
            board[row+2][column] == "X" and \
            board[row+3][column] == "X":
                p1win = True
                return
    
    # Diagonally 1
    for column in range(4):
        for row in range(3):
            if board[row][column] == "X" and \
            board[row+1][column+1] == "X" and \
            board[row+2][column+2] == "X" and \
            board[row+3][column+3] == "X":
                p1win = True
                return
            
    # Diagonally 2
    for column in range(3, 7):
        for row in range(3):
            if board[row][column] == "X" and \
            board[row+1][column-1] == "X" and \
            board[row+2][column-2] == "X" and \
            board[row+3][column-3] == "X":
                p1win = True
                return

# Checks if player2 has won
def checkWin2(board):
    global p2win
    # Horizontally
    for row in range(6):
        for column in range(4):
            if board[row][column] == "O" and \
            board[row][column+1] == "O" and \
            board[row][column+2] == "O" and \
            board[row][column+3] == "O":
                p2win = True
                return
    # Vertically
    for column in range(7):
        for row in range(3):
            if board[row][column] == "O" and \
            board[row+1][column] == "O" and \
            board[row+2][column] == "O" and \
            board[row+3][column] == "O":
                p2win = True
                return
    
    # Diagonally 1
    for column in range(4):
        for row in range(3):
            if board[row][column] == "O" and \
            board[row+1][column+1] == "O" and \
            board[row+2][column+2] == "O" and \
            board[row+3][column+3] == "O":
                p2win = True
                return
            
    # Diagonally 2
    for column in range(3, 7):
        for row in range(3):
            if board[row][column] == "O" and \
            board[row+1][column-1] == "O" and \
            board[row+2][column-2] == "O" and \
            board[row+3][column-3] == "O":
                p2win = True
                return

# Checks if the board is full
def fullBoard(board):
    for i in board[0]:
        if i == " ":
            return False
    return True

# Plays the game 
def playGame():
    showBoard(board)
    while not p1win and not p2win:
        p1()
        if p1win:
            print("Player 1 has won the game!")
            break
        p2()
        if p2win:
            print("Player 2 has won the game!")
            break
        # Checks if board is full, even amount of spaces so board can only be full after p2
        if fullBoard(board):
            print("It's a draw, board is full.")
            break
    

playGame()
