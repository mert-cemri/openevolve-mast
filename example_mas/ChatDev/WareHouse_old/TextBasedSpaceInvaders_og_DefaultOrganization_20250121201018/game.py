'''
Game class that manages the game loop, events, updates, and rendering.
'''
import pygame
from player import Player
from alien import Alien
from shot import Shot
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.aliens = [Alien(x, 50) for x in range(100, 700, 100)]
        self.shots = []
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
                if event.key == pygame.K_LEFT:
                    self.player.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()
                elif event.key == pygame.K_SPACE:
                    self.shots.append(self.player.shoot())
    def update(self):
        shots_to_remove = []
        for shot in self.shots:  # Iterate over the list directly
            shot.move()
            for alien in self.aliens[:]:  # Iterate over a copy of the list
                if alien.check_collision(shot):
                    self.aliens.remove(alien)
                    shots_to_remove.append(shot)
                    break
        # Remove shots after iteration
        for shot in shots_to_remove:
            if shot in self.shots:
                self.shots.remove(shot)
        for alien in self.aliens:
            alien.move()
            if alien.rect.y >= 550:  # Corrected attribute access
                self.running = False
    def render(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        for alien in self.aliens:
            alien.draw(self.screen)
        for shot in self.shots:
            shot.draw(self.screen)
        pygame.display.flip()