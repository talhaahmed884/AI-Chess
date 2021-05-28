from abc import ABC

from chess_resources.Classes.Dimension import Dimension
from chess_resources.Classes.Piece import Piece


class Knight(Piece, ABC):
    def __init__(self, row: int, col: int, identity: str):
        self.row = row
        self.col = col
        self.identity = identity

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
        if board[rowArg][colArg] is None:
            return True
        elif board[rowArg][colArg].identity[0] == self.identity[0]:
            return False
        elif board[rowArg][colArg].identity[0] != self.identity[0]:
            return True
        else:
            return False
