from enum import Enum, auto

KING    = "K"   #King
QUEEN   = "Q"   #Queen
ROOK    = "R"   #Rook
BISHOP  = "B"   #Bishop
KNIGHT  = "N"   #kNight
PAWN    = "P"   #Pawn
EMPTY   = " "   #(empty)

board = [
[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], 
[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]]

class ErrorType(Enum):
    INVALID_COMMAND = auto()
    INVALID_MOVING = auto()

BLACK_PREFIX = '\033[47m\33[30m'
BLACK_POSTFIX = '\033[0m'
WHITE_PREFIX = ''
WHITE_POSTFIX = ''

def addWhitePiece(x, y, s):
    board[x-1][y-1] = WHITE_PREFIX + s + WHITE_POSTFIX

def addBlackPiece(x, y, s):
    board[x-1][y-1] = BLACK_PREFIX + s + BLACK_POSTFIX

def initBoard():
    for i in range(0,8):
        for j in range(0,8):
            board[i][j] = EMPTY

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
        s += str(i+1) + EMPTY
    print(s)

    s = EMPTY
    for i in range(0,8):
        s = str(i+1) + EMPTY
        for j in range(0,8):
            s += board[j][i] + EMPTY
        print(s)
    print()

def move(fromX, fromY, toX, toY):
    piece = board[fromX-1][fromY-1]
    board[fromX-1][fromY-1] = EMPTY
    board[toX-1][toY-1] = piece

def canMove(fromX, fromY, toX, toY):
    result = True
    if(board[fromX-1][fromY-1] == EMPTY):
        result = False
    else:
        result = True
    return result

def validateCommand(command):
    result = True
    if(len(command) != 4):
        result = False

    else:
        for i in range(0,4):
            if len(command[i]) < 1:
                result = False
                break
            if command[i].isdecimal == False:
                result = False

    return result

def inputCommand():
    validCommand = False
    while validCommand == False:
        print(">", end="")
        command = input().split(',')
        validCommand = validateCommand(command)

        if validCommand == True:
            command = list(map(lambda x: int(x), command))  #translate position from string to int
            if canMove(command[0],command[1],command[2],command[3]) == False:
                validCommand = False
                print("You cannot move")
        else:
            print("Invalid command")
    
    print()

    fromX   = command[0]
    fromY   = command[1]
    toX     = command[2]
    toY     = command[3]

    move(fromX,fromY,toX,toY)

def main():
    initBoard()
    drawBoard()

    while True:
        inputCommand()
        drawBoard()

main()
