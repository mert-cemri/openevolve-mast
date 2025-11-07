'''
Utility functions for the Gold Miner game.
'''
import pygame
def load_image(filename):
    return pygame.image.load(filename)
def display_text(screen, text, position):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, position)