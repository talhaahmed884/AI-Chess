# Responsible for storing all the information for storing the current game state of the game. It will also be
# responsible for determining the valid moves at the current state, it will also keep a move log
import numpy as np


class Move:
    # maps keys to values
    # key : value
    # ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
    #                "5": 3, "6": 2, "7": 1, "8": 0}
    # rowsToRanks = {v: k for k, v in ranksToRows.items()}
    # filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
    #                "e": 4, "f": 5, "g": 6, "h": 7}
    # colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, start: tuple(), target: tuple(), board: np.array([])):
        self.startSQ = start
        self.targetSQ = target
        # print("start Row: ", self.startSQ[0], " start Col: ", self.startSQ[1])
        self.pieceMoved = board[self.startSQ[0]][self.startSQ[1]]
        self.pieceCaptured = board[self.targetSQ[0]][self.targetSQ[1]]

    # def getChessNotation(self):
    #     return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
    #
    # def getRankFile(self, row, col):
    #     return self.colsToFiles[col] + self.rowsToRanks[row]


class GameState:
    board = np.array([
        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    ])
    whiteToMove = True
    moveLog = []

    def makeMove(self, move: Move):
        self.board[move.startSQ[0]][move.startSQ[1]] = "--"
        self.board[move.targetSQ[0]][move.targetSQ[1]] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove
