'''
Treasure class to represent treasure chests, which restore the player's health.
'''
import random
class Treasure:
    def __init__(self, position):
        self.position = position
        self.heal_amount = random.randint(20, 30)