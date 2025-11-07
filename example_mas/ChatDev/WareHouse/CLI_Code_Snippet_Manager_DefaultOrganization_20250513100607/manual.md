```markdown
# CLI Code Snippet Manager

A command-line interface (CLI) application to manage your frequently used code snippets. This tool allows you to save, categorize, search, and retrieve code snippets efficiently, storing them in local files for easy access.

## Main Features

- **Add Snippets**: Save new code snippets with associated language and description.
- **Search Snippets**: Search for snippets by language or description.
- **Retrieve Snippets**: Retrieve a specific snippet by its index.
- **Graphical User Interface (GUI)**: An optional GUI is available for users who prefer a visual interface.

## Installation

### Prerequisites

- Ensure you have Python 3.x installed on your system.

### Installation Steps

1. **Clone the Repository**: Download the source code from the repository.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Although there are no external packages required, ensure your Python environment is set up correctly.
   ```bash
   # No external packages required
   # Ensure Python 3.x is used
   ```

3. **Prepare the Environment**: Make sure the `snippets.json` file is present in the directory. This file is used to store your code snippets.

## Usage

### Command-Line Interface

1. **Add a Snippet**:
   ```bash
   python main.py add --language <language> --description <description> --code <code>
   ```
   - Replace `<language>`, `<description>`, and `<code>` with your snippet details.

2. **Search for Snippets**:
   ```bash
   python main.py search --query <search-query>
   ```
   - Replace `<search-query>` with the keyword you want to search for in the snippets.

3. **Retrieve a Snippet**:
   ```bash
   python main.py retrieve --index <snippet-index>
   ```
   - Replace `<snippet-index>` with the index number of the snippet you want to retrieve.

### Graphical User Interface

1. **Launch the GUI**:
   ```bash
   python gui.py
   ```

2. **Add a Snippet**:
   - Click on "Add Snippet" and fill in the language, description, and code snippet in the dialog boxes.

3. **Search for Snippets**:
   - Enter a search query in the search box and click "Search" to display matching snippets.

4. **View Snippets**:
   - The list box will display the snippets. Click on any snippet to view its details.

## Documentation

For more detailed documentation, please refer to the source code comments and docstrings within the Python files. These provide insights into the functionality and structure of the application.

## Support

For support or further inquiries, please contact the development team at ChatDev. We are committed to assisting you in making the most out of this application.
```
