'''
Defines the Candy class representing a single candy on the board.
'''
import random
class Candy:
    def __init__(self):
        self.type = random.choice(['red', 'green', 'blue', 'yellow', 'purple'])
    def __repr__(self):
        return f"Candy({self.type})"