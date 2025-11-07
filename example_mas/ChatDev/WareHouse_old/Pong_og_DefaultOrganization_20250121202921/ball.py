'''
Ball class for game dynamics.
'''
import pygame
import random
# Constants
BALL_RADIUS = 10
BALL_COLOR = (255, 255, 255)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.reset()
        self.speed_increment = 0.5
        self.max_speed = 10
    def move(self, paddle1, paddle2, scoreboard):
        self.rect.x += self.dx
        self.rect.y += self.dy
        # Bounce off top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.dy = -self.dy
        # Bounce off paddles
        if self.rect.colliderect(paddle1.rect) or self.rect.colliderect(paddle2.rect):
            self.dx = -self.dx
            # Increase speed after hitting a paddle
            self.dx += self.speed_increment if self.dx > 0 else -self.speed_increment
            self.dy += self.speed_increment if self.dy > 0 else -self.speed_increment
            # Cap the speed to max_speed
            self.dx = max(-self.max_speed, min(self.dx, self.max_speed))
            self.dy = max(-self.max_speed, min(self.dy, self.max_speed))
        # Check for scoring
        if self.rect.left <= 0:
            scoreboard.update_score(2)
            self.reset()
        elif self.rect.right >= SCREEN_WIDTH:
            scoreboard.update_score(1)
            self.reset()
    def reset(self):
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.dx = random.choice([-4, 4])
        self.dy = random.choice([-4, 4])
        # Ensure that the ball does not stop
        if self.dx == 0:
            self.dx = random.choice([-4, 4])
        if self.dy == 0:
            self.dy = random.choice([-4, 4])
    def draw(self, screen):
        pygame.draw.ellipse(screen, BALL_COLOR, self.rect)