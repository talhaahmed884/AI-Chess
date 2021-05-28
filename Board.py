import enum


class Dimension(enum.Enum):
    maxRow = maxCol = 7
    minRow = minCol = 0


class Board:
    def __init__(self):
        self.pieces = [[]]
