'''
Main file for the CLI recipe manager.
Handles user input and interacts with the RecipeManager class.
'''
import json
from recipe_manager import RecipeManager
def main():
    recipe_manager = RecipeManager()
    while True:
        print("\nRecipe Manager")
        print("1. Add Recipe")
        print("2. Search Recipes by Name")
        print("3. Search Recipes by Ingredient")
        print("4. View Recipe Details")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            instructions = input("Enter instructions: ")
            recipe_manager.add_recipe(name, ingredients, instructions)
        elif choice == '2':
            name = input("Enter recipe name to search: ")
            recipes = recipe_manager.search_recipes_by_name(name)
            if not recipes:
                print("No recipes found with that name.")
            for recipe in recipes:
                print(recipe)
        elif choice == '3':
            ingredient = input("Enter ingredient to search: ")
            recipes = recipe_manager.search_recipes_by_ingredient(ingredient)
            if not recipes:
                print("No recipes found with that ingredient.")
            for recipe in recipes:
                print(recipe)
        elif choice == '4':
            name = input("Enter recipe name to view: ")
            recipe = recipe_manager.view_recipe(name)
            if recipe:
                print(recipe)
            else:
                print("Recipe not found.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()