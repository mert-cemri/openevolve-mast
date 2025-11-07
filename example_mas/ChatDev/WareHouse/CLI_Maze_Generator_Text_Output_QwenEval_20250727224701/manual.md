# Maze Generator CLI User Manual

## Introduction

Welcome to the Maze Generator CLI! This tool allows you to generate mazes of specified dimensions directly from your command line interface (CLI). The mazes are represented using text characters, where `#` denotes walls and ` ` (space) denotes paths. The generator uses a depth-first search algorithm to create the mazes, ensuring that they are solvable and have a single path from start to finish.

## Main Functions

### Maze Generation
- **Functionality**: Generates a maze based on user-specified dimensions.
- **Algorithm**: Depth-first search (DFS) algorithm.
- **Output**: A maze printed to the console using `#` for walls and ` ` for paths.

## Installation

### Prerequisites
- Python 3.6 or higher must be installed on your system.
- `pip` (Python package installer) must be installed.

### Steps to Install

1. **Clone the Repository** (if you haven't already):
   ```bash
   git clone https://github.com/your-repo/maze-generator-cli.git
   cd maze-generator-cli
   ```

2. **Install Dependencies**:
   The project currently does not have any external dependencies. However, if you have a `requirements.txt` file, you can install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Maze Generator

1. **Navigate to the Project Directory**:
   ```bash
   cd path/to/maze-generator-cli
   ```

2. **Run the CLI Application**:
   ```bash
   python main.py
   ```

3. **Input Maze Dimensions**:
   - When prompted, enter the desired width and height of the maze. **Note**: Both dimensions must be odd numbers to ensure the maze is properly generated.
   - Example:
     ```
     Enter maze width (odd number): 15
     Enter maze height (odd number): 15
     ```

4. **View the Generated Maze**:
   - The maze will be printed to the console using `#` for walls and ` ` for paths.
   - Example Output:
     ```
     ###################
     #                 #
     # ### ##### ### ###
     # # ### #   # # ###
     # # ### ### ### ###
     # # ### #   #   ###
     # ### ### ### ### #
     # #   #   #   #   #
     # ### ### ### ### #
     # #   #   #   #   #
     # ### ### ### ### #
     # #   #   #   #   #
     # ### ### ### ### #
     #                 #
     ###################
     ```

### Error Handling
- If you enter an even number for the width or height, the program will display an error message and terminate.
- Example Error Message:
  ```
  Invalid input: Width and height must be odd numbers.
  ```

## Additional Notes

- **GUI Interface**: While the primary focus is on the CLI, a graphical user interface (GUI) is also available in the `gui_interface.py` file. This can be run using a Python GUI library like `tkinter`.
- **Customization**: You can modify the `maze.py` file to change the characters used for walls and paths, or to implement different maze generation algorithms.

## Conclusion

Thank you for using the Maze Generator CLI! We hope you find it useful for generating mazes for various applications, from educational purposes to game development. If you have any questions or encounter any issues, feel free to reach out to our support team.

---

This manual provides a comprehensive overview of the Maze Generator CLI, including its main functions, installation process, and usage instructions. It is designed to be user-friendly and informative, ensuring that users can quickly get started with generating mazes.