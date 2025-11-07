'''
Defines the Game class, managing the main game loop, user input, snake and food interactions, difficulty settings, score tracking, and board updates using curses for portability and reliability.
'''
import curses
import time
from snake import Snake
from food import Food
class Game:
    def __init__(self, width, height, difficulty):
        self.width = width
        self.height = height
        self.snake = Snake()
        self.food = Food(width, height, self.snake.body)
        self.score = 0
        self.difficulty = difficulty
        self.speed = {'easy': 0.3, 'medium': 0.2, 'hard': 0.1}[difficulty]
        self.game_over = False
    def play(self):
        curses.wrapper(self.curses_main)
    def curses_main(self, stdscr):
        curses.curs_set(0)
        stdscr.nodelay(True)
        stdscr.timeout(int(self.speed * 1000))
        key_mapping = {
            curses.KEY_UP: 'UP',
            curses.KEY_DOWN: 'DOWN',
            curses.KEY_LEFT: 'LEFT',
            curses.KEY_RIGHT: 'RIGHT'
        }
        while not self.game_over:
            key = stdscr.getch()
            if key in key_mapping:
                self.snake.change_direction(key_mapping[key])
            self.snake.move()
            if self.snake.check_collision(self.width, self.height):
                self.game_over = True
                self.display_board_curses(stdscr)
                stdscr.addstr(self.height + 1, 0, "Game Over!")
                stdscr.addstr(self.height + 2, 0, f"Final Score: {self.score}")
                stdscr.refresh()
                time.sleep(2)
                break
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.score += 1
                self.food = Food(self.width, self.height, self.snake.body)
            self.display_board_curses(stdscr)
    def display_board_curses(self, stdscr):
        stdscr.clear()
        for y in range(self.height):
            row = ''
            for x in range(self.width):
                if (x, y) == self.snake.body[0]:
                    row += 'S'
                elif (x, y) in self.snake.body:
                    row += 's'
                elif (x, y) == self.food.position:
                    row += 'F'
                else:
                    row += '.'
            stdscr.addstr(y, 0, row)
        stdscr.addstr(self.height, 0, f"Score: {self.score}")
        stdscr.refresh()