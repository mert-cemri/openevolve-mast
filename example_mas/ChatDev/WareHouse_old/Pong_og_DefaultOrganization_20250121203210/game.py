'''
Game class to manage the game loop and handle events.
'''
import pygame
from paddle import Paddle
from ball import Ball
from score import Score
class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pong Game")
        self.clock = pygame.time.Clock()
        self.paddle1 = Paddle(30, self.screen_height // 2 - 60)
        self.paddle2 = Paddle(self.screen_width - 40, self.screen_height // 2 - 60)
        self.ball = Ball(self.screen_width // 2, self.screen_height // 2)
        self.score = Score()
    def run(self):
        running = True
        while running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.paddle1.move_up()
        if keys[pygame.K_s]:
            self.paddle1.move_down()
        if keys[pygame.K_UP]:
            self.paddle2.move_up()
        if keys[pygame.K_DOWN]:
            self.paddle2.move_down()
    def update(self):
        self.ball.update(self.paddle1, self.paddle2, self.score)
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        self.ball.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()