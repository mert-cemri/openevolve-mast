'''
Main game file that initializes and runs the match-3 puzzle game.
'''
import pygame
from board import Board
from score import Score
from utils import load_images
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Match-3 Puzzle Game")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.score = Score()
        self.images = load_images()
        self.selected_candy = None
    def run(self):
        running = True
        while running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_click(event.pos)
    def handle_click(self, position):
        col = position[0] // 50
        row = position[1] // 50
        if self.selected_candy:
            self.board.swap_candies(self.selected_candy, (row, col))
            self.selected_candy = None
        else:
            self.selected_candy = (row, col)
    def update(self):
        self.board.update(self.score)
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.board.draw(self.screen, self.images)
        self.display_score()
        pygame.display.flip()
    def display_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score.points}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))
if __name__ == "__main__":
    game = Game()
    game.run()