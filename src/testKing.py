# coding:utf-8

import unittest
from piece import Piece, Color, King
from chessboard import ChessBoard

class TestKing(unittest.TestCase):
    def setUp(self):
        # initialze
        self.board = ChessBoard()
        self.board.empty()
        self.king = King(Color.WHITE, self.board)
        pass

    def tearDown(self):
        # terminate
        pass

    def test_canMove(self):
        self.board.addPiece(self.king, 1, 1)
        self.assertEqual(True, self.king.canMove(2,1))
        self.assertEqual(True, self.king.canMove(2,2))
        self.assertEqual(True, self.king.canMove(1,2))

        self.assertEqual(False, self.king.canMove(1,4))
        self.assertEqual(False, self.king.canMove(1,8))
        self.assertEqual(False, self.king.canMove(8,7))
        self.assertEqual(False, self.king.canMove(1,-1))

    def test_getOwnPos(self):
        self.board.addPiece(self.king, 0, 0)
        self.assertEqual((0,0), self.king.getOwnPos())
        self.board.empty()

        self.board.addPiece(self.king, 1, 1)
        self.assertEqual((1,1), self.king.getOwnPos())
        self.board.empty()

        self.board.addPiece(self.king, 3, 5)
        self.assertEqual((3,5), self.king.getOwnPos())
        self.board.empty()

        self.board.addPiece(self.king, 7, 7)
        self.assertEqual((7,7), self.king.getOwnPos())
        self.board.empty()

if __name__ == "__main__":
    unittest.main()