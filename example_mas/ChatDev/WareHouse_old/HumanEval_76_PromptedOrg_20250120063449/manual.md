manual.md

```
# Simple Power Checker

This software provides a function to determine if a number `x` is a simple power of another number `n`. A number `x` is considered a simple power of `n` if there exists an integer `k` such that `n**k = x`.

## Main Function

The main function provided by this software is:

- `is_simple_power(x, n)`: This function takes two arguments, `x` and `n`, and returns `True` if `x` is a simple power of `n`, and `False` otherwise.

### Examples

- `is_simple_power(1, 4)` returns `True`
- `is_simple_power(2, 2)` returns `True`
- `is_simple_power(8, 2)` returns `True`
- `is_simple_power(3, 2)` returns `False`
- `is_simple_power(3, 1)` returns `False`
- `is_simple_power(5, 3)` returns `False`

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

### Quick Start

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Change your current directory to the cloned repository:

   ```
   cd <repository-directory>
   ```

3. **Run the Code:**

   You can run the `main.py` file directly to test the function:

   ```python
   python main.py
   ```

## Usage

To use the `is_simple_power` function in your own projects, you can import it from the `main.py` file:

```python
from main import is_simple_power

# Example usage
result = is_simple_power(8, 2)
print(result)  # Output: True
```

## Documentation

For further information on how to use the function, please refer to the inline comments and docstrings within the `main.py` file.

```