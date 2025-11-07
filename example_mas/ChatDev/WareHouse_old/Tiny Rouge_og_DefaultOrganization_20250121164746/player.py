'''
Player class to manage player attributes and actions.
'''
import pygame
import random
class Player:
    def __init__(self, position):
        self.position = position
        self.hp = 100
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 255, 0))
    def move(self, direction, game_map):
        x, y = self.position
        new_position = self.position
        if direction == 'up' and game_map.is_walkable(x, y - 1):
            new_position = (x, y - 1)
        elif direction == 'down' and game_map.is_walkable(x, y + 1):
            new_position = (x, y + 1)
        elif direction == 'left' and game_map.is_walkable(x - 1, y):
            new_position = (x - 1, y)
        elif direction == 'right' and game_map.is_walkable(x + 1, y):
            new_position = (x + 1, y)
        # Update position
        self.position = new_position
        # Check for interactions at the new position
        x, y = self.position
        tile = game_map.get_tile(x, y)
        if tile == 'monster':
            self.hp -= random.randint(10, 20)  # Example monster damage
        elif tile == 'treasure':
            self.hp += random.randint(20, 30)
            self.hp = min(self.hp, 100)  # Cap HP at 100
    def draw(self, screen):
        screen.blit(self.image, (self.position[0] * 10, self.position[1] * 10))