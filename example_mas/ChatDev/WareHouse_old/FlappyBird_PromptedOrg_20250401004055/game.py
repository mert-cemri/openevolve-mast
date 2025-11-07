'''
Game class to manage game loop, events, updates, rendering, and game over logic.
'''
import pygame
import random
from bird import Bird
from pipe import Pipe
class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.bird = Bird(100, 300)
        self.pipes = []
        self.spawn_timer = 0
        self.score = 0
        self.font = pygame.font.SysFont(None, 48)
        self.running = True
        self.pipe_speed = 4
        self.pipe_gap = 200
    def reset(self):
        self.bird = Bird(100, 300)
        self.pipes.clear()
        self.spawn_timer = 0
        self.score = 0
        self.pipe_speed = 4
        self.pipe_gap = 200
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.flap()
    def update(self):
        self.bird.update()
        self.spawn_timer += 1
        if self.spawn_timer > 90:
            self.spawn_timer = 0
            gap_y = random.randint(150, 450)
            self.pipes.append(Pipe(400, gap_y, self.pipe_gap, self.pipe_speed))
        bird_rect = self.bird.get_rect()
        screen_rect = self.screen.get_rect()
        for pipe in self.pipes:
            pipe.update()
            if pipe.collide(bird_rect) or bird_rect.bottom >= screen_rect.bottom or bird_rect.top <= screen_rect.top:
                self.running = False
                self.draw_game_over()
                self.wait_for_restart()
                self.reset()
                self.running = True
                break
            if pipe.passed is False and pipe.x + pipe.width < self.bird.x:
                pipe.passed = True
                self.score += 1
                if self.score % 5 == 0:
                    self.pipe_speed += 0.5
                    self.pipe_gap = max(120, self.pipe_gap - 10)
        self.pipes = [pipe for pipe in self.pipes if not pipe.off_screen()]
    def draw(self):
        self.screen.fill((135, 206, 235))  # Sky blue background
        self.bird.draw(self.screen)
        for pipe in self.pipes:
            pipe.draw(self.screen)
        score_img = self.font.render(str(self.score), True, (255, 255, 255))
        self.screen.blit(score_img, (200 - score_img.get_width() // 2, 20))
        pygame.display.flip()
    def draw_game_over(self):
        self.screen.fill((0, 0, 0))
        game_over_text = self.font.render("Game Over", True, (255, 0, 0))
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        restart_text = self.font.render("Press SPACE to Restart", True, (255, 255, 255))
        self.screen.blit(game_over_text, (200 - game_over_text.get_width() // 2, 200))
        self.screen.blit(score_text, (200 - score_text.get_width() // 2, 260))
        self.screen.blit(restart_text, (200 - restart_text.get_width() // 2, 320))
        pygame.display.flip()
    def wait_for_restart(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False
    def run(self):
        while True:
            self.handle_events()
            if self.running:
                self.update()
                self.draw()
            self.clock.tick(60)