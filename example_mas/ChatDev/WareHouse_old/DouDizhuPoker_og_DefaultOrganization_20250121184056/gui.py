'''
Handles the graphical user interface for the Dou Dizhu game.
'''
import pygame
class GameGUI:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.font = pygame.font.Font(None, 36)
    def handle_event(self, event):
        # Example: Handle mouse clicks or keyboard inputs to play cards
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Logic to play selected cards
                pass
    def render(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))
        # Render each player's hand
        for i, player in enumerate(self.game.players):
            hand_text = self.font.render(str(player), True, (255, 255, 255))
            self.screen.blit(hand_text, (50, 50 + i * 100))
        # Render additional game state information as needed