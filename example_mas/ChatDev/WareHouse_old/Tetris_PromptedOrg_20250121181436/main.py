'''
Main entry point for the Tetris game.
'''
from game import Game
def main(stdscr):
    game = Game(stdscr)
    game.start()
if __name__ == "__main__":
    import curses
    try:
        curses.wrapper(main)
    except curses.error as e:
        print(f"An error occurred with curses: {e}. Please ensure your terminal supports curses.")