'''
Main game loop and initialization.
'''
import pygame
from claw import Claw
from object import GameObject
from level import Level
from utils import load_image
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Gold Miner")
        self.clock = pygame.time.Clock()
        self.claw = Claw()
        self.objects = [GameObject("gold", 100, 50, (400, 300))]
        self.level = Level(minimum_gold=500, time_limit=60)
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.claw.grab(self.objects)
    def update(self):
        self.claw.move()
        if self.level.check_completion(self.claw, self.objects):
            print("Level Complete!")
            pygame.quit()
            exit()
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.claw.draw(self.screen)
        for obj in self.objects:
            obj.draw(self.screen)
        pygame.display.flip()
if __name__ == "__main__":
    game = Game()
    game.run()