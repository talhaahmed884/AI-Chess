# from Bishop import Bishop
# from Dimension import Dimension
# from King import King
# from Knight import Knight
# from Pawn import Pawn
# from Piece import Color
# from Queen import Queen
# from Rook import Rook
#
#
# class Board:
#     def __init__(self):
#         self.pieces = [[]]
#
#         for a in range(0, Dimension.maxRow + 1):
#             self.pieces.append([])
#             for b in range(0, Dimension.maxCol + 1):
#                 self.pieces[a].append(None)
#
#         self.initBoard()
#
#     def initBoard(self):
#         for a in range(0, Dimension.minRow + 1):
#             self.pieces[1][a] = Pawn(1, a, Color.White)
#             self.pieces[6][a] = Pawn(6, a, Color.Black)
#
#     def printBoard(self):
#         for a in range(0, Dimension.maxRow + 1):
#             for b in range(0, Dimension.maxCol + 1):
#                 if self.pieces[a][b] is None:
#                     print('--', end=' ')
#                 else:
#                     if isinstance(self.pieces[a][b], Pawn):
#                         print('P', end=' ')
#                     elif isinstance(self.pieces[a][b], Bishop):
#                         print('B', end=' ')
#                     elif isinstance(self.pieces[a][b], King):
#                         print('K', end=' ')
#                     elif isinstance(self.pieces[a][b], Knight):
#                         print('KN', end=' ')
#                     elif self.pieces[a][b] == isinstance(Queen):
#                         print('Q', end=' ')
#                     elif isinstance(self.pieces[a][b], Rook):
#                         print('R', end=' ')
#             print()
#
