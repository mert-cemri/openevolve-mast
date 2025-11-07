# Correct Bracketing

This software provides a function to check if a string of brackets is correctly matched. It ensures that every opening bracket ("<") has a corresponding closing bracket (">").

## Main Function

The main function provided by this software is `correct_bracketing`. This function takes a string of brackets as input and returns a boolean value indicating whether the brackets are correctly matched.

### Function Signature

```python
def correct_bracketing(brackets: str) -> bool:
```

### Parameters

- `brackets`: A string consisting of the characters "<" and ">".

### Returns

- `True` if every opening bracket has a corresponding closing bracket.
- `False` otherwise.

### Examples

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

This software does not require any external dependencies. It is implemented purely in Python and can be run in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

## Usage

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your working directory to where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can run the function by executing the `main.py` file in a Python environment.

   ```bash
   python main.py
   ```

4. **Test the Function**: You can test the function using the provided examples or by passing your own string of brackets.

## Documentation

This software is straightforward and does not require extensive documentation. The primary function is `correct_bracketing`, which is well-documented within the code itself.

For any further questions or support, please contact our support team.

---

This manual provides all necessary information to understand, install, and use the `correct_bracketing` function effectively. Enjoy using the software to ensure your brackets are always correctly matched!