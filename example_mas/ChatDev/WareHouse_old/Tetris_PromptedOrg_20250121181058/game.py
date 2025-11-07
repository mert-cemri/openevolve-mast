'''
Game class to manage the Tetris game state and logic.
'''
import pygame
from board import Board
from tetromino import Tetromino
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.current_tetromino = Tetromino()
        self.running = True
        self.score = 0
    def start(self):
        while self.running:
            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(FPS)
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.current_tetromino.move(-1, self.board)
                elif event.key == pygame.K_RIGHT:
                    self.current_tetromino.move(1, self.board)
                elif event.key == pygame.K_DOWN:
                    self.current_tetromino.move(0, self.board, down=True)
                elif event.key == pygame.K_UP:
                    self.current_tetromino.rotate(self.board)
    def update(self):
        if not self.current_tetromino.move(0, self.board, down=True):
            # Add the tetromino to the board
            for y, row in enumerate(self.current_tetromino.shape):
                for x, cell in enumerate(row):
                    if cell:
                        self.board.grid[self.current_tetromino.y + y][self.current_tetromino.x + x] = cell
            lines_cleared = self.board.clear_lines()
            self.score += lines_cleared * 100  # Example scoring: 100 points per line
            self.current_tetromino = Tetromino()
            if self.board.is_game_over():
                self.running = False
    def render(self):
        self.screen.fill((0, 0, 0))
        self.board.draw(self.screen)
        self.current_tetromino.draw(self.screen)
        self.display_score()
        pygame.display.flip()
    def display_score(self):
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))