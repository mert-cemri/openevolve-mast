# ModP Function User Manual

This user manual provides detailed instructions on how to use the `modp` function, which calculates \(2^n \mod p\). This function is implemented in Python and is designed to be simple and efficient.

## Overview

The `modp` function computes the result of \(2^n \mod p\), which is a common operation in modular arithmetic. This function can be useful in various applications, including cryptography, computer science, and number theory.

## Quick Install

No external dependencies are required to use the `modp` function. You only need Python installed on your system.

### Prerequisites

- Python 3.x

### Installation

1. **Ensure Python is installed**: You can download and install Python from the [official Python website](https://www.python.org/downloads/).

2. **Clone or download the repository**: You can clone the repository using Git or download the ZIP file and extract it.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:

   ```bash
   cd <project-directory>
   ```

## How to Use

The `modp` function is defined in the `main.py` file. You can use this function by importing it into your Python script or by running the `main.py` file directly.

### Function Definition

```python
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p."""
    return pow(2, n, p)
```

### Usage Example

You can use the `modp` function in your Python script as follows:

```python
from main import modp

# Example usage
result = modp(3, 5)
print(result)  # Output: 3

result = modp(1101, 101)
print(result)  # Output: 2

result = modp(0, 101)
print(result)  # Output: 1

result = modp(3, 11)
print(result)  # Output: 8

result = modp(100, 101)
print(result)  # Output: 1
```

### Running Tests

The function includes several test cases in the docstring. You can run these tests using Python's built-in `doctest` module to ensure the function works as expected.

```bash
python -m doctest main.py
```

## Documentation

For further information and documentation, please refer to the comments and docstrings within the `main.py` file. The function is straightforward and does not require additional libraries or frameworks.

## Support

If you encounter any issues or have questions about using the `modp` function, please feel free to reach out through the project's issue tracker or contact the support team.

---

This manual provides all necessary information to effectively use the `modp` function. Enjoy using the software, and feel free to contribute to its development!