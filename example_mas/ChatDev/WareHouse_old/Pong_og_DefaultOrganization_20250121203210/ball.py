'''
Ball class to represent the ball in the game.
'''
import pygame
import random
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.initial_speed = 4
        self.x_speed = self.initial_speed
        self.y_speed = self.initial_speed
        self.speed_increment = 0.5  # Increment factor for speed
    def update(self, paddle1, paddle2, score):
        self.x += self.x_speed
        self.y += self.y_speed
        # Ball collision with top and bottom
        if self.y - self.radius <= 0 or self.y + self.radius >= 600:
            self.y_speed = -self.y_speed
        # Ball collision with paddles
        if self.x - self.radius <= paddle1.x + paddle1.width and paddle1.y < self.y < paddle1.y + paddle1.height:
            self.x_speed = -self.x_speed
        if self.x + self.radius >= paddle2.x and paddle2.y < self.y < paddle2.y + paddle2.height:
            self.x_speed = -self.x_speed
        # Ball out of bounds
        if self.x < 0:
            score.increase_score(2)
            self.reset()
        if self.x > 800:
            score.increase_score(1)
            self.reset()
    def reset(self):
        self.x = 400
        self.y = 300
        self.x_speed = random.choice([-self.initial_speed, self.initial_speed])
        self.y_speed = random.choice([-self.initial_speed, -3, 3, self.initial_speed])
        self.initial_speed += self.speed_increment  # Increase speed for next round
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)