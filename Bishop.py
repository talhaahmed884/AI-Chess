from abc import ABC, abstractmethod

from Board import Board, Dimension
from Piece import Piece, Color


class Bishop(Piece, ABC):
    def __init__(self, row: int, col: int, color: Color):
        self.row = row
        self.col = col
        self.color = color

    @abstractmethod
    def checkMove(self, rowArg: int, colArg: int, board: Board) -> bool:
        if Dimension.maxRow >= rowArg >= Dimension.minRow and Dimension.maxCol >= colArg >= Dimension.minCol:
            if rowArg > self.row:
                if colArg > self.col:
                    if not self._checkLowerRightDiagonal(rowArg, colArg, board):
                        return False
                elif colArg < self.col:
                    if not self._checkLowerLeftDiagonal(rowArg, colArg, board):
                        return False
                else:
                    return False
            elif self.row > rowArg:
                if colArg > self.col:
                    if not self._checkUpperRightDiagonal(rowArg, colArg, board):
                        return False
                elif colArg < self.col:
                    if not self._checkUpperLeftDiagonal(rowArg, colArg, board):
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

        return self.movePiece(rowArg, colArg, board)

    def movePiece(self, rowArg: int, colArg: int, board: Board) -> bool:
        if board.pieces[rowArg][colArg] is None:
            return True
        elif board.pieces[rowArg][colArg].color == self.color:
            return False
        elif board.pieces[rowArg][colArg].color != self.color:
            return True
        else:
            return False

    def _checkLowerRightDiagonal(self, rowArg: int, colArg: int, board: Board) -> bool:
        for currRow, currCol in zip(range(self.row, rowArg + 1), range(self.col, colArg + 1)):
            if (currRow == rowArg and currCol != colArg) or (currRow != rowArg and currCol == colArg):
                return False
            if board.pieces[currRow][currCol] is not None:
                return False
        return True

    def _checkUpperLeftDiagonal(self, rowArg: int, colArg: int, board: Board) -> bool:
        for currRow, currCol in zip(range(self.row - 1, rowArg - 1, -1), range(self.col - 1, colArg - 1, -1)):
            if (currRow == rowArg and currCol != colArg) and (currRow != rowArg and currCol == colArg):
                return False
            if (currRow != rowArg and currCol == colArg) and (currRow == rowArg and currCol != colArg):
                return False
        return True

    def _checkUpperRightDiagonal(self, rowArg: int, colArg: int, board: Board) -> bool:
        for currRow, currCol in zip(range(self.row - 1, rowArg - 1, -1), range(self.col + 1, colArg + 1)):
            if (currRow == rowArg and currCol != colArg) and (currRow != rowArg and currCol == colArg):
                return False
            if (currRow != rowArg and currCol == colArg) and (currRow == rowArg and currCol != colArg):
                return False
        return True

    def _checkLowerLeftDiagonal(self, rowArg: int, colArg: int, board: Board) -> bool:
        for currRow, currCol in zip(range(self.row + 1, rowArg + 1), range(self.col - 1, colArg - 1, -1)):
            if (currRow == rowArg and currCol != colArg) or (currRow != rowArg and currCol == colArg):
                return False
            if board.pieces[currRow][currCol] is not None:
                return False
        return True

