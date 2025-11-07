'''
Main file to run the Pong game.
'''
import pygame
from paddle import Paddle
from ball import Ball
class PongGame:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Two-Player Pong Game")
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.paddle_left = Paddle((10, self.HEIGHT//2 - 60))
        self.paddle_right = Paddle((self.WIDTH - 20, self.HEIGHT//2 - 60))
        self.ball = Ball(self.WIDTH, self.HEIGHT)
        self.score_left = 0
        self.score_right = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.WINNING_SCORE = 5
    def paddle_movement(self, keys_pressed):
        if keys_pressed[pygame.K_w] and self.paddle_left.y > 0:
            self.paddle_left.move(-5)
        if keys_pressed[pygame.K_s] and self.paddle_left.y < self.HEIGHT - self.paddle_left.height:
            self.paddle_left.move(5)
        if keys_pressed[pygame.K_UP] and self.paddle_right.y > 0:
            self.paddle_right.move(-5)
        if keys_pressed[pygame.K_DOWN] and self.paddle_right.y < self.HEIGHT - self.paddle_right.height:
            self.paddle_right.move(5)
    def ball_movement(self):
        self.ball.move()
        # Collision with top and bottom edges
        if self.ball.y <= 0 or self.ball.y >= self.HEIGHT - self.ball.size:
            self.ball.y_vel *= -1
        # Improved Collision with paddles (checking ball direction)
        if (self.ball.x_vel < 0 and
            self.ball.x <= self.paddle_left.x + self.paddle_left.width and
            self.ball.y + self.ball.size >= self.paddle_left.y and
            self.ball.y <= self.paddle_left.y + self.paddle_left.height):
            self.ball.x_vel *= -1
        if (self.ball.x_vel > 0 and
            self.ball.x + self.ball.size >= self.paddle_right.x and
            self.ball.y + self.ball.size >= self.paddle_right.y and
            self.ball.y <= self.paddle_right.y + self.paddle_right.height):
            self.ball.x_vel *= -1
        # Scoring
        if self.ball.x < 0:
            self.score_right += 1
            self.reset_ball()
        if self.ball.x > self.WIDTH:
            self.score_left += 1
            self.reset_ball()
    def reset_ball(self):
        self.ball.reset_position()
    def check_score(self):
        if self.score_left >= self.WINNING_SCORE:
            return "Left Player Wins!"
        elif self.score_right >= self.WINNING_SCORE:
            return "Right Player Wins!"
        return None
    def draw(self):
        self.WIN.fill(self.BLACK)
        self.paddle_left.draw(self.WIN)
        self.paddle_right.draw(self.WIN)
        self.ball.draw(self.WIN)
        score_text = self.font.render(f"{self.score_left} : {self.score_right}", True, self.WHITE)
        self.WIN.blit(score_text, (self.WIDTH//2 - score_text.get_width()//2, 20))
        pygame.display.update()
    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys_pressed = pygame.key.get_pressed()
            self.paddle_movement(keys_pressed)
            self.ball_movement()
            winner = self.check_score()
            if winner:
                print(winner)
                running = False
            self.draw()
        pygame.quit()
if __name__ == "__main__":
    game = PongGame()
    game.run()