import random
import sys
from chess_resources.ChessEngine import GameState, Move

scores_dict = {"Q": 9, "R": 5, "B": 3, "N": 3, "P": 1, "K": 0}
DEPTH = 3

def evaluateBoard(gs: GameState) -> int:
    score = 0
    if gs.isCheckMate():
        if gs.whiteToMove:
            return -sys.maxsize  # Black Wins
        else:
            return sys.maxsize  # White Wins
    elif gs.getAllPossibleMovesOfASide() is None:
        return 0
    for row in gs.board:
        for piece in row:
            if piece:
                score += scores_dict[piece.identity[1]] if piece.identity[0] == 'w' else -scores_dict[piece.identity[1]]
    return score


def findRandomMove(allMoves: list) -> Move:
    return allMoves[random.randint(0, len(allMoves) - 1)]
def findGreedyMove(gs: GameState) -> Move:
    turnSwitch = 1 if gs.whiteToMove else -1
    boardVal = -sys.maxsize - 1
    bestMove = None
    allMoves = gs.getAllPossibleMovesOfASide()
    for move in allMoves:
        gs.makeMove(move)
        score = turnSwitch * evaluateBoard(gs)
        if score > boardVal:
            boardVal = score
            bestMove = move
        gs.undoMove()

    return bestMove

def findBestMove(gs):
    global bestMove
    bestMove = None
    findMinmaxMove(gs, 3, -sys.maxsize, sys.maxsize, gs.whiteToMove)
    return bestMove


def findMinmaxMove(gs: GameState, depth: int, alpha, beta, isWhiteTurn: bool) -> int:
    global bestMove
    if depth == 0 or gs.isCheckMate():
        return evaluateBoard(gs)
    if isWhiteTurn:  # Will try to maximize the score for white
        maxScore = -sys.maxsize
        allWhiteMoves = gs.getAllPossibleMovesOfASide()
        for move in allWhiteMoves:
            gs.makeMove(move)
            score = findMinmaxMove(gs, depth - 1, alpha, beta, False)
            maxScore = max(maxScore, score)
            alpha = max(alpha, score)
            if maxScore == score and depth == DEPTH:
                bestMove = move
            gs.undoMove()

            if beta <= alpha:
                break
        return maxScore
    else:
        minScore = sys.maxsize
        allBlackMoves = gs.getAllPossibleMovesOfASide()
        for move in allBlackMoves:
            gs.makeMove(move)
            score = findMinmaxMove(gs, depth - 1, alpha, beta, True)
            minScore = min(minScore, score)
            beta = min(beta, score)
            if minScore == score and depth == DEPTH:
                bestMove = move
            gs.undoMove()

            if beta <= alpha:
                break
        return minScore


def findNegaMax(gs, depth, alpha, beta, turnMult):
    global nextMove
    if depth == 0:
        return turnMult * evaluateBoard(gs)

    maxScore = -sys.maxsize
    all_moves = gs.getAllPossibleMovesOfASide()
    for move in all_moves:
        gs.makeMove(move)
        score = -findNegaMax(gs, depth - 1, -beta, -alpha, -turnMult)
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move
        gs.undoMove()
        if maxScore > alpha:
            alpha = maxScore
        if alpha >= beta:
            break
    return maxScore