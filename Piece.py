import enum
from abc import abstractmethod

import Board


class Color(enum.Enum):
    Black = 0
    White = 1


class Piece:
    def __init__(self):
        self.row = None
        self.col = None
        self.isDead = False
        self.color = None

    def __str__(self):
        return str(self.row) + ' ' + str(self.col)

    @abstractmethod
    def checkMove(self, rowArg: int, colArg: int, board: Board) -> bool:
        pass

    @abstractmethod
    def movePiece(self, rowArg: int, colArg: int, board: Board) -> bool:
        pass
