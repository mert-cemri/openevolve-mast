'''
Main entry point for the text-based adventure game.
'''
from game_engine import GameEngine
def main():
    game = GameEngine()
    game.load_game_data('game_data.json')
    game.start_game()
if __name__ == '__main__':
    main()