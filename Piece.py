class Piece:

    def __init__(self, typestring, color):
        assert color.upper() in ['W','B']
        assert typestring.upper() in ['P','N','B','R','Q', 'K']
        self.typestring = typestring.upper()
        self.color = color.upper()

    def isWhite(self):
        return self.color == 'W'

    def getFenChar(self):
        if self.isWhite():
            return self.typestring.upper()
        else:
            return self.typestring.lower()

    def __str__(self):
        if self.isWhite():
            str1 = 'White'
        else:
            str1 = 'Black'

        if self.typestring == 'P':
            str2 = 'Pawn'
        elif self.typestring == 'N':
            str2 = 'Knight'
        elif self.typestring == 'B':
            str2 = 'Bishop'
        elif self.typestring == 'R':
            str2 = 'Rook'
        elif self.typestring == 'Q':
            str2 = 'Queen'
        else:
            str2 = 'King'

        return str1 + ' ' + str2
        
