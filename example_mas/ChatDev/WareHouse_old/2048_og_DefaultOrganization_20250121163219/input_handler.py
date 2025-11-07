'''
Handles user input for the 2048 game using Pygame.
'''
import pygame
class InputHandler:
    def __init__(self, game):
        self.game = game
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.game.move('UP')
            elif event.key == pygame.K_DOWN:
                self.game.move('DOWN')
            elif event.key == pygame.K_LEFT:
                self.game.move('LEFT')
            elif event.key == pygame.K_RIGHT:
                self.game.move('RIGHT')