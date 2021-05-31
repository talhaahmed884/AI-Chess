from abc import ABC

from chess_resources.Classes.Dimension import Dimension
from chess_resources.Classes.Piece import Piece


class Rook(Piece, ABC):
    def __init__(self, row: int, col: int, identity: str):
        self.row = row
        self.col = col
        self.identity = identity
        self.canCastle = True

    def checkMove(self, rowArg: int, colArg: int, board) -> bool:
        if Dimension.maxRow >= rowArg > self.row and colArg == self.col:
            if self._checkRow(self.row, rowArg, 1, board):
                return self.movePiece(rowArg, colArg, board)
            else:
                return False
        elif Dimension.minRow <= rowArg < self.row and colArg == self.col:
            if self._checkRow(self.row, rowArg, -1, board):
                return self.movePiece(rowArg, colArg, board)
            else:
                return False
        elif rowArg == self.row and self.col < colArg <= Dimension.maxCol:
            if self._checkCol(self.col, colArg, 1, board):
                return self.movePiece(rowArg, colArg, board)
            else:
                return False
        elif rowArg == self.row and self.col > colArg >= Dimension.minCol:
            if self._checkCol(self.col, colArg, -1, board):
                return self.movePiece(rowArg, colArg, board)
            else:
                return False
        else:
            return False

    def movePiece(self, rowArg: int, colArg: int, board) -> bool:
        if board[rowArg][colArg] is None:
            return True
        else:
            if board[rowArg][colArg].identity[0] == self.identity[0]:
                return False
            elif board[rowArg][colArg].identity[0] != self.identity[0]:
                return True
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

    def _checkCol(self, col: int, colArg: int, increment: int, board) -> bool:
        if increment > 0:
            start = col + 1
        elif increment < 0:
            start = col - 1

        for a in range(start, colArg, increment):
            if board[self.row][a] is not None:
                return False
        return True

    def disableCastling(self):
        if self.identity[0] == 'w':
            if self.row != 7 and self.col != 0 or self.col != 7:
                self.canCastle = False
        elif self.identity[0] == 'b':
            if self.row != 0 and self.col != 0 or self.col != 7:
                self.canCastle = False

