'''
Ball class for the Pong game.
'''
import pygame
import random
WHITE = (255, 255, 255)
BALL_SIZE = 20
BALL_SPEED = 5
MAX_BALL_SPEED = 10  # Define a maximum speed limit for the ball
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.dx = BALL_SPEED * random.choice((1, -1))
        self.dy = BALL_SPEED * random.choice((1, -1))
        self.speed = BALL_SPEED
    def update(self, paddle1, paddle2, score):
        self.rect.x += self.dx
        self.rect.y += self.dy
        # Bounce off top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= pygame.display.get_surface().get_height():
            self.dy = -self.dy
        # Bounce off paddles
        if self.rect.colliderect(paddle1.rect) or self.rect.colliderect(paddle2.rect):
            self.dx = -self.dx
            if self.speed < MAX_BALL_SPEED:  # Only increase speed if below max limit
                self.speed += 0.5
            self.dx = self.dx / abs(self.dx) * self.speed  # Maintain direction
            self.dy = self.dy / abs(self.dy) * self.speed  # Maintain direction
        # Check for scoring
        if self.rect.left <= 0:
            score.increment_player2()
            self.reset()
        if self.rect.right >= pygame.display.get_surface().get_width():
            score.increment_player1()
            self.reset()
    def reset(self):
        self.rect.x = pygame.display.get_surface().get_width() // 2
        self.rect.y = pygame.display.get_surface().get_height() // 2
        self.speed = BALL_SPEED  # Reset speed to initial value
        self.dx = self.speed * random.choice((1, -1))
        self.dy = self.speed * random.choice((1, -1))
    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)