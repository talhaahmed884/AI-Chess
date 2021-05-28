from abc import ABC, abstractmethod

from Dimension import Dimension
from Piece import Piece


class Knight(Piece, ABC):
    def __init__(self, row: int, col: int, color: str):
        self.row = row
        self.col = col
        self.color = color

    @abstractmethod
    def checkMove(self, rowArg: int, colArg: int, board) -> bool:
        if Dimension.maxRow >= rowArg >= Dimension.minRow and Dimension.maxCol >= colArg >= Dimension.minCol:
            if abs(rowArg - self.row) == 2 and abs(colArg - self.col) == 1:
                return self.movePiece(rowArg, colArg, board)
            elif abs(rowArg - self.row) == 1 and abs(colArg - self.col) == 2:
                return self.movePiece(rowArg, colArg, board)
            else:
                return False
        else:
            return False

    def movePiece(self, rowArg: int, colArg: int, board) -> bool:
        if board.pieces[rowArg][colArg] is None:
            return True
        elif board.pieces[rowArg][colArg].color == self.color:
            return False
        elif board.pieces[rowArg][colArg].color != self.color:
            return True
        else:
            return False

