'''
This module contains the Candy class which represents a single candy in the match-3 puzzle game.
'''
import random
class Candy:
    COLORS = ['R', 'G', 'B', 'Y', 'P']  # Red, Green, Blue, Yellow, Purple
    def __init__(self, color):
        self.color = color
    @staticmethod
    def random_candy():
        return Candy(random.choice(Candy.COLORS))