```markdown
# CLI Maze Generator

A command-line interface (CLI) application for generating and displaying mazes using text characters. This application allows users to specify the dimensions of the maze and outputs the maze to the console using '#' for walls and ' ' for paths.

## Main Functions

- **Maze Generation**: The application generates a maze using a randomized depth-first search algorithm.
- **Customizable Dimensions**: Users can specify the width and height of the maze.
- **Console Output**: The generated maze is displayed in the console as a 2D grid of characters.

## Quick Install

To run the CLI Maze Generator, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository**: Clone the repository containing the maze generator code to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your working directory to the location of the cloned repository.

   ```bash
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not require any external Python packages beyond the standard library, so no additional installations are necessary.

## How to Use

1. **Run the Application**: Use the command line to run the `main.py` script with the desired maze dimensions.

   ```bash
   python main.py <width> <height>
   ```

   Replace `<width>` and `<height>` with the desired dimensions of the maze. Both values should be integers.

2. **Example Usage**:

   To generate a maze with a width of 10 and a height of 5, execute the following command:

   ```bash
   python main.py 10 5
   ```

3. **Output**: The generated maze will be displayed in the console. The maze consists of walls represented by '#' and paths represented by spaces.

## Troubleshooting

- **Invalid Input**: If you enter non-integer values for width and height, the application will display an error message: "Invalid input. Please enter integers for width and height."

- **Incorrect Usage**: If you do not provide exactly two arguments for width and height, the application will display the usage instructions: "Usage: python main.py <width> <height>".

## Documentation

For more information on the implementation details and algorithm used in the maze generation, please refer to the comments within the source code files `maze_generator.py` and `main.py`.

## Support

For any issues or questions, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).
```
