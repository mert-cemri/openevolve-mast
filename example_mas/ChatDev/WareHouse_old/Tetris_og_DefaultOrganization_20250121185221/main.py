'''
Main file for the Tetris game. Initializes and runs the game loop.
'''
import pygame
from board import Board
from tetromino import Tetromino
from score import Score
class TetrisGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 600))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.current_tetromino = Tetromino()
        self.score = Score()
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
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
            lines_cleared = self.board.clear_lines()
            self.score.add_points(lines_cleared)
            self.current_tetromino = Tetromino()
            if not self.board.is_valid_position(self.current_tetromino):
                self.running = False
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.board.draw(self.screen)
        self.current_tetromino.draw(self.screen)
        pygame.display.flip()
if __name__ == '__main__':
    game = TetrisGame()
    game.run()