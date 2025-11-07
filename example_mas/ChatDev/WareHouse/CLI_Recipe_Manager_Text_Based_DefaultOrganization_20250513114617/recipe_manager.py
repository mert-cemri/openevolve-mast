'''
Manages the collection of recipes, including adding, searching, and retrieving recipes.
'''
import json
from recipe import Recipe
class RecipeManager:
    def __init__(self):
        self.recipes = []
        self.load_recipes()
    def add_recipe(self, name, ingredients, instructions):
        recipe = Recipe(name, ingredients, instructions)
        self.recipes.append(recipe)
    def search_recipes(self, query):
        return [recipe for recipe in self.recipes if query.lower() in recipe.name.lower() or any(query.lower() in ingredient.lower() for ingredient in recipe.ingredients)]
    def load_recipes(self):
        try:
            with open('recipes.json', 'r') as file:
                recipes_data = json.load(file)
                self.recipes = [Recipe(**data) for data in recipes_data]
        except FileNotFoundError:
            self.recipes = []
    def save_recipes(self):
        with open('recipes.json', 'w') as file:
            json.dump([recipe.to_dict() for recipe in self.recipes], file, indent=4)