import random
import sys

from chess_resources.ChessEngine import GameState, Move, _getKingPosition

scores_dict = {"Q": 9, "R": 5, "B": 3, "N": 3, "P": 1, "K": 0}
DEPTH = 2


def evaluateBoard(gs: GameState) -> int:
    score = 0
    if gs.isCheckMate():
        print("CHECKMATE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        if gs.whiteToMove:
            return -sys.maxsize  # Black Wins
        else:
            return sys.maxsize  # White Wins
    wKing, bKing = _getKingPosition(gs.board)
    if wKing.isCheck(gs.board):
        return -15
    elif bKing.isCheck(gs.board):
        return 15
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
        # print("GREEDY MOVE: ", gs.board[move.targetSQ[0]][move.targetSQ[1]].identity, "-> MOVES: ", move.startSQ,
        #       "--->", move.targetSQ, "SCORE: ", score)

        if score > maxBoardVal:
            maxBoardVal = score
        gs.undoMove(False)

    return maxBoardVal


def findBestMove(gs):
    bestMovesList = findMinMaxMove(gs, 2, -sys.maxsize, sys.maxsize, gs.whiteToMove, [])[1]
    bestMove = None
    # print()
    # print("_____________________________________BEST MOVE LIST_________________________________________________")
    maxScore = -sys.maxsize
    if len(bestMovesList) > 1:
        for move in bestMovesList:
            # print("One of the best moves: ", gs.board[move.startSQ[0]][move.startSQ[1]].identity, move.startSQ, "-->",
            #       move.targetSQ)
            gs.makeMove(move, False)
            checkOnTheseMoves = gs.getAllPossibleMovesOfASide()
            score = findGreedyMove(gs, checkOnTheseMoves, gs.whiteToMove)
            if score >= maxScore:
                maxScore = score
                bestMove = move
            gs.undoMove(False)

        if maxScore == -sys.maxsize:
            bestMove = bestMovesList[0]
    elif len(bestMovesList) == 1:
        bestMove = bestMovesList[0]
    else:
        print("NO POSSIBLE MOVES FOUND")
        return None

    # bestMove = findRandomMove(bestMovesList)
    print(bestMove.startSQ, bestMove.targetSQ)
    gs.makeMove(bestMove)
    # print("=====> SCORE FOR THESE MOVES ARE: ", evaluateBoard(gs))
    return bestMove


def findMinMaxMove(gs: GameState, depth: int, alpha, beta, isWhiteTurn: bool, bestMoves: list) -> int:
    if depth == 0 or gs.isCheckMate():
        return evaluateBoard(gs), []
    if isWhiteTurn:  # Will try to maximize the score for white
        maxScore = -sys.maxsize
        allWhiteMoves = gs.getAllPossibleMovesOfASide()
        bestMoves = []
        # print()
        # print("---------------------------------------------------------------------------------------------------------")
        for move in allWhiteMoves:
            gs.makeMove(move)
            score = findMinMaxMove(gs, depth - 1, alpha, beta, False, bestMoves)[0]
            # print("WHITE: ", "MOVES: ", gs.board[move.targetSQ[0]][move.targetSQ[1]].identity ,move.startSQ, "--->", move.targetSQ, "SCORE: ", score)
            if score >= maxScore:
                if depth == DEPTH:
                    if maxScore == score:
                        bestMoves.append(move)
                    else:
                        bestMove = []
                        bestMoves.append(move)
                maxScore = score
            alpha = max(alpha, score)
            gs.undoMove()

            if beta <= alpha:
                break
        # print("-------------------------------WHITE LOOP ENDS HERE----------------------------------------")
        # if bestMoves:
        #     print("WHITE: ", "BESTT MOVE FOR THIS LOOP ITERATION: ", bestMoves[0].startSQ, "--->",
        #       bestMoves[0].targetSQ, "SCORE: ", maxScore)

        return maxScore, bestMoves
    else:
        minScore = sys.maxsize
        allBlackMoves = gs.getAllPossibleMovesOfASide()
        bestMoves = []
        # print()
        # print("---------------------------------------------------------------------------------------------------------")
        for move in allBlackMoves:
            gs.makeMove(move)
            # print("BLACK OF DEPTH: ", depth, " TRIES A MOVE: ", gs.board[move.targetSQ[0]][move.targetSQ[1]].identity,
            #       move.startSQ, "--->", move.targetSQ)
            score = findMinMaxMove(gs, depth - 1, alpha, beta, True, bestMoves)[0]
            # print("WHITES RESPONSE FOR THIS MOVE HAS SCORE: ", score)
            # print()

            if score <= minScore:
                if depth == DEPTH:
                    if minScore == score:
                        bestMoves.append(move)
                    else:
                        bestMoves = [move]
                minScore = score

            beta = min(beta, score)
            gs.undoMove()

            if beta <= alpha:
                break
        # print("-------------------------------BLACK LOOP ENDS HERE----------------------------------------")
        # if bestMoves:
        #     print("BLACK: ", "BESTT MOVE FOR THIS LOOP ITERATION: ", bestMoves[0].startSQ, "--->",
        #           bestMoves[0].targetSQ, "SCORE: ", minScore)

        return minScore, bestMoves
