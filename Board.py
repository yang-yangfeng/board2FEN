from Piece import Piece

class Board:
    def __init__(self, wtomove=True, castles='KQkq', enpst='-', halfmv=0,fullmv=1):
        #8x8 grid initialized with nulls
        #grid[row][col] is the piece at square {col}row where {col} is the mapping
        #   1 -> A, 2 -> B, etc.
        self.grid = [[None for _ in range(0,9)] for _ in range(0,9)]
        self.setMove(wtomove)
        self.setCastles(castles)
        self.setenpst(enpst)
        self.sethalfmv(halfmv)
        self.setfullmv(fullmv)

    def removePiece(self, row, col):
        assert 1 <= row <= 8 and 1 <= col <= 8
        self.grid[row][col] = None

    def clearPieces(self):
        self.grid = [[None for _ in range(0,9)] for _ in range(0,9)]

    def addPiece(self, piecetype, color, row, col):
        assert 1 <= row <= 8 and 1 <= col <= 8
        p = Piece(piecetype, color)
        self.grid[row][col] = p

    def getPiece(self, row, col):
        assert 1 <= row <= 8 and 1 <= col <= 8
        return self.grid[row][col]

    def setMove(self, wtomove=True):
        self.wtomove = wtomove

    #castles is a string (e.g. KQk) describing castles available in the format
    #in which it appears in the FEN notation
    def setCastles(self, castles='KQkq'):
        self.castles = castles

    #set enpassant square string as it appears in FEN notation
    def setenpst(self, enpst='-'):
        self.enpst = enpst

    def sethalfmv(self, halfmv=0):
        self.halfmv = halfmv

    def setfullmv(self, fullmv=1):
        self.fullmv = fullmv

    def rowstring(self, row):
        ret = ''
        count = 0
        for i in range(1,9):
            piece = self.grid[row][i]
            if piece is None:
                count += 1
            else:
                if count > 0:
                    ret += str(count)
                    count = 0
                ret += piece.getFenChar()
        if count > 0:
            ret += str(count)
        return ret

    def fen(self):
        ret = self.rowstring(8)
        for i in range(7,0,-1):
            ret += '/'
            ret += self.rowstring(i)

        if self.wtomove:
            ret += ' w '
        else:
            ret += ' b '

        ret += self.castles
        ret += ' '
        ret += self.enpst
        ret += ' '
        ret += str(self.halfmv)
        ret += ' '
        ret += str(self.fullmv)
        return ret



if __name__ == '__main__':
    print 'hi'
