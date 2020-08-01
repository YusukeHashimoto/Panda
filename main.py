board = [[" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], 
[" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "]] 

KING    = "K"
QUEEN   = "Q"
ROOK    = "R"
BISHOP  = "B"
KNIGHT  = "N"
PAWN    = "P"


def addWhitePiece(x, y, s):
    board[x-1][y-1] = s

def addBlackPiece(x,y,s):
    board[x-1][y-1] = '\033[47m\33[30m' + s + '\033[0m'

def initBoard():
    for i in range(0,8):
        for j in range(0,8):
            board[i][j] = " "

    for i in range(1,9):
        addWhitePiece(i, 7, PAWN)
    addWhitePiece(1,8,ROOK)
    addWhitePiece(2,8,KNIGHT)
    addWhitePiece(3,8,BISHOP)
    addWhitePiece(4,8,KING)
    addWhitePiece(5,8,QUEEN)
    addWhitePiece(6,8,BISHOP)
    addWhitePiece(7,8,KNIGHT)
    addWhitePiece(8,8,ROOK)

    for i in range(1,9):
        addBlackPiece(i, 2, PAWN)
    addBlackPiece(1,1,ROOK)
    addBlackPiece(2,1,KNIGHT)
    addBlackPiece(3,1,BISHOP)
    addBlackPiece(4,1,QUEEN)
    addBlackPiece(5,1,KING)
    addBlackPiece(6,1,BISHOP)
    addBlackPiece(7,1,KNIGHT)
    addBlackPiece(8,1,ROOK)


def drawBoard():
    s = "  "
    for i in range(0,8):
        s += str(i+1) + " "
    print(s)

    s = " "
    for i in range(0,8):
        s = str(i+1) + " "
        for j in range(0,8):
            s += board[j][i] + " "
        print(s)
    print()

def move(fromX, fromY, toX, toY):
    piece = board[fromX-1][fromY-1]
    board[fromX-1][fromY-1] = " "
    board[toX-1][toY-1] = piece

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
