'''
Candy representation for the match-3 game.
'''
import pygame
class Candy:
    def __init__(self, candy_type):
        self.candy_type = candy_type
        self.color = self.get_color()
    def get_color(self):
        colors = {
            1: (255, 0, 0),
            2: (0, 255, 0),
            3: (0, 0, 255),
            4: (255, 255, 0),
            5: (255, 0, 255)
        }
        return colors[self.candy_type]
    def draw(self, screen, x, y):
        pygame.draw.circle(screen, self.color, (x, y), 20)