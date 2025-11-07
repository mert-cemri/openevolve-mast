'''
Main entry point for the Tetris game.
'''
import pygame
import sys
from game import TetrisGame
def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 600))
    pygame.display.set_caption('Tetris')
    clock = pygame.time.Clock()
    game = TetrisGame()
    running = True
    fall_time = 0
    fall_speed = game.speed
    while running:
        fall_time += clock.get_rawtime()
        clock.tick()
        if fall_time > fall_speed:
            fall_time = 0
            if not game.move(0, 1):
                game.lock_tetromino()
                game.clear_lines()
                if game.is_game_over():
                    running = False
                else:
                    game.spawn_tetromino()
                fall_speed = game.speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    game.move(0, 1)
                elif event.key == pygame.K_UP:
                    game.rotate()
                elif event.key == pygame.K_SPACE:
                    game.drop()
                    game.clear_lines()
                    if game.is_game_over():
                        running = False
                    else:
                        game.spawn_tetromino()
                    fall_speed = game.speed
        screen.fill((0, 0, 0))
        game.draw(screen)
        pygame.display.flip()
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()