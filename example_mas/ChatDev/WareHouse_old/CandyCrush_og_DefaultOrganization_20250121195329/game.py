'''
Game class manages the overall game state, including the game loop, event handling, and rendering.
'''
import pygame
from board import Board
from score import Score
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Match-3 Puzzle Game")
        self.clock = pygame.time.Clock()
        self.score = Score()
        self.board = Board(self.score)  # Pass score to Board
        self.running = True
        self.selected_candy = None
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(pygame.mouse.get_pos())
    def handle_mouse_click(self, pos):
        col = pos[0] // 50
        row = pos[1] // 50
        if self.selected_candy:
            if (abs(self.selected_candy[0] - row) == 1 and self.selected_candy[1] == col) or \
               (abs(self.selected_candy[1] - col) == 1 and self.selected_candy[0] == row):
                self.board.swap_candies(self.selected_candy, (row, col))
                self.selected_candy = None
            else:
                self.selected_candy = (row, col)
        else:
            self.selected_candy = (row, col)
    def update(self):
        self.board.update()
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.board.draw(self.screen)
        # Display score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {self.score.points}', True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()