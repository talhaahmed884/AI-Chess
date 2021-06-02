'''
This is UNIVERSITY KA CODE

YOU CAN SKIP THIS BAISHAK CLOSE THIS SECTION CUZ IDK KHAIR COULD BE USED FOR HELP
'''

'''
import copy
import math
import random
import sys


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in board:
        for j in i:
            if j:
                count += 1
    if count % 2 != 0:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = set()
    board_len = len(board)
    for i in range(board_len):
        for j in range(board_len):
            if board[i][j] == EMPTY:
                res.add((i, j))
    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    curr_player = player(board)
    result_board = copy.deepcopy(board)
    (i, j) = action
    result_board[i][j] = curr_player
    return result_board


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_val = winner(board)
    if winner_val == X:
        return 1
    elif winner_val == O:
        return -1
    return 0


def minimax(board):
    if board == initial_state():
        res = set()
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        res.add((row, col))
        return res

    elif player(board) == 'X':
        v = -sys.maxsize
        reqAction = None
        for action in actions(board):
            min = min_value(result(board, action))
            if min > v:
                v = min
                reqAction = action
        return reqAction
    else:
        v = sys.maxsize
        reqAction = None
        for action in actions(board):
            max = max_value(result(board, action))
            if max < v:
                v = max
                reqAction = action
        return reqAction

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -sys.maxsize
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = sys.maxsize
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


if __name__ == "__main__":
    user = None
    board = initial_state()
    ai_turn = False
    print("Choose a player")
    user = input()
    while True:
        game_over = terminal(board)
        playr = player(board)
        if game_over:
            winner = winner(board)
            if winner is None:
                print("Game Over: Tie.")
            else:
                print(f"Game Over: {winner} wins.")
            break;

        else:

            if user != playr and not game_over:
                if ai_turn:
                    move = minimax(board)
                    board = result(board, move)
                    ai_turn = False
                    print(board)


            elif user == playr and not game_over:

                ai_turn = True
                print("Enter the position to move (row,col)")
                i = int(input("Row:"))
                j = int(input("Col:"))
                if board[i][j] == EMPTY:
                    board = result(board, (i, j))
                    print(board)

'''

'''
THIS IS THE VIDEOS CODE THAT I SENT YOU 11 MINS WALLI
'''
'''
def minimax(position, depth, maximizingPLayer):
    if depth == or gameOver in position:
        return ScoreBoard(gs)

    if maximizingPLayer:
        maxEval = -infinity
        for child in position:
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval

    else:
        minEval = +infinity
        for child in position:
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval
'''

'''
THIS IS THE ALGO I THOUGHT OF BUT I DONT THIS THIS IS CORRECT COMPARE KARLO WITH ABOVE ALGOS, 
PROBLEM IS THERE ARE 2 LOOPS HERE AND I DONT GET WHY THE OTHER ALGOS ARENT USING THESE 2 LOOPS
'''
# def minimax(gs, depth, isWhiteTurn):
#     if depth == 0 or if checkMate is true:
#         return the evaluation of the board
#
#     score = -infinity
#     if its isWhiteTurn:
#         for all the pieces of white in the current game state:
#             for moves in all the moves that this piece can play:
#                 play move
#                 score = minimax(gs, depth - 1, False)
#                 if the score > max:
#                     max == score
#                     if depth == the depth of the branches we specified:
#                         save this move
#
#     else:
#         vice versa for black


'''
THIS IS US BANDAY KI VIDEO KA CODE THAT WE ARE FOLLOWING THE ONE WE USED TO MAKE THE BOARD TOO 
THIS WORKS FINE BUT A) PLEDGE AND B) IM NOT SURE IF I IMPLEMENTED THIS CORRECTLY OR IF THE ALGO IS WORKING CORRECTLY
'''


def ScoreTheBoard(gs):
    score = 0
    # if gs.CheckMate:
    #     if gs.whiteToMove:
    #         return -sys.maxsize  # Black Wins
    #     else:
    #         return sys.maxsize
    # elif gs.StaleMate:
    #     return 0
    for row in gs.board:
        for piece in row:
            if piece:
                score += scores_dict[piece.identity[1]] if piece.identity[0] == 'w' else -scores_dict[piece.identity[1]]
    return score


def findBestMoveMinMax(gs, valid_moves):
    global nextMove
    nextMove = None
    print()
    _MinimaxFunc(gs, valid_moves, 2, gs.whiteToMove)
    print()
    print("================> THE NEXT MOVE OF THE PLAYER IS: ", nextMove)
    return nextMove


def _MinimaxFunc(gs, valid_movesList, depth, player_IsWhite):
    global nextMove
    if depth == 0:
        return ScoreTheBoard(gs)
    if player_IsWhite:
        maxScore = -sys.maxsize - 1
        for move in valid_movesList:
            gs.makeMove(move)
            moveList = gs.getAllPossibleMovesOfASide()
            score = _MinimaxFunc(gs, moveList, depth - 1, False)
            print("White Back From Recursive Calls Score is: ", score)
            if score >= maxScore:
                maxScore = score
                if depth == DEPTH:
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print("SETTING THE MOVE OF THE PLAYER TO: ", move.startSQ, " --> ", move.targetSQ)
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    nextMove = move
            gs.undoMove()
        print("--------------------------------------END OF WHITE LOOP------------------------------------------------")
        return maxScore

    else:
        minScore = sys.maxsize
        selected_move = None
        for move in valid_movesList:
            print("BLACK: Move: ", move.startSQ, " --> ", move.targetSQ, " DEPTH: ", depth)
            gs.makeMove(move)
            moveList = gs.getAllPossibleMovesOfASide()
            copyDepth = depth
            score = _MinimaxFunc(gs, moveList, copyDepth - 1, True)
            print("Black Back From Recursive Calls Score is: ", score)
            if score <= minScore:
                minScore = score
                if depth == DEPTH:
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print("SETTING THE MOVE OF THE PLAYER TO: ", move.startSQ, " --> ", move.targetSQ)
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    nextMove = move
            gs.undoMove()
        print("--------------------------------------END OF BLACK LOOP------------------------------------------------")
        return minScore
