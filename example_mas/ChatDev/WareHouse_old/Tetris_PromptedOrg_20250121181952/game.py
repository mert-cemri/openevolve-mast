'''
Game class manages the overall game state, including the game loop, score, and game over conditions.
'''
from board import Board
from tetromino import Tetromino
import time
import curses
class Game:
    def __init__(self):
        self.board = Board()
        self.current_tetromino = Tetromino(self.board)
        self.score = 0
        self.game_over = False
    def run(self):
        curses.wrapper(self.game_loop)
    def game_loop(self, stdscr):
        curses.curs_set(0)  # Hide the cursor
        stdscr.keypad(True)
        stdscr.nodelay(True)  # Make getch non-blocking
        try:
            while not self.game_over:
                self.update()
                self.render(stdscr)
                key = stdscr.getch()
                if key == curses.KEY_LEFT:
                    self.current_tetromino.move_left()
                    if not self.board.can_place(self.current_tetromino):
                        self.current_tetromino.move_right()
                elif key == curses.KEY_RIGHT:
                    self.current_tetromino.move_right()
                    if not self.board.can_place(self.current_tetromino):
                        self.current_tetromino.move_left()
                elif key == curses.KEY_UP:
                    self.current_tetromino.rotate()
                elif key == curses.KEY_DOWN:
                    self.current_tetromino.move_down()
                    if not self.board.can_place(self.current_tetromino):
                        self.current_tetromino.move_up()
                time.sleep(0.1)
        except curses.error as e:
            stdscr.addstr(self.board.height + 2, 0, f"Curses Error: {str(e)}")
            stdscr.refresh()
            time.sleep(2)
        except Exception as e:
            stdscr.addstr(self.board.height + 2, 0, f"Error: {str(e)}")
            stdscr.refresh()
            time.sleep(2)
        finally:
            stdscr.keypad(False)
            curses.curs_set(1)  # Restore the cursor
            stdscr.nodelay(False)  # Reset getch to blocking mode
    def update(self):
        if not self.board.can_place(self.current_tetromino):
            self.game_over = True
            print("Game Over!")
            return
        self.current_tetromino.move_down()
        if not self.board.can_place(self.current_tetromino):
            self.current_tetromino.move_up()
            self.board.place(self.current_tetromino)
            self.board.clear_lines()
            self.current_tetromino = Tetromino(self.board)
            self.score += 100  # Example scoring
    def render(self, stdscr):
        stdscr.clear()
        self.board.display(stdscr)
        stdscr.addstr(self.board.height + 1, 0, f"Score: {self.score}")
        stdscr.refresh()