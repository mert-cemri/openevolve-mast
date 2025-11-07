'''
Player class for managing player state and interactions.
'''
import pygame
class Player:
    def __init__(self, x, y, game_map):
        self.x = x
        self.y = y
        self.hp = 100
        self.game_map = game_map
    def move(self, dx, dy):
        new_x, new_y = self.x + dx, self.y + dy
        if self.game_map.is_walkable(new_x, new_y):
            self.x, self.y = new_x, new_y
            # Check for monsters
            for monster in self.game_map.monsters:
                if monster.x == self.x and monster.y == self.y:
                    self.combat(monster)
                    break
            # Check for treasures
            for treasure in self.game_map.treasures:
                if treasure.x == self.x and treasure.y == self.y:
                    self.heal(treasure.heal_amount)
                    self.game_map.treasures.remove(treasure)
                    break
    def combat(self, monster):
        self.hp -= monster.hp
        self.game_map.monsters.remove(monster)
    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100
    def render(self, screen, tile_size):
        rect = pygame.Rect(self.x * tile_size, self.y * tile_size, tile_size, tile_size)
        pygame.draw.rect(screen, (0, 0, 255), rect)