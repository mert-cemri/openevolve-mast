'''
GameDataLoader class to load game data from a JSON file.
'''
import json
class GameDataLoader:
    @staticmethod
    def load_data(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)