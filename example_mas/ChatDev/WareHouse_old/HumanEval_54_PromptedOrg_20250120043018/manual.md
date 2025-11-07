# Same Characters Checker

This software provides a simple function to check if two words have the same characters, regardless of their frequency or order. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function provided by this software is `same_chars`, which takes two strings as input and returns a boolean indicating whether the two strings contain the same characters.

### Function Signature

```python
def same_chars(s0: str, s1: str) -> bool:
```

### Example Usage

```python
>>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
True
>>> same_chars('abcd', 'dddddddabc')
True
>>> same_chars('dddddddabc', 'abcd')
True
>>> same_chars('eabcd', 'dddddddabc')
False
>>> same_chars('abcd', 'dddddddabce')
False
>>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
False
```

## Installation

This software does not require any external dependencies. You only need to have Python installed on your system.

### Installing Python

If you do not have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/). Follow the instructions for your operating system to install Python.

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can run the function in a Python environment by importing it and passing the desired strings as arguments.

   ```python
   from main import same_chars

   result = same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
   print(result)  # Output: True
   ```

## Documentation

For further details on how the function works, refer to the docstring within the `main.py` file. It includes example usages and expected outputs.

This software is designed to be simple and straightforward, making it easy to integrate into larger projects or use as a standalone utility for checking character equivalence between strings.