'''
Manages the game loop, handles events, and updates the game state.
'''
import pygame
from player import Player
from alien import Alien
from bullet import Bullet
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.aliens = [Alien(x, 50) for x in range(0, 800, 50)]
        self.bullets = []
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
                    self.player.move(-1)
                elif event.key == pygame.K_RIGHT:
                    self.player.move(1)
                elif event.key == pygame.K_SPACE:
                    self.bullets.append(self.player.shoot())
    def update(self):
        bullets_to_remove = []
        aliens_to_remove = []
        for bullet in self.bullets:
            bullet.move()
            for alien in self.aliens:
                if bullet.check_collision(alien):
                    aliens_to_remove.append(alien)
                    bullets_to_remove.append(bullet)
                    break
        for alien in self.aliens:
            alien.move()
            if alien.y > 550:
                self.running = False
        # Remove bullets and aliens outside the iteration
        self.bullets = [bullet for bullet in self.bullets if bullet not in bullets_to_remove]
        self.aliens = [alien for alien in self.aliens if alien not in aliens_to_remove]
        # Check if all aliens are defeated
        if not self.aliens:
            self.running = False
    def render(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        for alien in self.aliens:
            alien.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        pygame.display.flip()