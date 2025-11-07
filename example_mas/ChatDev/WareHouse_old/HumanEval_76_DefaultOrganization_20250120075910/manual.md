manual.md

```
# Simple Power Checker

This software provides a function to determine if a number \( x \) is a simple power of another number \( n \). A number \( x \) is considered a simple power of \( n \) if there exists an integer \( k \) such that \( n^k = x \).

## Main Functionality

The main functionality of this software is encapsulated in the `is_simple_power` function. This function checks whether a given number \( x \) is a simple power of another number \( n \).

### Function Definition

```python
def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n, and false otherwise."""
```

### Example Usage

- `is_simple_power(1, 4)` returns `True`
- `is_simple_power(2, 2)` returns `True`
- `is_simple_power(8, 2)` returns `True`
- `is_simple_power(3, 2)` returns `False`
- `is_simple_power(3, 1)` returns `False`
- `is_simple_power(5, 3)` returns `False`

## Installation

This project does not require any external dependencies. The function is implemented in pure Python, and you can use it directly in your Python environment.

### Quick Start

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd <project-directory>
   ```

3. **Run the Function**

   You can run the function by importing it into your Python script or interactive shell:

   ```python
   from main import is_simple_power

   # Example usage
   print(is_simple_power(8, 2))  # Output: True
   ```

## How to Use

1. **Import the Function**

   Ensure you have the `main.py` file in your project directory. Import the `is_simple_power` function into your script:

   ```python
   from main import is_simple_power
   ```

2. **Call the Function**

   Pass the numbers \( x \) and \( n \) as arguments to the function to determine if \( x \) is a simple power of \( n \).

   ```python
   result = is_simple_power(8, 2)
   print(result)  # Output: True
   ```

## Documentation

For further details on the implementation and usage, please refer to the comments within the `main.py` file. The function is straightforward and designed to be easily integrated into larger projects.

```