#Square class
class Square:

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    #Does the square have a piece on it
    def has_piece(self):
        return self.piece != None