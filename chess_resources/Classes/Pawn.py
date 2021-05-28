from abc import ABC

from chess_resources.Classes.Dimension import Dimension
from chess_resources.Classes.Piece import Piece


class Pawn(Piece, ABC):
    def __init__(self, row: int, col: int, identity: str):
        self.row = row
        self.col = col
        self.identity = identity

    def checkMove(self, rowArg: int, colArg: int, board) -> bool:
        if rowArg > Dimension.maxRow or colArg > Dimension.maxCol or rowArg < Dimension.minRow or colArg < \
                Dimension.minCol:
            return False
        elif rowArg == self.row and colArg == self.col:
            return False
        else:
            return self.movePiece(rowArg, colArg, board)

    def movePiece(self, rowArg: int, colArg: int, board: list) -> bool:
        if self.identity[0] == 'w':
            return self._whitePawnMove(rowArg, colArg, board)
        elif self.identity[0] == 'b':
            return self._blackPawnMove(rowArg, colArg, board)
        else:
            return False

    def _blackPawnMove(self, rowArg: int, colArg: int, board: list) -> bool:
        if board[rowArg][colArg] is None:
            if rowArg - self.row == 2 and self.row == 1 and colArg == self.col:
                return self._checkRow(self.row, rowArg, 1, board)
            elif rowArg - self.row == 1 and colArg == self.col:
                return True
            else:
                return False
        elif board[rowArg][colArg].identity[0] == 'w':
            if abs(colArg - self.col) == 1 and rowArg - self.row == 1:
                return True
            else:
                return False
        else:
            return False

    def _whitePawnMove(self, rowArg: int, colArg: int, board: list) -> bool:
        if board[rowArg][colArg] is None:
            if self.row - rowArg == 2 and self.row == 6 and colArg == self.col:
                return self._checkRow(self.row, rowArg, -1, board)
            elif self.row - rowArg == 1 and colArg == self.col:
                return True
            else:
                return False
        elif board[rowArg][colArg].identity[0] == 'b':
            if abs(colArg - self.col) == 1 and (self.row - rowArg) == 1:
                return True
            else:
                return False
        else:
            return False

    def _checkRow(self, row: int, rowArg: int, increment: int, board) -> bool:
        start = 0
        if increment > 0:
            start = row + 1
        elif increment < 0:
            start = row - 1

        for a in range(start, rowArg, increment):
            if board[a][self.col] is not None:
                return False
        return True

