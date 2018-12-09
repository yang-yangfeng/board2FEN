class Piece:

    def __init__(self, typestring, color):
        assert color.upper() in ['W','B']
        assert typestring.upper() in ['PAWN','KNIGHT','BISHOP','ROOK','QUEEN', 'KING']
        self.typestring = typestring.upper()
        self.color = color.upper()

    def isWhite(self):
        return self.color == 'W'

    def getType(self):
        return self.typestring
