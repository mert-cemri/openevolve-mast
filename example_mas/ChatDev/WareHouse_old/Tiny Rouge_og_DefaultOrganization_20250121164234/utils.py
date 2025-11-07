'''
Utility functions for common tasks.
'''
import pygame
import random
def load_image(filename):
    return pygame.image.load(filename)
def random_hp_restore():
    return random.randint(20, 30)