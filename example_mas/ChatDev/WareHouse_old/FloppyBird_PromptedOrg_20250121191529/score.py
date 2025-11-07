'''
Manages the player's score and displays it on the screen.
'''
import pygame
class Score:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.score = 0
    def update(self, bird, pipes):
        for pipe in pipes:
            if pipe.rect_top.right < bird.get_rect().left and not pipe.scored:
                self.score += 1
                pipe.scored = True
    def draw(self, screen):
        score_surface = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))