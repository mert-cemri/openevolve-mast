'''
Main entry point for the Space Invaders game. Initializes the game and starts the game loop.
'''
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from shot import Shot
class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Invaders")
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self._create_fleet()
    def run(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_shots()
            self._update_aliens()
            self._update_screen()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.ship.fire_shot()
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _update_shots(self):
        self.shots.update()
        for shot in self.shots.copy():
            if shot.rect.bottom <= 0:
                self.shots.remove(shot)
        self._check_collisions()
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!")
            pygame.quit()
            exit()
        self._check_aliens_bottom()
    def _check_collisions(self):
        collisions = pygame.sprite.groupcollide(self.shots, self.aliens, True, True)
        if not self.aliens:
            print("You won!")
            pygame.quit()
            exit()
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)
    def _create_alien(self, alien_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                print("Aliens reached the bottom!")
                pygame.quit()
                exit()
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.rect.right >= self.screen.get_rect().right or alien.rect.left <= 0:
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.fleet_direction *= -1
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for shot in self.shots.sprites():
            shot.draw_shot()
        self.aliens.draw(self.screen)
        pygame.display.flip()
if __name__ == '__main__':
    game = Game()
    game.run()