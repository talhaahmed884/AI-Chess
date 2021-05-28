from abc import abstractmethod

import Board


class Piece:
    def __init__(self):
        self.row = None
        self.col = None
        self.color = None

    @abstractmethod
    def checkMove(self, row: int, col: int, rowArg: int, colArg: int, board: Board) -> bool:
        pass
