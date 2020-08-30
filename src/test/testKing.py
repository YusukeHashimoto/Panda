# coding:utf-8

import unittest
import piece as piece

class KingTest(unittest.TestCase):
    def setUp(self):
        # initialze
        board = ChessBoard()
        board.empty()
        king = King(Color.WHITE, board)
        pass

    def tearDown(self):
        # terminate
        pass

    def testKingMove(self):
        board.addPiece(king, 1, 1)
        self.assertEqual(true, king.canMove(1,1,2,1))
        self.assertEqual(true, king.canMove(1,1,2,2))
        self.assertEqual(true, king.canMove(1,1,1,2))
