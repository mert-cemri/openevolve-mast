'''
Defines the Chest class.
'''
from random import randint
class Chest:
    def __init__(self, position):
        self.position = position
    def open(self, player):
        player.hp += randint(20, 30)