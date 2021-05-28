from abc import ABC

from Board import Dimension, Board
from Piece import Piece, Color


class Pawn(Piece, ABC):
    def __init__(self, row: int, col: int, color: Color):
        self.row = row
        self.col = col
        self.color = color

    def checkMove(self, rowArg: int, colArg: int, board: Board) -> bool:
        if rowArg > Dimension.maxRow or colArg > Dimension.maxCol or rowArg < Dimension.minRow or colArg < \
                Dimension.minCol:
            return False
        elif rowArg == self.row or colArg == self.col:
            return False
        else:
            return self.movePiece(rowArg, colArg, board)

    def movePiece(self, rowArg: int, colArg: int, board: Board) -> bool:
        if self.color is Color.White:
            return self._whitePawnMove(rowArg, colArg, board)
        elif self.color is Color.Black:
            return self._blackPawnMove(rowArg, colArg, board)
        else:
            return False

    def _blackPawnMove(self, rowArg: int, colArg: int, board: Board) -> bool:
        if board.pieces[rowArg][colArg] is None:
            if self.row - rowArg == 2 and self.row == 6 and colArg == self.col:
                return True
            elif self.row - rowArg == 1 and colArg == self.col:
                return True
            else:
                return False
        elif board.pieces[rowArg][colArg].color is Color.White:
            if abs(colArg - self.col) == 1 and self.row - rowArg == 1:
                return True
            else:
                return False
        else:
            return False

    def _whitePawnMove(self, rowArg: int, colArg: int, board: Board) -> bool:
        if board.pieces[rowArg][colArg] is None:
            if rowArg - self.row == 2 and self.row == 1 and colArg == self.col:
                return True
            elif rowArg - self.row == 1 and colArg == self.col:
                return True
            else:
                return False
        elif board.pieces[rowArg][colArg].color is Color.Black:
            if abs(colArg - self.col) == 1 and rowArg - self.row == 1:
                return True
            else:
                return False
        else:
            return False
