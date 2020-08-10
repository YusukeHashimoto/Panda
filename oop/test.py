from piece import Piece
from piece import King
from piece import Color

board = [
[None, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None], 
[None, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None]]

def initBoard():
    for x in range(0,8):
        for y in range(0,8):
            board[x][y] = None


king = King(Color.WHITE, board)

#test king.canMove()
def testKing(atX, atY):
    initBoard()
    board[atX-1][atY-1] = king
    print("test king at (" + str(atX) + "," + str(atY) + ")")

    for x in range(0,8):
        for y in range(0,8):
            result = king.canMove(atX,atY,x,y)
            if result == True:
                print("King can move to (" + str(x) + ", " + str(y) + ")")

testKing(3,3)
