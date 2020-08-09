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


king = King(Color.WHITE, board)
board[4-1][4-1] = king  #King at (4,4)

print(king.canMove(4,4,5,4))

for x in range(0,8):
    for y in range(0,8):
        result = king.canMove(4,4,x,y)
        if result == True:
            print("King can move to (" + str(x) + ", " + str(y) + ")")
