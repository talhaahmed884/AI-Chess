from abc import ABC

from chess_resources.Classes.Dimension import Dimension
from chess_resources.Classes.Piece import Piece


class Bishop(Piece, ABC):
    def __init__(self, row: int, col: int, identity: str):
        self.row = row
        self.col = col
        self.identity = identity

    def checkMove(self, rowArg: int, colArg: int, board: list) -> bool:
        if Dimension.maxRow >= rowArg >= Dimension.minRow and Dimension.maxCol >= colArg >= Dimension.minCol:
            if abs(self.row - rowArg) == abs(self.col - colArg):
                if rowArg > self.row and colArg > self.col:
                    if not self._checkLowerRightDiagonal(rowArg, colArg, board):
                        return False
                elif rowArg > self.row and colArg < self.col:
                    if not self._checkLowerLeftDiagonal(rowArg, colArg, board):
                        return False
                elif self.row > rowArg and colArg > self.col:
                    if not self._checkUpperRightDiagonal(rowArg, colArg, board):
                        return False
                elif self.row > rowArg and colArg < self.col:
                    if not self._checkUpperLeftDiagonal(rowArg, colArg, board):
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

        return self.movePiece(rowArg, colArg, board)

    def movePiece(self, rowArg: int, colArg: int, board: list) -> bool:
        if board[rowArg][colArg] is None:
            return True
        elif board[rowArg][colArg].identity[0] == self.identity[0]:
            return False
        elif board[rowArg][colArg].identity[0] != self.identity[0]:
            return True
        else:
            return False

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
