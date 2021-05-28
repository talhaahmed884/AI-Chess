from abc import ABC

from chess_resources.Classes.Dimension import Dimension
from chess_resources.Classes.Piece import Piece


class Queen(Piece, ABC):
    def __init__(self, row: int, col: int, identity: str):
        self.row = row
        self.col = col
        self.identity = identity

    def checkMove(self, rowArg: int, colArg: int, board: list) -> bool:
        if self.row < Dimension.minRow or self.row > Dimension.maxRow or self.col < Dimension.minCol or self.col > \
                Dimension.maxCol:
            return False
        elif board[rowArg][colArg] is not None and self.identity[0] == board[rowArg][colArg].identity[0]:
            return False
        else:
            return self.movePiece(rowArg, colArg, board)

    def movePiece(self, rowArg: int, colArg: int, board: list) -> bool:
        if self.col == colArg and self.row > rowArg:
            return self._checkRow(self.row, rowArg, -1, board)
        elif self.col == colArg and self.row < rowArg:
            return self._checkRow(self.row, rowArg, 1, board)
        elif self.col < colArg and self.row == rowArg:
            return self._checkCol(self.col, colArg, 1, board)
        elif self.col > colArg and self.row == rowArg:
            return self._checkCol(self.col, colArg, -1, board)
        elif abs(self.row - rowArg) != abs(self.col - colArg):
            return False
        else:
            if self.col < colArg and self.row > rowArg:
                return self._checkUpperRightDiagonal(rowArg, colArg, board)
            elif self.col < colArg and self.row < rowArg:
                return self._checkLowerRightDiagonal(rowArg, colArg, board)
            elif self.col > colArg and self.row > rowArg:
                return self._checkUpperLeftDiagonal(rowArg, colArg, board)
            elif self.col > colArg and self.row < rowArg:
                return self._checkLowerLeftDiagonal(rowArg, colArg, board)
            else:
                return False

    def _checkRow(self, row: int, rowArg: int, increment: int, board: list) -> bool:
        if increment > 0:
            start = row + 1
        elif increment < 0:
            start = row - 1

        for a in range(start, rowArg, increment):
            if board[a][self.col] is not None:
                return False
        return True

    def _checkCol(self, col: int, colArg: int, increment: int, board: list) -> bool:
        if increment > 0:
            start = col + 1
        elif increment < 0:
            start = col - 1

        for a in range(start, colArg, increment):
            if board[self.row][a] is not None:
                return False
        return True

    def _checkLowerRightDiagonal(self, rowArg: int, colArg: int, board: list) -> bool:
        for currRow, currCol in zip(range(self.row + 1, rowArg), range(self.col + 1, colArg)):
            if board[currRow][currCol] is not None:
                return False
        return True

    def _checkUpperLeftDiagonal(self, rowArg: int, colArg: int, board: list) -> bool:
        for currRow, currCol in zip(range(self.row - 1, rowArg, -1), range(self.col - 1, colArg, -1)):
            if board[currRow][currCol] is not None:
                return False
        return True

    def _checkUpperRightDiagonal(self, rowArg: int, colArg: int, board: list) -> bool:
        for currRow, currCol in zip(range(self.row - 1, rowArg, -1), range(self.col + 1, colArg)):
            if board[currRow][currCol] is not None:
                return False
        return True

    def _checkLowerLeftDiagonal(self, rowArg: int, colArg: int, board: list) -> bool:
        for currRow, currCol in zip(range(self.row + 1, rowArg), range(self.col - 1, colArg, -1)):
            if board[currRow][currCol] is not None:
                return False
        return True
