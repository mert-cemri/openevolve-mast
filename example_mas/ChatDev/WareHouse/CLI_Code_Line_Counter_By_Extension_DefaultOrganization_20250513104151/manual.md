```markdown
# Code Line Counter

A CLI and GUI application for counting lines of code in a directory, categorized by file extension. This tool helps developers quickly assess the size of their codebase by counting the lines of code while ignoring comments and blank lines.

## Main Functions

- **CLI Mode**: Count lines of code in a specified directory using the command line interface.
- **GUI Mode**: Use a graphical user interface to select a directory and view the results.

## Quick Install

### Prerequisites

- Python 3.x installed on your system.
- Ensure `tkinter` is installed if you wish to use the GUI component.

### Installation

1. **Clone the Repository**: Clone the project repository from your version control system.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up Environment**: No third-party dependencies are required, but ensure `tkinter` is available for GUI usage.

   ```bash
   # If tkinter is not installed, you can install it using your package manager.
   # For example, on Ubuntu:
   sudo apt-get install python3-tk
   ```

## How to Use

### CLI Mode

1. **Navigate to the Project Directory**: Open your terminal and navigate to the directory where the project is located.

   ```bash
   cd <repository-directory>
   ```

2. **Run the CLI Program**: Use the following command to run the CLI program and count lines of code in a specified directory.

   ```bash
   python main.py <directory-path>
   ```

   Replace `<directory-path>` with the path to the directory you want to analyze.

### GUI Mode

1. **Run the GUI Program**: Execute the following command to launch the graphical user interface.

   ```bash
   python gui.py
   ```

2. **Select a Directory**: Use the "Browse" button to select the directory you want to analyze.

3. **View Results**: The results will be displayed in the text area, showing the count of lines for each file extension.

## Documentation

For further details on how the application works, please refer to the source code files:

- `main.py`: Entry point for the CLI application.
- `code_counter.py`: Contains the logic for counting lines of code.
- `gui.py`: Provides the graphical user interface for the application.

Feel free to explore and modify the code to suit your needs. If you encounter any issues or have questions, please reach out to our support team.

```