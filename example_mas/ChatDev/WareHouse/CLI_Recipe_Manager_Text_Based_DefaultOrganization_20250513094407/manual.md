```markdown
# CLI Recipe Manager

A simple command-line interface (CLI) application to manage your recipes. This application allows users to add recipes, search for recipes by name or ingredient, and view detailed recipe information. All data is stored in a JSON file for easy access and modification.

## Quick Install

This application does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## Installation

1. **Clone the Repository:**
   Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**
   Change into the project directory:
   ```bash
   cd <project-directory>
   ```
   Replace `<project-directory>` with the name of the directory where the repository was cloned.

3. **Run the Application:**
   Execute the main script to start the CLI Recipe Manager:
   ```bash
   python main.py
   ```

## 🤔 What is this?

The CLI Recipe Manager is a tool designed to help users organize and manage their recipes efficiently. It provides a simple interface for adding new recipes, searching for existing ones, and viewing detailed instructions and ingredients.

### Main Functions

- **Add Recipe:** Users can add new recipes by providing a name, a list of ingredients, and instructions.
- **Search Recipes:** Users can search for recipes by name or by specific ingredients.
- **View Recipe Details:** Users can view detailed information about a specific recipe, including its ingredients and instructions.

## 📖 How to Use

1. **Add a Recipe:**
   - Select the "Add Recipe" option from the main menu.
   - Enter the recipe name when prompted.
   - Provide a list of ingredients, separated by commas.
   - Enter the instructions for the recipe.
   - The recipe will be saved and confirmed with a success message.

2. **Search for Recipes:**
   - Select the "Search Recipes" option from the main menu.
   - Enter a search term, which can be a recipe name or an ingredient.
   - The application will display a list of matching recipes.
   - Select a recipe from the list to view its details.

3. **Exit the Application:**
   - Select the "Exit" option from the main menu to close the application.

## Data Storage

All recipes are stored in a JSON file named `recipes.json` in the project directory. This file is automatically created and updated by the application, ensuring that all your recipes are saved between sessions.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the repository.

```
