'''
Module containing the Recipe class.
Represents a recipe with name, ingredients, and instructions.
'''
class Recipe:
    def __init__(self, name, ingredients, instructions):
        '''
        Initializes a new Recipe object.
        :param name: Name of the recipe.
        :param ingredients: List of ingredients for the recipe.
        :param instructions: Instructions for the recipe.
        '''
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
    def __str__(self):
        '''
        Returns a string representation of the recipe.
        :return: String representation of the recipe.
        '''
        ingredients_str = ', '.join(self.ingredients).replace(',', ', ')
        return f"Name: {self.name}\nIngredients: {ingredients_str}\nInstructions: {self.instructions}"