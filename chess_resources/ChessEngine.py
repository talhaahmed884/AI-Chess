# Responsible for storing all the information for storing the current game state of the game. It will also be
# responsible for determining the valid moves at the current state, it will also keep a move log

from chess_resources.Classes.Bishop import Bishop
from chess_resources.Classes.Dimension import Dimension
from chess_resources.Classes.King import King
from chess_resources.Classes.Knight import Knight
from chess_resources.Classes.Pawn import Pawn
from chess_resources.Classes.Queen import Queen
from chess_resources.Classes.Rook import Rook


class Move:
    def __init__(self, start: tuple(), target: tuple(), board: list):
        self.startSQ = start
        self.targetSQ = target

        self.pieceMoved = board[self.startSQ[0]][self.startSQ[1]]
        self.pieceCaptured = board[self.targetSQ[0]][self.targetSQ[1]]


class GameState:
    board = [
        [Rook(0, 0, 'bR'), Knight(0, 1, 'bN'), Bishop(0, 2, 'bB'), Queen(0, 3, 'bQ'), King(0, 4, 'bK'),
         Bishop(0, 5, 'bB'), Knight(0, 6, 'bN'), Rook(0, 7, 'bR')],
        [Pawn(1, 0, 'bP'), Pawn(1, 1, 'bP'), Pawn(1, 2, 'bP'), Pawn(1, 3, 'bP'), Pawn(1, 4, 'bP'), Pawn(1, 5, 'bP'),
         Pawn(1, 6, 'bP'), Pawn(1, 7, 'bP')],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [Pawn(6, 0, 'wP'), Pawn(6, 1, 'wP'), Pawn(6, 2, 'wP'), Pawn(6, 3, 'wP'), Pawn(6, 4, 'wP'), Pawn(6, 5, 'wP'),
         Pawn(6, 6, 'wP'), Pawn(6, 7, 'wP')],
        [Rook(7, 0, 'wR'), Knight(7, 1, 'wN'), Bishop(7, 2, 'wB'), Queen(7, 3, 'wQ'), King(7, 4, 'wK'),
         Bishop(7, 5, 'wB'), Knight(7, 6, 'wN'), Rook(7, 7, 'wR')]
    ]

    whiteToMove = True
    moveLog = []

    def makeMove(self, move: Move):
        if self.board[move.startSQ[0]][move.startSQ[1]] is not None:
            if (self.whiteToMove and self.board[move.startSQ[0]][move.startSQ[1]].identity[0] == 'b') or (
                    not self.whiteToMove and self.board[move.startSQ[0]][move.startSQ[1]].identity[0] == 'w'):
                return
            else:
                if self.board[move.startSQ[0]][move.startSQ[1]].checkMove(move.targetSQ[0], move.targetSQ[1],
                                                                          self.board):
                    self.board[move.startSQ[0]][move.startSQ[1]] = None
                    self.board[move.targetSQ[0]][move.targetSQ[1]] = move.pieceMoved
                    self.board[move.targetSQ[0]][move.targetSQ[1]].row = move.targetSQ[0]
                    self.board[move.targetSQ[0]][move.targetSQ[1]].col = move.targetSQ[1]
                    self.moveLog.append(move)
                    self.whiteToMove = not self.whiteToMove

    def undoMove(self):
        if self.moveLog:
            move = self.moveLog.pop()
            self.board[move.startSQ[0]][move.startSQ[1]] = move.pieceMoved
            self.board[move.targetSQ[0]][move.targetSQ[1]] = move.pieceCaptured

            self.board[move.startSQ[0]][move.startSQ[1]].row = move.startSQ[0]
            self.board[move.startSQ[0]][move.startSQ[1]].col = move.startSQ[1]

            self.whiteToMove = not self.whiteToMove

    def possibleMoves(self, currPos: tuple):
        if self.board[currPos[0]][currPos[1]] is not None:
            if (self.whiteToMove and self.board[currPos[0]][currPos[1]].identity[0] == 'b') or (
                    not self.whiteToMove and self.board[currPos[0]][currPos[1]].identity[0] == 'w'):
                return
            else:
                possibleMovesList = []
                for a in range(Dimension.maxRow + 1):
                    for b in range(Dimension.maxCol + 1):
                        if self.board[currPos[0]][currPos[1]].checkMove(a, b, self.board):
                            possibleMovesList.append((a, b))

                return possibleMovesList

