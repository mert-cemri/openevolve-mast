manual.md

```
# Prime Multiplication Checker

This software provides a simple function to determine if a given number is the product of exactly three prime numbers. It is designed to work with numbers less than 100.

## Main Function

The core functionality of this software is encapsulated in the `is_multiply_prime` function. This function takes an integer input and returns `True` if the number is the product of exactly three prime numbers, and `False` otherwise.

### Function Definition

```python
def is_multiply_prime(a):
    """
    Returns True if the given number is the multiplication of 3 prime numbers
    and False otherwise.
    Knowing that (a) is less than 100.
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
```

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted on a version control system like GitHub, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change your working directory to the location where the project files are stored.

   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can directly run the `main.py` file to test the function.

   ```bash
   python main.py
   ```

## Usage

To use the `is_multiply_prime` function, you simply need to call it with an integer argument. The function will return a boolean value indicating whether the number is the product of exactly three prime numbers.

### Example Usage

```python
result = is_multiply_prime(30)
print(result)  # Output: True

result = is_multiply_prime(28)
print(result)  # Output: False
```

## Additional Information

- **Limitations**: The function is designed to work with numbers less than 100. It uses a predefined list of prime numbers under 10 to check combinations.

- **No External Libraries Required**: This project is self-contained and does not require any additional Python packages.

- **Modifications**: If you wish to extend the functionality to numbers greater than 100, you will need to modify the list of prime numbers and potentially the logic for checking combinations.

This manual provides all necessary information to understand, install, and use the Prime Multiplication Checker software effectively.
```