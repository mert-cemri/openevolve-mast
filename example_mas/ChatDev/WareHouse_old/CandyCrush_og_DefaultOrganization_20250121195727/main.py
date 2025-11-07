'''
Main game loop and initialization.
'''
import pygame
from board import Board
from score import Score
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Match-3 Puzzle Game")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.score = Score()
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
                pos = pygame.mouse.get_pos()
                self.board.handle_click(pos)
    def update(self):
        self.board.update()
        self.score.update_score(self.board.cleared_matches)
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.board.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()
if __name__ == "__main__":
    game = Game()
    game.run()