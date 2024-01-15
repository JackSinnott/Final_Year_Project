#imports
import pygame
import sys

from const import *
from game import Game
from square import Square
from move import Move

#loop
class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Monte Carlo Chess')
        self.game = Game()

    def mainloop(self):       
        game = self.game
        screen = self.screen
        board = self.game.board
        dragger = self.game.dragger

        while True:
            game.draw_bg(screen)
            game.draw_moves(screen)
            game.draw_pieces(screen)
             
            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    #convert to board space
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        board.cal_moves(piece, clicked_row, clicked_col)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        game.draw_bg(screen)
                        game.draw_moves(screen)
                        game.draw_pieces(screen)

                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.draw_bg(screen)
                        game.draw_moves(screen)
                        game.draw_pieces(screen)
                        dragger.update_blit(screen)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        if board.valid_move(dragger.piece, move):
                            board.move(dragger.piece, move)
                            game.draw_bg(screen)
                            game.draw_pieces(screen)
                    
                    dragger.undrag_piece()    


                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

            pygame.display.update()

#calls
main = Main()
main.mainloop()