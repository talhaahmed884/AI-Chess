from abc import abstractmethod


class Piece:
    def __init__(self):
        self.row = None
        self.col = None
        self.identity = None

    @abstractmethod
    def checkMove(self, rowArg: int, colArg: int, board: list) -> bool:
        pass
