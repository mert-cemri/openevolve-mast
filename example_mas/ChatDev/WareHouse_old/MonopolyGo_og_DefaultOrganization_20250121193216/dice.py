'''
Dice class to simulate dice rolling.
'''
import random
class Dice:
    def roll(self):
        return random.randint(1, 6)