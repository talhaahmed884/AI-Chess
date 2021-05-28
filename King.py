from abc import ABC

from Board import Board, Dimension
from Piece import Piece, Color


class King(Piece, ABC):
    def __init__(self, row: int, col: int, color: Color):
        self.row = row
        self.col = col
        self.color = color

    def checkMove(self, rowArg: int, colArg: int, board: Board) -> bool:
        if Dimension.maxRow >= rowArg >= Dimension.minRow and Dimension.maxCol >= colArg >= Dimension.minCol:
            if (abs(self.row - rowArg) == 1 and self.col == colArg) or \
                    (abs(self.col - colArg) == 1 and self.row == rowArg):
                return self.movePiece(rowArg, colArg, board)
            else:
                return False
        else:
            return False

    def movePiece(self, rowArg: int, colArg: int, board: Board) -> bool:
        if board.pieces[rowArg][colArg] is None:
            return True
        elif board.pieces[rowArg][colArg].color != self.color:
            return True
        elif board.pieces[rowArg][colArg].color == self.color:
            return False
        else:
            return False

