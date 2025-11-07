'''
Handles the main game loop, event handling, and rendering.
'''
import pygame
from board import Board
from tetromino import TetrominoFactory
from constants import *
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.tetromino_factory = TetrominoFactory()
        self.current_tetromino = self.tetromino_factory.create_tetromino()
    def run(self):
        running = True
        while running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.current_tetromino.move(-1, 0, self.board)
                elif event.key == pygame.K_RIGHT:
                    self.current_tetromino.move(1, 0, self.board)
                elif event.key == pygame.K_DOWN:
                    self.current_tetromino.move(0, 1, self.board)
                elif event.key == pygame.K_UP:
                    self.current_tetromino.rotate(self.board)
    def update(self):
        if not self.current_tetromino.move(0, 1, self.board):
            self.board.add_tetromino(self.current_tetromino)
            self.board.clear_lines()
            self.current_tetromino = self.tetromino_factory.create_tetromino()
            if not self.board.is_valid_position(self.current_tetromino):
                print("Game Over")
                pygame.quit()
                exit()
    def draw(self):
        self.screen.fill(BLACK)
        self.board.draw(self.screen)
        self.current_tetromino.draw(self.screen)
        pygame.display.flip()