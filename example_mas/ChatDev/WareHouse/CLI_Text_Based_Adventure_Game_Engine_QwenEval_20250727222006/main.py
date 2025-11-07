'''
Main entry point for the text-based adventure game CLI engine.
This script initializes the game engine with data loaded from a JSON or YAML file and starts the game.
'''
import game_engine
import data_loader
def main():
    # Load game data from JSON or YAML file
    game_data = data_loader.load_game_data('data.json')  # You can change this to 'data.yaml' to test YAML support
    # Initialize the game engine with the loaded data
    engine = game_engine.GameEngine(game_data)
    # Start the game
    engine.start()
if __name__ == '__main__':
    main()