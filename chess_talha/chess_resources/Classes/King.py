from abc import ABC

from chess_resources.Classes.Dimension import Dimension
from chess_resources.Classes.Piece import Piece
from chess_resources.Classes.Rook import Rook


class King(Piece, ABC):
    def __init__(self, row: int, col: int, identity: str):
        self.row = row
        self.col = col
        self.identity = identity
        self.isUnderCheck = False
        self.canCastle = True

    def checkMove(self, rowArg: int, colArg: int, board: list) -> bool:
        if Dimension.maxRow >= rowArg >= Dimension.minRow and Dimension.maxCol >= colArg >= Dimension.minCol:
            if (abs(self.row - rowArg) == 1 and self.col == colArg) or \
                    (abs(self.col - colArg) == 1 and self.row == rowArg) or \
                    (abs(self.col - colArg) == 1 and abs(self.row - rowArg) == 1):
                return self.movePiece(rowArg, colArg, board)
            elif rowArg == self.row and abs(colArg - self.col) == 2:
                if self._checkCastling(colArg, board) and not self.isCheck(board) and self.canCastle:
                    return self.movePiece(rowArg, colArg, board)

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

    def _checkCastling(self, colArg: int, board: list) -> bool:
        if self.col > colArg:
            return self._checkLeftSideCastling(board)
        elif self.col < colArg:
            return self._checkRightSideCastling(board)

        return False

    def _checkLeftSideCastling(self, board: list) -> bool:
        if self.identity[0] == 'w':
            if isinstance(board[7][0], Rook):
                if board[7][0].canCastle:
                    return self._validCol(0, board)
        elif self.identity[0] == 'b':
            if isinstance(board[0][0], Rook):
                if board[0][0].canCastle:
                    return self._validCol(0, board)

        return False

    def _checkRightSideCastling(self, board: list) -> bool:
        if self.identity[0] == 'w':
            if isinstance(board[7][7], Rook):
                if board[7][7].canCastle:
                    return self._validCol(7, board)
        elif self.identity[0] == 'b':
            if isinstance(board[0][7], Rook):
                if board[0][7].canCastle:
                    return self._validCol(7, board)

        return False

    def _validCol(self, colArg: int, board: list) -> bool:
        if self.col > colArg:
            return self._checkCol(self.col, colArg, -1, board)
        elif self.col < colArg:
            return self._checkCol(self.col, colArg, +1, board)

        return False

    def _checkCol(self, col: int, colArg: int, increment: int, board) -> bool:
        if increment > 0:
            start = col + 1
        elif increment < 0:
            start = col - 1

        for a in range(start, colArg, increment):
            if board[self.row][a] is not None or self._moveUnderAttack(self.row, a, board):
                return False
        return True

    def isCheck(self, board: list) -> bool:
        for a in range(0, Dimension.maxRow + 1):
            for b in range(0, Dimension.maxCol + 1):
                if board[a][b] is not None:
                    if board[a][b].identity[0] != self.identity[0]:
                        if board[a][b].checkMove(self.row, self.col, board):
                            return True

        return False

    def _moveUnderAttack(self, rowArg: int, colArg: int, board: list) -> bool:
        for a in range(Dimension.maxRow + 1):
            for b in range(Dimension.maxCol + 1):
                if board[a][b]:
                    if board[a][b].identity[0] != self.identity[0]:
                        if board[a][b].checkMove(rowArg, colArg, board):
                            return True

        return False

