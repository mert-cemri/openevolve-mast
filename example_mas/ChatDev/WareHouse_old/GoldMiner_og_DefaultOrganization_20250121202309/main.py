'''
Main game file that initializes the game and runs the main loop.
'''
import pygame
from claw import Claw
from object import Object
from level import Level
from ui import UI
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Gold Miner")
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.claw = Claw(self.screen, self.level)
        self.objects = [Object(self.screen, x, y) for x, y in [(100, 400), (300, 450), (500, 420)]]
        self.ui = UI(self.screen)
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
                if event.key == pygame.K_SPACE:
                    self.claw.grab(self.objects)
    def update(self):
        self.claw.move()
        self.claw.reel_in()
        self.level.update_timer()
        if self.level.check_completion():
            self.running = False
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.claw.draw()
        for obj in self.objects:
            obj.draw()
        self.ui.draw_score(self.level.score)
        self.ui.draw_timer(self.level.time_remaining)
        pygame.display.flip()
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()