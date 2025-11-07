'''
Main game loop and initialization.
'''
import pygame
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
# Initialize Pygame
pygame.init()
# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)
FPS = 60
# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")
# Create game objects
paddle1 = Paddle(30, SCREEN_HEIGHT // 2 - 60)
paddle2 = Paddle(SCREEN_WIDTH - 40, SCREEN_HEIGHT // 2 - 60)
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
scoreboard = Scoreboard()
# Main game loop
def run():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Handle input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_up()
        if keys[pygame.K_s]:
            paddle1.move_down()
        if keys[pygame.K_UP]:
            paddle2.move_up()
        if keys[pygame.K_DOWN]:
            paddle2.move_down()
        # Update game state
        ball.move(paddle1, paddle2, scoreboard)
        # Draw everything
        screen.fill(BG_COLOR)
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)
        scoreboard.draw(screen)
        # Refresh display
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
if __name__ == "__main__":
    run()