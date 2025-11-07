'''
Module containing the RecipeManager class.
Handles operations related to recipes.
'''
import json
from recipe import Recipe
from storage import Storage
class RecipeManager:
    def __init__(self):
        '''
        Initializes the RecipeManager by loading recipes from storage.
        '''
        self.storage = Storage()
        self.recipes = self.storage.load_recipes()
    def add_recipe(self, name, ingredients, instructions):
        '''
        Adds a new recipe to the manager and saves it to storage.
        :param name: Name of the recipe.
        :param ingredients: List of ingredients for the recipe.
        :param instructions: Instructions for the recipe.
        '''
        recipe = Recipe(name, ingredients, instructions)
        self.recipes.append(recipe)
        self.storage.save_recipes(self.recipes)
        print("Recipe added successfully.")
    def search_recipes_by_name(self, name):
        '''
        Searches for recipes by name.
        :param name: Name to search for.
        :return: List of recipes matching the search term.
        '''
        if not name.strip():
            return []
        return [recipe for recipe in self.recipes if name.lower() in recipe.name.lower()]
    def search_recipes_by_ingredient(self, ingredient):
        '''
        Searches for recipes by ingredient.
        :param ingredient: Ingredient to search for.
        :return: List of recipes containing the ingredient.
        '''
        if not ingredient.strip():
            return []
        return [recipe for recipe in self.recipes if ingredient.lower() in [ing.lower() for ing in recipe.ingredients]]
    def view_recipe(self, name):
        '''
        Retrieves a recipe by name.
        :param name: Name of the recipe to retrieve.
        :return: Recipe object if found, otherwise None.
        '''
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                return recipe
        return None