# coding:utf-8

import unittest
from piece import Piece, Color, King
from chessboard import ChessBoard

class TestChessBoard(unittest.TestCase):
    def setUp(self):
        self.board = ChessBoard()
        self.board.empty()

    def tearDown(self):
        pass

    def test_addPiece(self):
        for x in range(1,9):
            for y in range(1,9):
                self.sub_test_addPiece1(x, y, x-1, y-1)
                pass
        self.sub_test_adddPiece2('a1', 0, 0)
        self.sub_test_adddPiece2('h8', 7, 7)
        self.sub_test_adddPiece2('c7', 2, 6)

    def sub_test_addPiece1(self, x, y, exp_x, exp_y):
        king = King(Color.WHITE, self.board)
        self.board.addPiece(king, x, y)
        self.assertEqual(self.board.board[exp_x][exp_y], king)
        self.board.empty()

    def sub_test_adddPiece2(self, pos, exp_x, exp_y):
        king = King(Color.WHITE, self.board)
        self.board.addPiece(king, pos)
        self.assertEqual(self.board.board[exp_x][exp_y], king)
        self.board.empty()

    def test_getPieceAt(self):
        pass
        self.sub_test_getPieceAt(1, 1)
        self.sub_test_getPieceAt(8, 8)
        self.sub_test_getPieceAt2('a1')

    def sub_test_getPieceAt(self, x, y):
        king = King(Color.BLACK, self.board)
        self.board.addPiece(king, x, y)
        result = self.board.getPieceAt(x, y)
        self.assertEqual(king, result)
        self.board.empty()

    def sub_test_getPieceAt2(self, pos):
        king = King(Color.BLACK, self.board)
        self.board.addPiece(king, pos)
        result = self.board.getPieceAt(pos)
        self.assertEqual(king, result)
        self.board.empty()

if __name__ == "__main__":
    unittest.main()