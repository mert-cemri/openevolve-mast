'''
Defines the Player class.
'''
import pygame
from random import randint
from monster import Monster
from chest import Chest
from door import Door
class Player:
    def __init__(self, position):
        self.position = position
        self.hp = 100
    def move(self, dx, dy, game_map):
        new_position = (self.position[0] + dx, self.position[1] + dy)
        if game_map.is_walkable(new_position):
            self.position = new_position
    def interact(self, game_map):
        tile = game_map.get_tile(self.position)
        if isinstance(tile, Monster):
            self.hp -= tile.hp  # Reduce player's HP by the monster's HP
        elif isinstance(tile, Chest):
            self.hp += randint(20, 30)  # Example interaction
        elif isinstance(tile, Door):
            game_map.next_level()
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (*self.position, 10, 10))