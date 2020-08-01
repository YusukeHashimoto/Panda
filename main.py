board = [[" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], 
[" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "]] 


def addWhitePiece(x, y, s):
    board[y-1][x-1] = s

def addBlackPiece(x,y,s):
    board[y-1][x-1] = '\033[47m\33[30m' + s + '\033[0m'

def initBoard():
    for i in range(0,8):
        for j in range(0,8):
            board[i][j] = " "

    for i in range(1,9):
        addWhitePiece(i, 7, "P")
    addWhitePiece(1,8,"R")
    addWhitePiece(2,8,"N")
    addWhitePiece(3,8,"B")
    addWhitePiece(4,8,"K")
    addWhitePiece(5,8,"Q")
    addWhitePiece(6,8,"B")
    addWhitePiece(7,8,"N")
    addWhitePiece(8,8,"R")

    for i in range(1,9):
        addBlackPiece(i, 2, "P")
    addBlackPiece(1,1,"R")
    addBlackPiece(2,1,"N")
    addBlackPiece(3,1,"B")
    addBlackPiece(4,1,"Q")
    addBlackPiece(5,1,"K")
    addBlackPiece(6,1,"B")
    addBlackPiece(7,1,"N")
    addBlackPiece(8,1,"R")


def drawBoard():
    s = "  "
    for i in range(0,8):
        s += str(i+1) + " "
    print(s)

    s = " "
    for i in range(0,8):
        s = str(i+1) + " "
        for j in range(0,8):
            s += board[i][j] + " "
        print(s)
    print()

def move(fromX, fromY, toX, toY):
    piece = board[fromY-1][fromX-1]
    board[fromY-1][fromX-1] = " "
    board[toY-1][toX-1] = piece

def inputCommand():
    print(">", end="")
    command = input().split(',')
    print()

    fromX   = int(command[0])
    fromY   = int(command[1])
    toX     = int(command[2])
    toY     = int(command[3])

    move(fromX,fromY,toX,toY)

def main():
    initBoard()
    drawBoard()

    while True:
        inputCommand()
        drawBoard()

main()
