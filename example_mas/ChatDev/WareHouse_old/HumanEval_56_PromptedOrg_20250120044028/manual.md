# Correct Bracketing

This software provides a function to check if a string of brackets is correctly balanced. It is designed to work with strings containing the characters "<" and ">". The function ensures that every opening bracket has a corresponding closing bracket.

## Main Functionality

The main function provided by this software is `correct_bracketing`. This function takes a string of brackets as input and returns a boolean value indicating whether the brackets are correctly balanced.

### Function Definition

```python
def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.
    """
```

### Example Usage

```python
>>> correct_bracketing("<")
False
>>> correct_bracketing("<>")
True
>>> correct_bracketing("<<><>>")
True
>>> correct_bracketing("><<>")
False
```

## Installation

This software does not require any external packages. It is implemented in Python and requires Python version 3.6 or higher. You can optionally specify the Python version in your environment.

### Setting Up the Environment

1. **Ensure Python is Installed**: Make sure you have Python 3.6 or higher installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Create a Virtual Environment (Optional)**: It is recommended to create a virtual environment to manage dependencies. You can create a virtual environment using the following command:

   ```bash
   python -m venv myenv
   ```

3. **Activate the Virtual Environment**:

   - On Windows:

     ```bash
     myenv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source myenv/bin/activate
     ```

4. **Install Dependencies**: There are no external dependencies required for this software. However, you can specify the Python version in a `requirements.txt` file if needed.

   ```plaintext
   # requirements.txt
   # No external packages required
   # Optionally specify Python version
   # python_version >= "3.6"
   ```

## Usage

To use the `correct_bracketing` function, simply import it into your Python script and call it with a string of brackets as the argument. The function will return `True` if the brackets are correctly balanced and `False` otherwise.

```python
from main import correct_bracketing

result = correct_bracketing("<<><>>")
print(result)  # Output: True
```

This software is designed to be simple and efficient, providing a straightforward solution to check the balance of brackets in a string.