'''
Game class to manage the game loop, handle events, and update the game state.
'''
import pygame
from player import Player
from alien import Alien
from bullet import Bullet
from collision_manager import CollisionManager
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.player = Player(self.screen)
        self.aliens = [Alien(self.screen, x, 50) for x in range(100, 700, 100)]
        self.bullets = []
        self.collision_manager = CollisionManager(self.bullets, self.aliens)
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
                    bullet = self.player.shoot()
                    if bullet:
                        self.bullets.append(bullet)
    def update(self):
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.rect.bottom < 0:  # Remove bullet if it moves off the top of the screen
                self.bullets.remove(bullet)
        for alien in self.aliens:
            alien.move()
            # Check if any alien has reached the bottom
            if alien.rect.bottom >= self.screen.get_height():
                self.running = False  # End the game if an alien reaches the bottom
        self.collision_manager.check_collisions()
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw()
        for bullet in self.bullets:
            bullet.draw()
        for alien in self.aliens:
            alien.draw()
        pygame.display.flip()