'''
Main entry point for the text-based adventure game.
'''
from game_engine import GameEngine
from game_data_loader import GameDataLoader
def main():
    # Load game data from JSON file
    game_data = GameDataLoader.load_data('game_data.json')
    # Initialize and start the game engine
    game_engine = GameEngine(game_data)
    game_engine.start()
if __name__ == "__main__":
    main()