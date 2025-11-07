'''
Creates the CLI for the recipe manager.
'''
from recipe_manager import RecipeManager
class RecipeApp:
    def __init__(self):
        self.manager = RecipeManager()
    def run(self):
        while True:
            print("\nRecipe Manager")
            print("1. Add Recipe")
            print("2. Search Recipes")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_recipe_cli()
            elif choice == '2':
                self.search_recipes_cli()
            elif choice == '3':
                print("Exiting Recipe Manager.")
                break
            else:
                print("Invalid choice. Please try again.")
    def add_recipe_cli(self):
        name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients (comma separated): ").split(',')
        instructions = input("Enter instructions: ")
        self.manager.add_recipe(name, ingredients, instructions)
        print("Recipe added successfully!")
    def search_recipes_cli(self):
        search_term = input("Enter recipe name or ingredient to search: ")
        results_by_name = self.manager.search_recipes_by_name(search_term)
        results_by_ingredient = self.manager.search_recipes_by_ingredient(search_term)
        results = {**results_by_name, **results_by_ingredient}
        if not results:
            print("No recipes found.")
            return
        print("Found recipes:")
        for recipe_name in results.keys():
            print(f"- {recipe_name}")
        selected_recipe = input("Enter recipe name to view details: ")
        if selected_recipe in results:
            self.view_recipe_details_cli(selected_recipe)
        else:
            print("Recipe not found.")
    def view_recipe_details_cli(self, name):
        details = self.manager.get_recipe_details(name)
        if details:
            ingredients = ", ".join(details['ingredients'])
            instructions = details['instructions']
            print(f"\nRecipe Details:\nName: {name}\nIngredients: {ingredients}\nInstructions: {instructions}")
        else:
            print("Recipe not found.")