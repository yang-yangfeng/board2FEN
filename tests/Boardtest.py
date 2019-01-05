from Board import Board
from random import randint

#class to keep track of squares w pieces on them
class randsquares:
    def __init__(self, board):
        self.board = board

    def randfreesq(self):
        row = randint(1,8)
        col = randint(1,8)
        #will be infinite loop if every square has a piece on it. should not happen
        #but maybe should fix
        while (self.board.getPiece(row,col) is not None):
            row = randint(1,8)
            col = randint(1,8)
        return row, col


def addpce(board, piece, color, row, col):
    board.addPiece(piece, color, row, col)
    if color.upper() == 'W':
        str1 = 'White'
    else:
        str1 = 'Black'

    if piece.upper() == 'P':
        str2 = 'Pawn'
    elif piece.upper() == 'N':
        str2 = 'Knight'
    elif piece.upper() == 'B':
        str2 = 'Bishop'
    elif piece.upper() == 'R':
        str2 = 'Rook'
    elif piece.upper() == 'Q':
        str2 = 'Queen'
    else:
        str2 = 'King'

    cols = [None,'A','B','C','D','E','F','G','H']
    print 'adding ' + str1 + ' ' + str2 + ' at ' + cols[col] + str(row)

def printfen(board):
    print 'FEN: ---'
    print board.fen()
    print '------'

def test1(board):
    rs = randsquares(board)
    #place 2 kings and 1 ranodmly colored pawn at random spot
    print '---- Test 1 ----'
    print '\n'
    board.clearPieces()
    row, col = rs.randfreesq()
    addpce(board,'K', 'W', row, col)

    row, col = rs.randfreesq()
    addpce(board,'K', 'B', row, col)

    if randint(0,1) == 0:
        c = 'W'
    else:
        c = 'B'
    row, col = rs.randfreesq()
    addpce(board,'P', c, row, col)
    printfen(board)
    print '\n'
    print '------'

    #place 2 kings and up to 8 white and up to 8 black pawns at random spots
    print '---- Test 2 ----'
    print '\n'
    board.clearPieces()
    row, col = rs.randfreesq()
    addpce(board,'K', 'W', row, col)

    row, col = rs.randfreesq()
    addpce(board,'K', 'B', row, col)
    w = randint(1,8)
    b = randint(1,8)

    for _ in range(0,w):
        row, col = rs.randfreesq()
        addpce(board,'P', 'W', row, col)

    for _ in range(0,b):
        row, col = rs.randfreesq()
        addpce(board,'P', 'B', row, col)

    printfen(board)
    print '\n'
    print '------'

    #place 2 kings and random subset of starting pieces at random places
def test2(board):
    print 'asdf'

if __name__ == '__main__':
    board = Board()
    test1(board)
