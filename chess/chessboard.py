from piece import Piece, King, Color

COLUMN_MIN = 0
ROW_MIN = 0
COLUMN_MAX = 8
ROW_MAX = 8
DEFAULT_ARG = -1

class ChessBoard:
    board = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None]]

    posMap = {
        'a' : 0,
        'b' : 1,
        'c' : 2,
        'd' : 3,
        'e' : 4,
        'f' : 5,
        'g' : 6,
        'h' : 7,
    }

    def getPieceAt(self, arg1, arg2 = DEFAULT_ARG):
        if arg2 == DEFAULT_ARG:
            x = self.posMap[arg1[0]]
            y = int(arg1[1]) - 1
        else:
            x = arg1 - 1
            y = arg2 - 1

        return self.board[x][y]

    def empty(self):
        for x in range(COLUMN_MIN, COLUMN_MAX):
            for y in range(ROW_MIN, ROW_MAX):
                self.board[x][y] = None

    def addPiece(self, piece, arg1, arg2=DEFAULT_ARG):
        if arg2 == DEFAULT_ARG:    #access like 'c7'
            x = self.posMap[arg1[0]]
            y = int(arg1[1]) - 1
#            self.board[x][y] = piece
        else:                   #access like '2,7'
            x = arg1 - 1
            y = arg2 - 1
#            self.board[x-1][y-1] = piece
        self.board[x][y] = piece

#    def initialize(self):

#    def movePiece(self, fromX, fromY, toX, toY):

    def draw(self):
        s = "  "
        for i in range(0,8):
            s += str(chr(ord('a')+i)) + " "
        print(s)

        for y in reversed(range(1,9)):
            s = str(y) + " "
            print(s, end="")
            for x in range(1,9):
                p = self.getPieceAt(x,y)
                if p != None:
                    s = p.draw()
                else:
                    s = " "
                s += " "
                print(s, end="")

            print("")

