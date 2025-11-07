'''
Defines the Player class for managing player attributes and actions.
'''
import pygame
from utils import load_image
from monster import Monster
from treasure_chest import TreasureChest
from door import Door
class Player:
    def __init__(self, start_position):
        self.image = load_image('player.png')
        self.position = start_position
        self.hp = 100
    def move(self, direction, level):
        x, y = self.position
        if direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
        if level.is_walkable(x, y):
            self.position = (x, y)
            obj = level.get_object_at(x, y)
            if obj:
                self.interact_with_object(obj)
    def interact_with_object(self, obj):
        if isinstance(obj, Monster):
            self.hp -= obj.hp
        elif isinstance(obj, TreasureChest):
            self.hp += obj.restore_hp()
        elif isinstance(obj, Door):
            # Code to go to the next level
            print("Proceeding to the next level...")
    def draw(self, screen):
        x, y = self.position
        screen.blit(self.image, (x * 10, y * 10))