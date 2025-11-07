'''
Main application file for the CLI Recipe Manager.
'''
from recipe_manager import RecipeManager
class RecipeApp:
    def __init__(self):
        self.manager = RecipeManager()
    def run(self):
        while True:
            print("\nRecipe Manager CLI")
            print("1. Add Recipe")
            print("2. Search Recipes")
            print("3. View Recipe Details")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_recipe()
            elif choice == '2':
                self.search_recipes()
            elif choice == '3':
                self.view_recipe()
            elif choice == '4':
                print("Exiting the Recipe Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    def add_recipe(self):
        name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients (comma separated): ").split(',')
        instructions = input("Enter instructions: ")
        if name and ingredients and instructions:
            self.manager.add_recipe(name, ingredients, instructions)
            self.manager.save_recipes()
            print("Recipe added successfully!")
        else:
            print("Please fill all fields.")
    def search_recipes(self):
        query = input("Enter search query (name or ingredient): ")
        results = self.manager.search_recipes(query)
        if results:
            print("Search Results:")
            for index, recipe in enumerate(results):
                print(f"{index + 1}. {recipe.name}")
        else:
            print("No recipes found.")
    def view_recipe(self):
        try:
            index = int(input("Enter recipe number to view details: ")) - 1
            if 0 <= index < len(self.manager.recipes):
                selected_recipe = self.manager.recipes[index]
                print(f"\nRecipe: {selected_recipe.name}")
                print(f"Ingredients: {', '.join(selected_recipe.ingredients)}")
                print(f"Instructions: {selected_recipe.instructions}")
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
    app = RecipeApp()
    app.run()