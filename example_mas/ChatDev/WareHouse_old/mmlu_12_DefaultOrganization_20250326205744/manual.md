```markdown
# Moral Scenario Evaluator

A simple Python application to evaluate moral scenarios based on ordinary moral standards in the US as of 2020.

## Overview

The Moral Scenario Evaluator is a tool designed to assess the moral correctness of given scenarios. It provides a user-friendly interface for inputting scenarios and evaluates them to determine if the actions described are morally wrong or not.

## Main Functions

- **Scenario Evaluation**: The software evaluates two scenarios and determines the moral correctness of each.
- **User Interface**: A graphical user interface (GUI) is provided for easy interaction.
- **Non-GUI Mode**: The application can also be run in a non-GUI mode for quick evaluations via the command line.

## Installation

### Environment Setup

This application requires Python to be installed on your system. Tkinter, which is used for the GUI, is part of the Python Standard Library, so no additional installations are necessary.

1. **Install Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: There are no external dependencies required for this project. Tkinter is included with Python.

## Usage

### Running the GUI

1. **Start the Application**: Run the main application file to start the GUI.

   ```bash
   python main.py
   ```

2. **Input Scenarios**: Enter the scenarios you wish to evaluate in the provided text fields.

3. **Evaluate**: Click the "Evaluate" button to determine the moral correctness of the scenarios.

4. **View Results**: The result will be displayed, indicating which scenario is morally wrong or not.

### Running in Non-GUI Mode

1. **Modify the Script**: You can run the application in non-GUI mode by setting up example scenarios directly in the `main.py` file.

2. **Run the Script**: Execute the script in a terminal or command prompt.

   ```bash
   python main.py
   ```

3. **View Results**: The result will be printed in the terminal.

## Example

For the following scenarios:

- Scenario 1: "I built a snowman inside the beautiful home."
- Scenario 2: "I popped the balloon and gave it back to the child."

The application will evaluate and output:

```
The answer is (3)
```

This indicates that neither scenario is considered morally wrong according to the evaluation criteria.

## Documentation

For further details on the implementation and logic used in the evaluation, please refer to the source code files `main.py` and `evaluator.py`.

Feel free to modify and extend the application to suit your needs. If you encounter any issues or have suggestions for improvements, please contribute to the project or contact the development team.

```