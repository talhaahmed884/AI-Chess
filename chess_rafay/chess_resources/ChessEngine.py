# Responsible for storing all the information for storing the current game state of the game. It will also be
# responsible for determining the valid moves at the current state, it will also keep a move log
import copy
from collections import defaultdict

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


def _movement(move: Move, board: list):
    board[move.startSQ[0]][move.startSQ[1]] = None
    board[move.targetSQ[0]][move.targetSQ[1]] = move.pieceMoved
    board[move.targetSQ[0]][move.targetSQ[1]].row = move.targetSQ[0]
    board[move.targetSQ[0]][move.targetSQ[1]].col = move.targetSQ[1]


def _getKingPosition(board: list) -> (King, King):
    wKing = bKing = None

    for a in range(0, Dimension.maxRow + 1):
        for b in range(0, Dimension.maxCol + 1):
            if isinstance(board[a][b], King):
                if board[a][b].identity[0] == 'w':
                    wKing = board[a][b]
                elif board[a][b].identity[0] == 'b':
                    bKing = board[a][b]

    return wKing, bKing


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
            if self.board[move.startSQ[0]][move.startSQ[1]] is not None:
                if (self.whiteToMove and self.board[move.startSQ[0]][move.startSQ[1]].identity[0] == 'b') or (
                        not self.whiteToMove and self.board[move.startSQ[0]][move.startSQ[1]].identity[0] == 'w'):
                    return
            if self.board[move.startSQ[0]][move.startSQ[1]].checkMove(move.targetSQ[0], move.targetSQ[1],
                                                                      self.board):
                _movement(move, self.board)
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
                wKing, bKing = _getKingPosition(self.board)
                return self.getPinningMoves(wKing, bKing, currPos)

    def _getAllPossibleMoves(self, currPos: tuple) -> list:
        possibleMovesList = []
        for a in range(Dimension.maxRow + 1):
            for b in range(Dimension.maxCol + 1):
                if self.board[currPos[0]][currPos[1]].checkMove(a, b, self.board):
                    possibleMovesList.append((a, b))
        return possibleMovesList

    def getAllPossibleMovesOfASide(self):
        # all moves is type MOVE
        all_moves = []
        for r in range(8):
            for c in range(8):
                if self.board[r][c]:
                    turn = self.board[r][c].identity[0]
                    if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                        target_moves = self.possibleMoves((r, c))
                        for tm in target_moves:
                            move = Move((r, c), tm, self.board)
                            all_moves.append(move)
        return all_moves

    def getPinningMoves(self, wKing, bKing, currPos: tuple) -> list:
        if wKing.isCheck(self.board):
            identity = 'w'
        elif bKing.isCheck(self.board):
            identity = 'b'
        else:
            if self.whiteToMove and self.board[currPos[0]][currPos[1]].identity[0] == 'w':
                identity = 'w'
            elif not self.whiteToMove and self.board[currPos[0]][currPos[1]].identity[0] == 'b':
                identity = 'b'

        pinningMoves = []

        if self.board[currPos[0]][currPos[1]].identity[0] == identity:
            possibleMoves = self._getAllPossibleMoves((currPos[0], currPos[1]))

            if possibleMoves:
                for c in possibleMoves:
                    newBoard = copy.deepcopy(self.board)
                    _movement(Move((currPos[0], currPos[1]), (c[0], c[1]), newBoard), newBoard)
                    twKing, tbKing = _getKingPosition(newBoard)
                    if identity == 'w' and not twKing.isCheck(newBoard):
                        pinningMoves.append(c)
                    elif identity == 'b' and not tbKing.isCheck(newBoard):
                        pinningMoves.append(c)

        return pinningMoves

    def isCheckMate(self) -> bool:
        wKing, bKing = _getKingPosition(self.board)
        tKing = None

        if wKing.isCheck(self.board):
            tKing = wKing
        elif bKing.isCheck(self.board):
            tKing = bKing

        if tKing is not None:
            for a in range(0, Dimension.maxRow + 1):
                for b in range(0, Dimension.maxCol + 1):
                    if self.board[a][b] is not None:
                        if self.board[a][b].identity[0] == tKing.identity[0]:
                            possibleBlockingMoves = self._getAllPossibleMoves((a, b))

                            for c in possibleBlockingMoves:
                                newBoard = copy.deepcopy(self.board)
                                _movement(Move((a, b), (c[0], c[1]), newBoard), newBoard)

                                if not tKing.isCheck(newBoard):
                                    return False

            print('CHECKMATE HAS OCCURRED')
            return True
