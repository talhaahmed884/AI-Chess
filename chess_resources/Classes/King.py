from abc import ABC

from chess_resources.Classes.Dimension import Dimension
from chess_resources.Classes.Piece import Piece


class King(Piece, ABC):
    def __init__(self, row: int, col: int, identity: str):
        self.row = row
        self.col = col
        self.identity = identity

    def checkMove(self, rowArg: int, colArg: int, board) -> bool:
        if Dimension.maxRow >= rowArg >= Dimension.minRow and Dimension.maxCol >= colArg >= Dimension.minCol:
            if (abs(self.row - rowArg) == 1 and self.col == colArg) or \
                    (abs(self.col - colArg) == 1 and self.row == rowArg):
                return self.movePiece(rowArg, colArg, board)
            else:
                return False
        else:
            return False

    def movePiece(self, rowArg: int, colArg: int, board) -> bool:
        if board[rowArg][colArg] is None:
            return True
        elif board[rowArg][colArg].identity[0] != self.identity[0]:
            return True
        elif board[rowArg][colArg].identity[0] == self.identity[0]:
            return False
        else:
            return False
