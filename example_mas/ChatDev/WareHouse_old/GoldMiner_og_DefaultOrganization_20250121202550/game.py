'''
Game class to manage the game loop and state.
'''
import pygame
from claw import Claw
from object import Object
from level import Level
from utils import display_text
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.claw = Claw()
        self.objects = [Object("gold", 100, (100, 300)), Object("rock", 50, (400, 300))]
        self.level = Level(60, 500)  # 60 seconds, 500 gold value goal
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
        self.claw.update_grab(self.level)
        self.level.check_time()
        if self.level.check_goal():
            self.running = False  # Stop the game when the goal is reached
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.claw.draw(self.screen)
        for obj in self.objects:
            if not self.claw.grabbing or obj != self.claw.grabbed_object:
                obj.draw(self.screen)
        display_text(self.screen, f"Time: {self.level.time_left}", (10, 10))
        display_text(self.screen, f"Goal: {self.level.goal}", (10, 40))
        display_text(self.screen, f"Current Value: {self.level.current_value}", (10, 70))
        pygame.display.flip()