'''
Game class to manage the game loop, events, and state updates.
'''
import pygame
from paddle import Paddle
from ball import Ball
from score import Score
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.paddle1 = Paddle(20, 250)
        self.paddle2 = Paddle(760, 250)
        self.ball = Ball(400, 300)
        self.score = Score()
    def update(self):
        keys = pygame.key.get_pressed()
        self.paddle1.move(keys, pygame.K_w, pygame.K_s)
        self.paddle2.move(keys, pygame.K_UP, pygame.K_DOWN)
        self.ball.move(self.paddle1, self.paddle2, self.score)
    def render(self):
        self.screen.fill((0, 0, 0))
        self.paddle1.render(self.screen)
        self.paddle2.render(self.screen)
        self.ball.render(self.screen)
        self.score.render(self.screen)