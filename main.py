from Pawn import Pawn

if __name__ == '__main__':
    pawn = Pawn(0, 0)
    print(pawn)
    print(pawn.row, pawn.col)

    pawn.row = 1
    pawn.col = 1

    print(pawn)
    print(pawn.row, pawn.col)
