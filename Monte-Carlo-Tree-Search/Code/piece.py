#imports
import os

#piece class
class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    #find and assign texture
    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')
        
    #draw available piece moves
    def add_moves(self, move):
        self.moves.append(move)

#Pawn class
class Pawn(Piece):

    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)

#Knight class
class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)

#Bishop class
class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.0)
    
#Rook class
class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)

#Queen class
class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)

#King class
class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, 10000.0)