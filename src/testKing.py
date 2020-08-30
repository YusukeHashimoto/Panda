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
        self.assertEqual(True, self.king.canMove(1,1,2,1))
        self.assertEqual(True, self.king.canMove(1,1,2,2))
        self.assertEqual(True, self.king.canMove(1,1,1,2))

        self.assertEqual(False, self.king.canMove(1,1,1,4))

if __name__ == "__main__":
    unittest.main()