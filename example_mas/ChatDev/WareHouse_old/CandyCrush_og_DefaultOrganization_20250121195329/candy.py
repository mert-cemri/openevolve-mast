'''
Candy class represents individual candies on the board.
'''
import pygame
class Candy:
    def __init__(self, color):
        self.color = color
        self.image = self.load_image()
    def load_image(self):
        # Load candy image based on color
        surface = pygame.Surface((50, 50))
        surface.fill(self.get_color())
        return surface
    def get_color(self):
        colors = {
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'yellow': (255, 255, 0),
            'purple': (128, 0, 128)
        }
        return colors[self.color]
    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))