# CycPattern Check

This software provides a function to check if any rotation of a second word is a substring of a first word. It is a simple utility function written in Python, designed to solve a specific problem efficiently.

## Main Function

The main function provided by this software is `cycpattern_check`. This function takes two words as input and returns `True` if any rotation of the second word is a substring of the first word, otherwise it returns `False`.

### Function Definition

```python
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    # Generate all rotations of the second word
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        # Check if the rotated version is a substring of the first word
        if rotated_b in a:
            return True
    return False
```

### Example Usage

- `cycpattern_check("abcd", "abd")` returns `False`
- `cycpattern_check("hello", "ell")` returns `True`
- `cycpattern_check("whassup", "psus")` returns `False`
- `cycpattern_check("abab", "baa")` returns `True`
- `cycpattern_check("efef", "eeff")` returns `False`
- `cycpattern_check("himenss", "simen")` returns `True`

## Installation

This software does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are needed as there are no external dependencies.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run a Python interpreter and import the function:

   ```bash
   python
   ```

   ```python
   from main import cycpattern_check
   ```

4. Use the function by passing two words as arguments:

   ```python
   result = cycpattern_check("hello", "ell")
   print(result)  # Output: True
   ```

This function is useful for applications where pattern matching with rotated strings is required, such as in certain text processing or cryptographic applications.