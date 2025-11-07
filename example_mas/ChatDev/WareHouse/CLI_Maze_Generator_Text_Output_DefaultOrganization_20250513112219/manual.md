# Maze Generator CLI

Welcome to the Maze Generator CLI! This application allows you to generate a maze using text characters directly in your console. The maze is generated using the Recursive Backtracking algorithm, and you can specify the dimensions of the maze.

## Main Functions

- **Maze Generation**: Generates a maze using the Recursive Backtracking algorithm, represented by '#' for walls and ' ' for paths.
- **Customizable Dimensions**: Allows you to specify the width and height of the maze to suit your needs.

## Installation

### Environment Setup

This project does not require any external dependencies, making it easy to set up and run. You only need Python installed on your system.

### Quick Install

1. **Clone the Repository**: First, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can check this by running:
   ```bash
   python --version
   ```

3. **No Additional Dependencies**: There are no additional dependencies required for this project, as indicated in the `requirements.txt` file.

## Usage

### Running the Maze Generator

To generate a maze, you need to run the `main.py` script from the command line. You will need to provide the width and height of the maze as command-line arguments.

#### Command Syntax

```bash
python main.py <width> <height>
```

- `<width>`: The width of the maze (must be an integer).
- `<height>`: The height of the maze (must be an integer).

#### Example

To generate a maze of width 10 and height 5, run the following command:

```bash
python main.py 10 5
```

This will output a randomly generated maze to the console, using '#' for walls and ' ' for paths.

### Error Handling

- If you do not provide the correct number of arguments, the program will display a usage message:
  ```
  Usage: python main.py <width> <height>
  ```

- If the width or height is not a valid integer, the program will display an error message:
  ```
  Width and height must be integers.
  ```

## Conclusion

The Maze Generator CLI is a simple yet powerful tool for generating mazes directly in your console. With customizable dimensions and no external dependencies, it's easy to set up and use. Enjoy exploring the mazes you create!