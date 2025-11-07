'''
Game class to manage the game loop, handle events, and update the game state.
'''
import pygame
from paddle import Paddle
from ball import Ball
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.paddle1 = Paddle(30, 300)
        self.paddle2 = Paddle(770, 300)
        self.ball = Ball(400, 300)
        self.score1 = 0
        self.score2 = 0
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.paddle1.move(up=True)
        if keys[pygame.K_s]:
            self.paddle1.move(up=False)
        if keys[pygame.K_UP]:
            self.paddle2.move(up=True)
        if keys[pygame.K_DOWN]:
            self.paddle2.move(up=False)
        self.ball.move()
        self.check_collisions()
    def check_collisions(self):
        if self.ball.rect.colliderect(self.paddle1.rect) or self.ball.rect.colliderect(self.paddle2.rect):
            self.ball.bounce()
        if self.ball.rect.left <= 0:
            self.score2 += 1
            self.ball.reset()
        if self.ball.rect.right >= 800:
            self.score1 += 1
            self.ball.reset()
    def render(self):
        self.screen.fill((0, 0, 0))
        self.paddle1.render(self.screen)
        self.paddle2.render(self.screen)
        self.ball.render(self.screen)
        font = pygame.font.Font(None, 74)
        text = font.render(str(self.score1), 1, (255, 255, 255))
        self.screen.blit(text, (250, 10))
        text = font.render(str(self.score2), 1, (255, 255, 255))
        self.screen.blit(text, (520, 10))