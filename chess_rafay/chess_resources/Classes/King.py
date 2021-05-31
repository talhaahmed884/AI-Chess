from abc import ABC

from chess_resources.Classes.Dimension import Dimension
from chess_resources.Classes.Piece import Piece


class King(Piece, ABC):
    def __init__(self, row: int, col: int, identity: str):
        self.row = row
        self.col = col
        self.identity = identity
        self.isUnderCheck = False

    def checkMove(self, rowArg: int, colArg: int, board: list) -> bool:
        if Dimension.maxRow >= rowArg >= Dimension.minRow and Dimension.maxCol >= colArg >= Dimension.minCol:
            if (abs(self.row - rowArg) == 1 and self.col == colArg) or \
                    (abs(self.col - colArg) == 1 and self.row == rowArg) or \
                    (abs(self.col - colArg) == 1 and abs(self.row - rowArg) == 1):
                return self.movePiece(rowArg, colArg, board)
            else:
                return False
        else:
            return False

    def movePiece(self, rowArg: int, colArg: int, board: list) -> bool:
        if board[rowArg][colArg] is None:
            return True
        elif board[rowArg][colArg].identity[0] != self.identity[0]:
            return True
        elif board[rowArg][colArg].identity[0] == self.identity[0]:
            return False
        else:
            return False

    def isCheck(self, board: list) -> bool:
        for a in range(0, Dimension.maxRow + 1):
            for b in range(0, Dimension.maxCol + 1):
                if board[a][b] is not None:
                    if board[a][b].identity[0] != self.identity[0]:
                        if board[a][b].checkMove(self.row, self.col, board):
                            # self.isUnderCheck = True
                            # print('KING UNDER CHECK')
                            return True

        return False
