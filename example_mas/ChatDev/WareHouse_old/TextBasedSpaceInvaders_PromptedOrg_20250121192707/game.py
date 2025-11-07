'''
This module contains the Game class, which manages the game loop and overall game state.
'''
import pygame
from player import Player
from alien import Alien
from shot import Shot
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.player = Player(self.screen)
        self.aliens = [Alien(self.screen, x, 50) for x in range(100, 700, 100)]
        self.shots = []
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
                if event.key == pygame.K_LEFT:
                    self.player.move(-1)
                elif event.key == pygame.K_RIGHT:
                    self.player.move(1)
                elif event.key == pygame.K_SPACE:
                    self.shots.append(self.player.fire())
    def update(self):
        for shot in self.shots[:]:
            shot.move()
            if shot.rect.bottom < 0:
                self.shots.remove(shot)
        for alien in self.aliens[:]:
            if alien.move():
                self.running = False  # End game if an alien reaches the bottom
        self.check_collisions()
        if not self.aliens:
            self.running = False  # End game if all aliens are defeated
    def check_collisions(self):
        for shot in self.shots:
            for alien in self.aliens:
                if shot.rect.colliderect(alien.rect):
                    self.shots.remove(shot)
                    self.aliens.remove(alien)
                    break
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw()
        for shot in self.shots:
            shot.draw()
        for alien in self.aliens:
            alien.draw()
        pygame.display.flip()