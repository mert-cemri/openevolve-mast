'''
Main game loop and initialization.
'''
import pygame
from bird import Bird
from pipe import Pipe
from score import Score
from collision_manager import CollisionManager
def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe()]
    score = Score()
    collision_manager = CollisionManager()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()
        bird.update()
        for pipe in pipes:
            pipe.update()
            if pipe.is_off_screen():
                pipes.remove(pipe)
                pipes.append(Pipe())
                score.increase()
        if collision_manager.check_collision(bird, pipes):
            running = False
        screen.fill((135, 206, 235))  # Sky blue background
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)
        score.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()