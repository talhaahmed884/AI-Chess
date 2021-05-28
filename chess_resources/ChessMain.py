# The driver file, responsible for handling the user input and the current GameState object
import pygame as p
import numpy as np
from chess_resources import ChessEngine

width = height = 624  # 400 is another option
dimension = 8  # Dimensions of a chess board are 8x8
sq_size = height // dimension
max_FPS = 15  # For animation
images = {}  # Dictionary of images


# Initialize a global dictionary of images. This will be called exactly once in the main
def load_images():
    for piece in ['wP', 'wR', 'wB', 'wN', 'wQ', 'wK', 'bP', 'bR', 'bB', 'bN', 'bQ', 'bK']:
        images[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (sq_size, sq_size))
    # we can access an image by 'Images['wP']'


# Helping Methods
def drawBoard(screen):
    # Only drawing the dark squares as the light color is the background
    for row in range(dimension):
        for col in range(dimension):
            if (row + col) % 2:
                p.draw.rect(screen, p.Color("#33684B"), p.Rect(col * sq_size, row * sq_size, sq_size, sq_size))


def drawPieces(screen, _board: np.array([])):
    for row in range(dimension):
        for col in range(dimension):
            piece = _board[row][col]
            # not an empty square
            if piece != "--":
                screen.blit(images[piece], p.Rect(col * sq_size, row * sq_size, sq_size, sq_size))


# Responsible for all the graphics within a current game state.
def drawGameState(screen, gs: ChessEngine.GameState()):
    drawBoard(screen)  # draw squares on the board
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
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        drawGameState(screen, gs)
        clock.tick(max_FPS)
        p.display.flip()


if __name__ == "__main__":
    main()
