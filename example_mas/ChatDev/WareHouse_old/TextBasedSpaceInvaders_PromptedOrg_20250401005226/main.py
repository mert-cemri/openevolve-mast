'''
Main file to run the Space Invaders game.
'''
import pygame
import sys
from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
from scoreboard import Scoreboard
class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Invaders")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.scoreboard = Scoreboard(self)
        self._create_fleet()
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.scoreboard.increase_score(len(aliens))
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self.scoreboard.decrease_life()
                if self.scoreboard.is_game_over():
                    self._game_over()
                    return
                self.aliens.empty()
                self.bullets.empty()
                self._create_fleet()
                break
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.rect.right >= self.settings.screen_width or alien.rect.left <= 0:
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        self.settings.fleet_direction *= -1
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        available_space_y = self.settings.screen_height // 2
        number_rows = available_space_y // (2 * alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.draw()
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.aliens.draw(self.screen)
        self.scoreboard.draw()
        pygame.display.flip()
    def _game_over(self):
        print("Game Over!")
        pygame.quit()
        sys.exit()
if __name__ == '__main__':
    game = Game()
    game.run_game()