'''
Represents a single recipe with attributes like name, ingredients, and instructions.
'''
class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
    def to_dict(self):
        return {
            'name': self.name,
            'ingredients': self.ingredients,
            'instructions': self.instructions
        }