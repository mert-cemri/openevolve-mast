'''
Utility functions for the Snake game.
'''
import random
def random_position():
    x = random.randint(0, 59) * 10
    y = random.randint(0, 39) * 10
    return (x, y)