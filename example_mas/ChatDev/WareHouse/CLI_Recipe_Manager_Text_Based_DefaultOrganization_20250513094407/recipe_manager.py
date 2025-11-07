'''
Handles recipe operations such as adding, searching, and retrieving recipes.
'''
import json
import os
class RecipeManager:
    def __init__(self, filename='recipes.json'):
        self.filename = filename
        self.recipes = self.load_recipes()
    def add_recipe(self, name, ingredients, instructions):
        self.recipes[name] = {
            'ingredients': ingredients,
            'instructions': instructions
        }
        self.save_recipes()
    def search_recipes_by_name(self, name):
        return {k: v for k, v in self.recipes.items() if name.lower() in k.lower()}
    def search_recipes_by_ingredient(self, ingredient):
        return {k: v for k, v in self.recipes.items() if ingredient.lower() in [i.lower() for i in v['ingredients']]}
    def get_recipe_details(self, name):
        return self.recipes.get(name)
    def load_recipes(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}
    def save_recipes(self):
        with open(self.filename, 'w') as file:
            json.dump(self.recipes, file, indent=4)