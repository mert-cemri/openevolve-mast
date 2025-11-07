# CLI Recipe Manager

## Introduction

The CLI Recipe Manager is a command-line interface application designed to help users manage their recipes efficiently. It allows users to add new recipes, search for recipes by name or ingredient, and view detailed information about specific recipes. All recipe data is stored in a JSON file, making it easy to access and modify.

## Quick Install

To install the CLI Recipe Manager, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the source code. Navigate to the project directory and install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

Note: At this time, there are no external dependencies other than Python's built-in libraries, so the `requirements.txt` file might be empty or not necessary. However, it's a good practice to include it for future updates.

## 🤔 What is this?

The CLI Recipe Manager is a simple yet powerful tool for managing recipes. It provides a straightforward interface for adding, searching, and viewing recipes. The application is designed to be user-friendly and efficient, allowing users to focus on cooking without worrying about managing their recipes.

## 📖 Documentation

### Main Functions

1. **Add Recipe**
   - Allows users to add a new recipe by providing the recipe name, ingredients, and instructions.
   - Ingredients should be entered as a comma-separated list.

2. **Search Recipes by Name**
   - Enables users to search for recipes by entering the recipe name.
   - The search is case-insensitive and returns all recipes that match the search term.

3. **Search Recipes by Ingredient**
   - Allows users to search for recipes by entering an ingredient.
   - The search is case-insensitive and returns all recipes that contain the specified ingredient.

4. **View Recipe Details**
   - Provides detailed information about a specific recipe, including the name, ingredients, and instructions.

5. **Exit**
   - Exits the application.

### How to Use

1. **Run the Application**
   - Open a terminal or command prompt.
   - Navigate to the project directory.
   - Run the application using the following command:

     ```bash
     python main.py
     ```

2. **Add a Recipe**
   - Select option 1 from the main menu.
   - Enter the recipe name, ingredients (comma-separated), and instructions when prompted.

3. **Search Recipes by Name**
   - Select option 2 from the main menu.
   - Enter the recipe name to search for.
   - The application will display all recipes that match the search term.

4. **Search Recipes by Ingredient**
   - Select option 3 from the main menu.
   - Enter the ingredient to search for.
   - The application will display all recipes that contain the specified ingredient.

5. **View Recipe Details**
   - Select option 4 from the main menu.
   - Enter the recipe name to view.
   - The application will display detailed information about the specified recipe.

6. **Exit the Application**
   - Select option 5 from the main menu.
   - The application will exit.

### Data Storage

All recipe data is stored in a JSON file named `recipes.json`. This file is automatically created in the project directory when the application is run for the first time. Users can manually edit this file if needed, but it is recommended to use the application's interface to manage recipes.

## 🛠️ Development

If you are interested in contributing to the development of the CLI Recipe Manager, you can find the source code on [GitHub](https://github.com/your-repo/cli-recipe-manager). Feel free to submit issues, pull requests, or feature requests.

## 📧 Support

For any questions or issues, please contact us at [support@chatdev.com](mailto:support@chatdev.com).

---

This manual provides a comprehensive overview of the CLI Recipe Manager, including installation instructions, main functions, and usage instructions. We hope you find it helpful and enjoy using the application!