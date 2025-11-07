'''
The GameDisplay class handles rendering the game state to the screen.
'''
import pygame
class GameDisplay:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
    def clear(self):
        self.screen.fill((0, 0, 0))
    def draw_player(self, player):
        pygame.draw.rect(self.screen, (0, 255, 0), (player.x, player.y, 50, 30))
    def draw_aliens(self, aliens):
        for alien in aliens:
            pygame.draw.rect(self.screen, (255, 0, 0), (alien.x, alien.y, 40, 30))
    def draw_shots(self, shots):
        for shot in shots:
            pygame.draw.rect(self.screen, (255, 255, 0), (shot.x, shot.y, 5, 10))
    def update(self):
        pygame.display.flip()