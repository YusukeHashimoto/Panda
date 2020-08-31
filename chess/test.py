from piece import Piece
from piece import King
from piece import Color
from chessboard import ChessBoard

#def testKing(atX, atY):
#    board = ChessBoard()
#    board.empty()
#    king = King(Color.WHITE, board)
#    board.addPiece(king, 1, 1)
#
#    print("Test King at (" + str(atX) + ", " + str(atY) + ")")
#    for x in range(0,8):
#        for y in range(0,8):
#            result = king.canMove(x,y)
#            if result == True:
#                print("King can move to (" + str(x) + ", " + str(y) + ")")
#    print()
#
#testKing(3,3)
#testKing(1,1)

board = ChessBoard()

king = King(Color.WHITE, board)
board.addPiece(king, 7, 4)

board.draw()
