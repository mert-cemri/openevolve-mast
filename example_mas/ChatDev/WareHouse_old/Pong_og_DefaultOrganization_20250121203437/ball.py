'''
Ball class to represent the ball in the game.
'''
import pygame
import random
class Ball:
    def __init__(self, x, y, radius):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.radius = radius
        self.base_speed = 5
        self.speed_x = random.choice([-self.base_speed, self.base_speed])
        self.speed_y = random.choice([-self.base_speed, self.base_speed])
        self.speed_increment = 0.5  # Increment speed after each paddle hit
        self.max_speed = 10  # Set a maximum speed limit
    def move(self, paddle1, paddle2, score, screen_width, screen_height):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Bounce off top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1
        # Bounce off paddles
        if self.rect.colliderect(paddle1.rect) or self.rect.colliderect(paddle2.rect):
            self.speed_x *= -1
            # Increase speed slightly
            self.speed_x += self.speed_increment if self.speed_x > 0 else -self.speed_increment
            self.speed_y += self.speed_increment if self.speed_y > 0 else -self.speed_increment
            # Ensure speed does not exceed max speed
            self.speed_x = max(min(self.speed_x, self.max_speed), -self.max_speed)
            self.speed_y = max(min(self.speed_y, self.max_speed), -self.max_speed)
        # Score points
        if self.rect.left <= 0:
            score.update(player=2)
            self.reset(screen_width, screen_height)
        if self.rect.right >= screen_width:
            score.update(player=1)
            self.reset(screen_width, screen_height)
    def reset(self, screen_width, screen_height):
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed_x = random.choice([-self.base_speed, self.base_speed])
        self.speed_y = random.choice([-self.base_speed, self.base_speed])
        # Reset speed increment logic
        self.speed_increment = 0.5  # Reset to initial increment value
    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)