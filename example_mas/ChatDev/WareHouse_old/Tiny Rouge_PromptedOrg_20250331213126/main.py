'''
Main entry point for the roguelike game inspired by Tower of the Sorcerer.
'''
import pygame
from map import Map
from player import Player
# Initialize pygame
pygame.init()
# Constants
SCREEN_SIZE = 800
TILE_SIZE = SCREEN_SIZE // 20
FONT = pygame.font.SysFont('Arial', 20)
# Setup screen
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Tower of the Sorcerer Roguelike")
def draw_ui(player):
    hp_text = FONT.render(f'Player HP: {player.hp}', True, (255, 255, 255))
    screen.blit(hp_text, (10, 10))
def main():
    clock = pygame.time.Clock()
    game_map = Map()
    player = Player(game_map.start_x, game_map.start_y, game_map)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.move(0, -1)
                elif event.key == pygame.K_s:
                    player.move(0, 1)
                elif event.key == pygame.K_a:
                    player.move(-1, 0)
                elif event.key == pygame.K_d:
                    player.move(1, 0)
        screen.fill((0, 0, 0))
        game_map.render(screen, TILE_SIZE)
        player.render(screen, TILE_SIZE)
        draw_ui(player)
        pygame.display.flip()
        clock.tick(60)
        if game_map.is_door(player.x, player.y):
            print("You reached the door! Level Complete!")
            running = False
        if player.hp <= 0:
            print("Game Over! You died.")
            running = False
    pygame.quit()
if __name__ == "__main__":
    main()