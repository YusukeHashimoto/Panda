COLUMN_MIN = 0
ROW_MIN = 0
COLUMN_MAX = 8
ROW_MAX = 8

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

    def getPieceAt(self, x, y):
        return self.board[x-1][y-1]

    def empty(self):
        for x in range(COLUMN_MIN, COLUMN_MAX):
            for y in range(ROW_MIN, ROW_MAX):
                self.board[x][y] = None

    def addPiece(self, piece, x, y):
        self.board[x-1][y-1] = piece

#    def initialize(self):

#    def movePiece(self, fromX, fromY, toX, toY):