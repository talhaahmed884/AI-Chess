import copy
import random
import sys

from chess_resources.ChessEngine import GameState, Move, _getKingPosition

scores_dict = {"Q": 9, "R": 5, "B": 3, "N": 3, "P": 1, "K": 0}
DEPTH = 2


def evaluateBoard(gs: GameState) -> int:
    score = 0
    if gs.isCheckMate():
        if gs.whiteToMove:
            return -sys.maxsize  # Black Wins
        else:
            return sys.maxsize  # White Wins
    wKing, bKing = _getKingPosition(gs.board)
    if wKing.isCheck(gs.board):
        return -2
    elif bKing.isCheck(gs.board):
        return 2
    elif gs.getAllPossibleMovesOfASide() is None:
        return 0
    for row in gs.board:
        for piece in row:
            if piece:
                score += scores_dict[piece.identity[1]] if piece.identity[0] == 'w' else -scores_dict[piece.identity[1]]
    return score


def findRandomMove(allMoves: list) -> Move:
    return allMoves[random.randint(0, len(allMoves) - 1)]


def findGreedyMove(gs: GameState, checkOnTheseMoves: list, isWhite: bool) -> Move:
    turnSwitch = 1 if isWhite else -1
    maxBoardVal = -sys.maxsize - 1
    for move in checkOnTheseMoves:
        gs.makeMove(move, False)
        score = turnSwitch * evaluateBoard(gs)
        # # #print"GREEDY MOVE: ", gs.board[move.targetSQ[0]][move.targetSQ[1]].identity, "-> MOVES: ", move.startSQ,
        #       "--->", move.targetSQ, "SCORE: ", score)
        if score > maxBoardVal:
            maxBoardVal = score
        gs.undoMove(False)

    return maxBoardVal


def findBestMove(gs, opening = False):
    #print("\n\n************NEW MOVE*************************NEW MOVE**********************NEW MOVE*************************NEW MOVE************************\n")
    bestMovesList = findMinMaxMove(gs, 2, -sys.maxsize, sys.maxsize, gs.whiteToMove, [])[1]                             # Get best moves from min max
    bestMovesList2 = []
    maxScore = -sys.maxsize
    if len(bestMovesList) > 1:
        print("---------------------------")
        for move in bestMovesList:
            gs.makeMove(move, False)
            checkOnTheseMoves = gs.getAllPossibleMovesOfASide()
            score = findGreedyMove(gs, checkOnTheseMoves, gs.whiteToMove)                                               # get greedy score
            if score >= maxScore:
                maxScore = score
                bestMovesList2.append(move)                                                                             # append these moves in another list
            gs.undoMove(False)

        if maxScore == -sys.maxsize:
            bestMovesList2 = [findRandomMove(bestMovesList)]
    elif len(bestMovesList) == 1:
        bestMovesList2 = [bestMovesList[0]]
    else:
        #print("NO POSSIBLE MOVES FOUND")
        return None
    for b in bestMovesList2:
        print(b.pieceMoved.identity, b.startSQ, b.targetSQ)
    bestMove_ = findRandomMove(bestMovesList2)                                                                          # get random move from bestest move list
    # in case of a duplicate move I calculate move again by randomizing it
    if len(gs.moveLog) >= 4:
        for m in range(2):
            if bestMove_.startSQ == gs.moveLog[-2 * (m+1)].startSQ and bestMove_.targetSQ == gs.moveLog[-2 * (m+1)].targetSQ:
                #print("=======================>>>>>>> MOVE DUPLICATED MULTIPLE TIMES")
                bestMove_ = findRandomMove(bestMovesList)

    gs.makeMove(bestMove_)
    return bestMove_


def findMinMaxMove(gs: GameState, depth: int, alpha, beta, isWhiteTurn: bool, bestMoves: list) -> int:
    if depth == 0 or gs.isCheckMate():
        return evaluateBoard(gs), []
    if isWhiteTurn:  # Will try to maximize the score for white
        maxScore = -sys.maxsize
        allWhiteMoves = gs.getAllPossibleMovesOfASide()
        bestMoves = []
        #print("---------------------------------------------------------------------------------------------------------")
        for move in allWhiteMoves:
            gs.makeMove(move)
            #print("WHITE OF DEPTH: ", depth, " TRIES A MOVE: ", gs.board[move.targetSQ[0]][move.targetSQ[1]].identity, move.startSQ, "--->", move.targetSQ)
            score = findMinMaxMove(gs, depth - 1, alpha, beta, False, bestMoves)[0]
            #print("BLACK RESPONSE FOR THIS MOVE HAS SCORE: ", score)
            #print("WHITE: ", "MOVES: ", gs.board[move.targetSQ[0]][move.targetSQ[1]].identity ,move.startSQ, "--->", move.targetSQ, "SCORE: ", score)
            if depth == DEPTH and score >= maxScore:
                if maxScore == score:
                    bestMoves.append(move)
                else:
                    bestMoves = [move]
            maxScore = max(maxScore, score)
            alpha = max(alpha, maxScore)
            gs.undoMove()
            if beta <= alpha:
                #print("WHITE: BREAKING CUZ OF AB PRUNING IN WHITE")
                break
        #print("-------------------------------WHITE LOOP ENDS HERE----------------------------------------")
        # if bestMoves:
            #print("WHITE: ", "BESTT MOVE FOR THIS LOOP ITERATION: ", bestMoves[0].startSQ, "--->", bestMoves[0].targetSQ, "SCORE: ", maxScore)

        return maxScore, bestMoves
    else:
        minScore = sys.maxsize
        allBlackMoves = gs.getAllPossibleMovesOfASide()
        bestMoves = []
        #print("---------------------------------------------------------------------------------------------------------")
        for move in allBlackMoves:
            gs.makeMove(move)
            #print("BLACK OF DEPTH: ", depth, " TRIES A MOVE: ", gs.board[move.targetSQ[0]][move.targetSQ[1]].identity, move.startSQ, "--->", move.targetSQ)
            score = findMinMaxMove(gs, depth - 1, alpha, beta, True, bestMoves)[0]
            #print("WHITES RESPONSE FOR THIS MOVE HAS SCORE: ", score)
            if depth == DEPTH and score <= minScore:
                if minScore == score:
                    bestMoves.append(move)
                else:
                    bestMoves = [move]
            minScore = min(minScore, score)
            beta = min(beta, minScore)
            gs.undoMove()
            if beta <= alpha:
                #print("BLACK: BREAKING CUZ OF AB PRUNING IN BLACK")
                break
        #print("-------------------------------BLACK LOOP ENDS HERE----------------------------------------")
        # if bestMoves:
            #print("BLACK: ", "BESTT MOVE FOR THIS LOOP ITERATION: ", bestMoves[0].startSQ, "--->", bestMoves[0].targetSQ, "SCORE: ", minScore)

        return minScore, bestMoves
