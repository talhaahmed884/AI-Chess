import random

scores_dict = {"Q": 9, "R": 5, "B": 3, "N": 3, "P": 1, "K": 0}
checkmate = 1000
stalemate = 0


def findRandomMove(validMoves):
    print("-------MOVE MADE----------------")
    print()
    for v in validMoves:
        print(v.startSQ, " ---> ", v.targetSQ)
    return validMoves[random.randint(0, len(validMoves) - 1)]


'''
def findBotMove(gs, validMoves):
    max_Board_Val = 10000000
    best_move = None
    for move in validMoves:
        gs.makeMove(move)

def ScoreTheBoard(board):
    score = 0
    for row in board:
        for piece in row:
            if piece:
                if piece.identity[0] == 'w':  # White is Max
                    score += scores_dict[piece.identity[1]]
                else:  # Black is Min
                    score -= scores_dict[piece.identity[1]]
    return score

def MiniMax():
    pass
'''
