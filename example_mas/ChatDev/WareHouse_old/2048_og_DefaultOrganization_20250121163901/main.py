'''
Main game file that initializes and runs the 2048 game with a 10x10 grid.
'''
import pygame
from grid import Grid
from renderer import Renderer
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("2048 Game - 10x10 Grid")
        self.clock = pygame.time.Clock()
        self.grid = Grid()
        self.renderer = Renderer(self.screen, self.grid)
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.grid.move('up')
                elif event.key == pygame.K_DOWN:
                    self.grid.move('down')
                elif event.key == pygame.K_LEFT:
                    self.grid.move('left')
                elif event.key == pygame.K_RIGHT:
                    self.grid.move('right')
    def update(self):
        if not self.grid.can_move():
            self.running = False
    def render(self):
        self.screen.fill((187, 173, 160))
        self.renderer.draw_grid()
        self.renderer.draw_tiles()
        pygame.display.flip()
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()