'''
Module containing the Storage class.
Handles loading and saving recipes to a JSON file.
'''
import json
from recipe import Recipe
class Storage:
    def __init__(self, filename='recipes.json'):
        '''
        Initializes the Storage object with a filename.
        :param filename: Name of the file to store recipes.
        '''
        self.filename = filename
    def load_recipes(self):
        '''
        Loads recipes from the JSON file.
        :return: List of Recipe objects.
        '''
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Recipe(**recipe) for recipe in data]
        except FileNotFoundError:
            return []
    def save_recipes(self, recipes):
        '''
        Saves recipes to the JSON file.
        :param recipes: List of Recipe objects to save.
        '''
        with open(self.filename, 'w') as file:
            json.dump([recipe.__dict__ for recipe in recipes], file, indent=4)