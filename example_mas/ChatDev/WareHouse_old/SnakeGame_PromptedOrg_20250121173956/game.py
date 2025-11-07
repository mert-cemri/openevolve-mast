'''
Manages the overall game state, including the game loop, checking for game over conditions, and updating the game board.
'''
from board import Board
from snake import Snake
from food import Food
import curses
class Game:
    def __init__(self):
        self.board = Board()
        self.snake = Snake(self.board)
        self.food = Food(self.board)
        self.is_game_over = False
    def run(self):
        try:
            curses.wrapper(self.game_loop)
        except curses.error:
            print("Error: The terminal does not support curses. Please use a compatible terminal.")
    def game_loop(self, stdscr):
        stdscr.nodelay(1)
        stdscr.timeout(100)
        while not self.is_game_over:
            key = stdscr.getch()
            self.handle_input(key)
            self.snake.move()
            self.check_collisions()
            self.board.render(stdscr, self.snake, self.food)
    def handle_input(self, key):
        if key == curses.KEY_UP:
            self.snake.change_direction((0, -1))
        elif key == curses.KEY_DOWN:
            self.snake.change_direction((0, 1))
        elif key == curses.KEY_LEFT:
            self.snake.change_direction((-1, 0))
        elif key == curses.KEY_RIGHT:
            self.snake.change_direction((1, 0))
    def check_collisions(self):
        if self.snake.has_collided_with_wall() or self.snake.has_collided_with_self():
            self.is_game_over = True
        elif self.snake.has_eaten_food(self.food):
            self.snake.grow()
            self.food.reposition(self.snake)