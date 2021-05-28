from abc import ABC

from Board import Dimension, Board
from Piece import Piece


class Rook(Piece, ABC):
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def checkMove(self, rowArg: int, colArg: int, board: Board) -> bool:
        if Dimension.maxRow >= rowArg > self.row and colArg == self.col:
            if self._checkRow(self.row, rowArg, 1, board):
                return self.movePiece(rowArg, colArg, board)
            else:
                return False
        elif Dimension.minRow <= rowArg < self.row and colArg == self.col:
            if self._checkRow(rowArg, self.row, -1, board):
                return self.movePiece(rowArg, colArg, board)
            else:
                return False
        elif rowArg == self.row and self.col < colArg <= Dimension.maxCol:
            if self._checkCol(self.col, colArg, 1, board):
                return self.movePiece(rowArg, colArg, board)
            else:
                return False
        elif rowArg == self.row and self.col > colArg >= Dimension.minCol:
            if self._checkCol(colArg, self.col, -1, board):
                return self.movePiece(rowArg, colArg, board)
            else:
                return False
        else:
            return False

    def movePiece(self, rowArg: int, colArg: int, board: Board) -> bool:
        if board.pieces[rowArg][colArg] is None:
            return True
        else:
            if board.pieces[rowArg][colArg].color == self.color:
                return False
            elif board.pieces[rowArg][colArg].color != self.color:
                return True
            else:
                return False

    def _checkRow(self, row: int, rowArg: int, increment: int, board: Board) -> bool:
        if increment > 0:
            start = row + 1
        elif increment < 0:
            start = row - 1

        for a in range(start, rowArg, increment):
            if board.pieces[a][self.col] is not None:
                return False
        return True

    def _checkCol(self, col: int, colArg: int, increment: int, board: Board) -> bool:
        if increment > 0:
            start = col + 1
        elif increment < 0:
            start = col - 1

        for a in range(start, colArg, increment):
            if board.pieces[self.row][a] is not None:
                return False
        return True
