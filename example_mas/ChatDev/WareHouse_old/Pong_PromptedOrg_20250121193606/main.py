'''
Main module to run the Pong game.
'''
import pygame
from paddle import Paddle
from ball import Ball
from score import Score
# Initialize Pygame
pygame.init()
# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong Game')
# Create paddles, ball, and score
paddle1 = Paddle(20, SCREEN_HEIGHT // 2 - 60)
paddle2 = Paddle(SCREEN_WIDTH - 30, SCREEN_HEIGHT // 2 - 60)
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
score = Score()
# Clock to control the frame rate
clock = pygame.time.Clock()
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Handle paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.move(up=True)
    if keys[pygame.K_s]:
        paddle1.move(up=False)
    if keys[pygame.K_UP]:
        paddle2.move(up=True)
    if keys[pygame.K_DOWN]:
        paddle2.move(up=False)
    # Update ball position and check for collisions
    ball.update(paddle1, paddle2, score)
    # Clear the screen
    screen.fill(BLACK)
    # Draw paddles, ball, and score
    paddle1.draw(screen)
    paddle2.draw(screen)
    ball.draw(screen)
    score.draw(screen, SCREEN_WIDTH)
    # Update the display
    pygame.display.flip()
    # Cap the frame rate
    clock.tick(60)
pygame.quit()