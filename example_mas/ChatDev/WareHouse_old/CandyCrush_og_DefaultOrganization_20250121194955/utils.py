'''
Utility functions for the match-3 puzzle game.
'''
import pygame
import random
def load_images():
    # Load candy images
    images = {}
    for i in range(6):
        images[i] = pygame.Surface((50, 50))
        images[i].fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    return images
def check_adjacent(pos1, pos2):
    # Check if two positions are adjacent
    return (abs(pos1[0] - pos2[0]) == 1 and pos1[1] == pos2[1]) or (abs(pos1[1] - pos2[1]) == 1 and pos1[0] == pos2[0])