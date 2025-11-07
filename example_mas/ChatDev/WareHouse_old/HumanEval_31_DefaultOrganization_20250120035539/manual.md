# Prime Checker

A simple Python module to determine if a number is prime.

## Introduction

This software provides a single function, `is_prime(n)`, which checks if a given number `n` is a prime number. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

## Main Function

### `is_prime(n)`

- **Description**: Determines if the input number `n` is a prime number.
- **Parameters**: 
  - `n` (int): The number to be checked.
- **Returns**: 
  - `bool`: `True` if `n` is a prime number, `False` otherwise.
- **Examples**:
  ```python
  >>> is_prime(6)
  False
  >>> is_prime(101)
  True
  >>> is_prime(11)
  True
  >>> is_prime(13441)
  True
  >>> is_prime(61)
  True
  >>> is_prime(4)
  False
  >>> is_prime(1)
  False
  ```

## Installation

This project does not require any external dependencies. You only need Python installed on your system.

### Step-by-Step Installation

1. **Ensure Python is installed**: 
   - You can download Python from the official website: [Python.org](https://www.python.org/downloads/).
   - Verify the installation by running `python --version` in your terminal or command prompt.

2. **Clone or download the repository**:
   - Clone the repository using Git:
     ```bash
     git clone <repository-url>
     ```
   - Or download the ZIP file from the repository page and extract it.

3. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

## Usage

1. **Open the terminal or command prompt**.

2. **Navigate to the directory containing `main.py`**:
   ```bash
   cd <path-to-main.py>
   ```

3. **Run the Python script**:
   - You can directly use the `is_prime` function in a Python interactive shell or within another script.
   - Example usage in a Python shell:
     ```python
     from main import is_prime
     print(is_prime(29))  # Output: True
     ```

## Documentation

For further information and examples, please refer to the docstring within the `main.py` file. The function is thoroughly documented with examples to guide you through its usage.

## Support

For any issues or questions, please contact our support team or open an issue in the repository.

---

This manual provides all necessary information to install, use, and understand the functionality of the Prime Checker software. Enjoy determining prime numbers efficiently!