from enum import Enum, auto
from abc import ABCMeta
from abc import abstractmethod

class Color(Enum):
    WHITE = auto()
    BLACK = auto()

BLACK_PREFIX = '\033[47m\33[30m'
BLACK_POSTFIX = '\033[0m'
WHITE_PREFIX = ''
WHITE_POSTFIX = ''

class Piece(metaclass = ABCMeta):
    ch = " "    #displayed character

    def __init__(self, color, board):
        self.color = color
        self.board = board

    @abstractmethod
    def canMove(self, fromX, fromY, toX, toY):
        result = True

        pos = self.getOwnPos()
        fromX = pos[0]
        fromY = pos[1]

        if self.__checkRange(toX, toY) == False:
            result = False  #destination is out of board
        elif self.__checkDestPos(toX, toY) == False:
            result = False  #your piece on destination

        return result
    
    def __checkRange(self, toX, toY):
        result = True

        if toX > 8 or toX < 1:
            result = False
        elif toY > 8 or toY < 1:
            result = False
        
        return result

    def __checkDestPos(self, toX, toY):
#        if self.board[toX-1][toY-1] == None:
        if self.board.getPieceAt(toX,toY) == None:
            return True
        else:
            return not(self.board.getPieceAt(toX,toY).color == self.color)
#            return not(self.board[toX-1][toY-1].color == self.color)
    
    def draw(self):
        if self.color == Color.WHITE:
            s = WHITE_PREFIX + self.ch + WHITE_POSTFIX
        else:
            s = BLACK_PREFIX + self.ch + BLACK_POSTFIX
#        print(s, end="")
        return s

    def getOwnPos(self):
        for x in range(0,8):
            for y in range(0,8):
                if self == self.board.getPieceAt(x,y):
                    return (x,y)

class King(Piece):
    ch = "K"    #King

    def canMove(self, fromX, fromY, toX, toY):
        result = super().canMove(fromX, fromY, toX, toY)

        if (abs(fromX - toX) < 2) and (abs(fromY - toY) < 2) and not((fromX == toX) and (fromY == toY)):
            result = result and True
        else:
            result = False

        return result
