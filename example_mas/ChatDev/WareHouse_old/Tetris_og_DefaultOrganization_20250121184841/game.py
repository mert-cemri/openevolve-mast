'''
Game class to manage the game state, including the game loop, score, and game over conditions.
'''
import pygame
from board import Board
from tetromino import Tetromino
from constants import *
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.current_tetromino = Tetromino()
        self.score = 0
        self.game_over = False
    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
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
            # If the tetromino cannot move down, it has landed
            self.board.add_tetromino(self.current_tetromino)
            self.current_tetromino = Tetromino()
        if self.board.is_game_over():
            self.game_over = True
    def draw(self):
        self.screen.fill(BLACK)
        self.board.draw(self.screen)
        self.current_tetromino.draw(self.screen)
        pygame.display.flip()