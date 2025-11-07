'''
Main entry point for the CLI Recipe Manager application.
'''
from recipe_app import RecipeApp
def main():
    app = RecipeApp()
    app.run()
if __name__ == "__main__":
    main()