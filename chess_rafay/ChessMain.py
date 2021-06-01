# The driver file, responsible for handling the user input and the current GameState object
import random
import sys

import pygame as p

from chess_resources import ChessEngine, AI_Bot
import chess_resources.AI_Bot
from chess_resources.ChessEngine import Move

width = height = 512  # 400 is another option
dimension = 8  # Dimensions of a chess board are 8x8
sq_size = height // dimension
max_FPS = 15  # For animation
images = {}  # Dictionary of images


# Initialize a global dictionary of images. This will be called exactly once in the main
def load_images():
    for piece in ['wP', 'wR', 'wB', 'wN', 'wQ', 'wK', 'bP', 'bR', 'bB', 'bN', 'bQ', 'bK']:
        images[piece] = p.transform.scale(p.image.load("chess_resources/images/" + piece + ".png"), (sq_size, sq_size))
    # we can access an image by 'Images['wP']'


# Helping Methods
def drawBoard(screen, selected_pos: tuple, allMoves: list):
    # Only drawing the dark squares as the light color is the background
    colors = ["#E7E8E4", "#33684B"]
    highlightedColors = ["#FF6E5E", "#D34437"]
    for row in range(dimension):
        for col in range(dimension):
            color = colors[(row + col) % 2]
            if selected_pos and (row, col) == selected_pos:
                color = "#9B4139"

            if allMoves and (row, col) in allMoves:
                allMoves.pop(0)
                color = highlightedColors[(row + col) % 2]
            p.draw.rect(screen, p.Color(color), p.Rect(col * sq_size, row * sq_size, sq_size, sq_size))


def drawPieces(screen, _board: list):
    for row in range(dimension):
        for col in range(dimension):
            piece = _board[row][col]
            # not an empty square
            if piece is not None:
                screen.blit(images[piece.identity], p.Rect(col * sq_size, row * sq_size, sq_size, sq_size))
            if col == 0:
                font = p.font.SysFont("Sans-serif", 20, True, False)
                textObject = font.render(str(row), 0, p.Color('#FF0000'))
                textLocation = p.Rect(col * sq_size, row * sq_size, 20, 20).move(20 / 2 - textObject.get_width() / 2,
                                                                20 / 2 - textObject.get_height() / 2)
                screen.blit(textObject, textLocation)
            if row == 0:
                font = p.font.SysFont("Sans-serif", 20, True, False)
                textObject = font.render(str(col), 0, p.Color('#FF0000'))
                textLocation = p.Rect(col * sq_size, row * sq_size, 20, 20).move(20 / 2 - textObject.get_width() / 2,
                                                                                 20 / 2 - textObject.get_height() / 2)
                screen.blit(textObject, textLocation)


def drawText(screen, text: str):
    font = p.font.SysFont("Sans-serif", 75, True, False)
    textObject = font.render(text, 0, p.Color('#404040'))
    textLocation = p.Rect(0, 0, width, height).move(width / 2 - textObject.get_width() / 2,
                                                    height / 2 - textObject.get_height() / 2)
    screen.blit(textObject, textLocation)


# Responsible for all the graphics within a current game state.
def drawGameState(screen, gs: ChessEngine.GameState(), selected_pos=None, allMoves=None):
    drawBoard(screen, selected_pos, allMoves)  # draw squares on the board
    # add in piece highlighting or move suggestions (later)
    drawPieces(screen, gs.board)  # draw pieces on top of those squares


# This will be our main driver for our code. This will handle user input and updating the graphics
def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    gs = ChessEngine.GameState()
    screen.fill(p.Color("#E7E8E4"))
    load_images()  # only do this once
    running = True
    sqSelected = ()  # no sq selected initially, keep track of the last click of the user tuple (row, col)
    playerClicks = []  # keep track of player clicks (two tuples: (6, 4), (4, 4))
    # Player Selects their player
    myPlayer = 'w'
    gameOver = False
    doNotDraw = False
    COUNT = 0
    while running:
        humanTurn = gs.whiteToMove if myPlayer == 'w' else not gs.whiteToMove
        # print(gs.whiteToMove, whitePlayer, blackPlayer)
        if gameOver:
            drawText(screen, "CHECKMATE")
            doNotDraw = True

        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if not gameOver and humanTurn:
                    location = p.mouse.get_pos()  # (x, y) location of mouse
                    col = location[0] // sq_size
                    row = location[1] // sq_size
                    if sqSelected == (row, col):  # user clicked the same sq twice
                        # Assumption this is undo
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected)  # append for both 1st and 2nd click
                    if len(playerClicks) == 2:  # after 2nd click
                        move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                        gs.makeMove(move)
                        if gs.isCheckMate():
                            drawText(screen, 'CHECKMATE')
                            gameOver = True

                        sqSelected = ()
                        playerClicks = []
            # Keyboard Press
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()

        if not gameOver and not humanTurn:
            choose_move = gs.getAllPossibleMovesOfASide()
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            bot_Move = AI_Bot.findBestMove(gs)

            if bot_Move is None:
                print("STRONG MOVE BY PLAYER AI TAKES A RISK")
                bot_Move = AI_Bot.findRandomMove(choose_move)

            for row in gs.board:
                for col in row:
                    if col:
                        print(col.identity, end="\t")
                    else:
                        print("--", end="\t")
                print()
            print("IS WHITE: ", gs.whiteToMove)
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX> IN MAIN FUNCTION: ", bot_Move.startSQ, " --> ", bot_Move.targetSQ)
            temp = Move(bot_Move.startSQ, bot_Move.targetSQ, gs.board)
            gs.makeMove(temp)
            print("IS WHITE: ", gs.whiteToMove)

        if len(playerClicks) == 1:
            if gs.board[sqSelected[0]][sqSelected[1]] is not None:
                highlightMoves = gs.possibleMoves(sqSelected)
                drawGameState(screen, gs, sqSelected, highlightMoves)
        elif not doNotDraw:
            drawGameState(screen, gs)

        clock.tick(max_FPS)
        p.display.flip()


if __name__ == "__main__":
    main()
