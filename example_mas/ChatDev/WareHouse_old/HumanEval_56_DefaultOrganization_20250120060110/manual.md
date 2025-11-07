# Correct Bracketing

This software provides a simple function to check if a string of brackets is correctly balanced. It is designed to determine whether every opening bracket ("<") has a corresponding closing bracket (">").

## Main Functionality

The main function of this software is `correct_bracketing`, which takes a string of brackets as input and returns a boolean value indicating whether the brackets are correctly balanced.

### Function: `correct_bracketing`

- **Input**: A string consisting of the characters "<" and ">".
- **Output**: Returns `True` if every opening bracket has a corresponding closing bracket, otherwise returns `False`.

#### Examples

```python
correct_bracketing("<")       # Returns: False
correct_bracketing("<>")      # Returns: True
correct_bracketing("<<><>>")  # Returns: True
correct_bracketing("><<>")    # Returns: False
```

## Installation

This project does not require any external dependencies, so you can use it directly in your Python environment. However, it is recommended to use a virtual environment to manage your Python packages.

### Setting Up a Virtual Environment

1. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   Since there are no external dependencies, you can skip this step. However, if you want to ensure your environment is clean, you can create a `requirements.txt` file with the following content:

   ```plaintext
   # No external dependencies required for this project
   ```

   Then, install the requirements (if any):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the `correct_bracketing` function, you can import it into your Python script and call it with the desired input string:

```python
from main import correct_bracketing

# Example usage
result = correct_bracketing("<<><>>")
print(result)  # Output: True
```

## Conclusion

This software provides a straightforward solution to check the balance of brackets in a string. It is easy to integrate into any Python project and does not require any additional setup beyond a basic Python environment.