'''
The Game class manages the game loop, processes user input, updates game state, and renders the game.
'''
import pygame
from player import Player
from alien import Alien
from shot import Shot
from game_display import GameDisplay
class Game:
    def __init__(self):
        pygame.init()
        self.display = GameDisplay()
        self.player = Player()
        self.aliens = [Alien(x, y) for x in range(5) for y in range(3)]
        self.shots = []
        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()
                elif event.key == pygame.K_SPACE:
                    self.shots.append(self.player.fire())
    def update(self):
        for shot in self.shots[:]:  # Iterate over a copy of the list
            shot.move()
            for alien in self.aliens[:]:  # Iterate over a copy of the list
                if shot.collides_with(alien):
                    if alien in self.aliens:
                        self.aliens.remove(alien)
                    if shot in self.shots:
                        self.shots.remove(shot)
                    break
        for alien in self.aliens:
            alien.move()
            if alien.reaches_bottom():
                self.running = False
        if not self.aliens:
            self.running = False
    def render(self):
        self.display.clear()
        self.display.draw_player(self.player)
        self.display.draw_aliens(self.aliens)
        self.display.draw_shots(self.shots)
        self.display.update()