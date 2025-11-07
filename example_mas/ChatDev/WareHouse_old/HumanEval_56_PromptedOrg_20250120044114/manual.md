# Correct Bracketing

This software module provides a function to check if a string of brackets is correctly matched. It is designed to ensure that every opening bracket ("<") has a corresponding closing bracket (">").

## Main Functionality

The main function provided by this module is `correct_bracketing`, which takes a string of brackets as input and returns a boolean value indicating whether the brackets are correctly matched.

### Function: `correct_bracketing`

- **Input**: A string consisting of the characters "<" and ">".
- **Output**: Returns `True` if every opening bracket has a corresponding closing bracket, otherwise returns `False`.

#### Examples

```python
correct_bracketing("<")        # Output: False
correct_bracketing("<>")       # Output: True
correct_bracketing("<<><>>")   # Output: True
correct_bracketing("><<>")     # Output: False
```

## Installation

This project does not require any external dependencies, making it simple and easy to use. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the project files to your local machine.

3. Navigate to the project directory.

4. Run the Python script using your preferred Python environment.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the script using Python:

   ```bash
   python main.py
   ```

4. You can test the function by calling it with different strings of brackets as shown in the examples above.

## Documentation

This module is self-contained and does not require additional documentation beyond what is provided here. The function is straightforward and designed to be used in any Python environment without additional setup.

For any further questions or support, please contact our support team.