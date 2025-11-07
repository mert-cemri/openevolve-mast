manual.md

```
# Prime Number Finder

This software provides a simple utility to find all prime numbers less than a given non-negative integer. It is implemented in Python and is designed to be straightforward and efficient for small to medium-sized inputs.

## Main Functions

The core functionality of this software is encapsulated in the `count_up_to` function, which returns an array of prime numbers less than a specified integer `n`.

### Function: `count_up_to(n)`

- **Description**: Takes a non-negative integer `n` and returns a list of all prime numbers less than `n`.
- **Parameters**: 
  - `n` (int): A non-negative integer.
- **Returns**: 
  - A list of integers, each of which is a prime number less than `n`.

### Example Usage

```python
# Example usage of the count_up_to function
print(count_up_to(5))  # Output: [2, 3]
print(count_up_to(11)) # Output: [2, 3, 5, 7]
print(count_up_to(0))  # Output: []
print(count_up_to(20)) # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1))  # Output: []
print(count_up_to(18)) # Output: [2, 3, 5, 7, 11, 13, 17]
```

## Installation

To use this software, you need to have Python installed on your system. The software does not require any additional dependencies, so you can directly run the Python script.

### Steps to Install Python

1. **Download Python**: Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.
2. **Install Python**: Follow the installation instructions provided on the website to install Python on your system.
3. **Verify Installation**: Open a terminal or command prompt and type `python --version` to verify that Python is installed correctly.

## How to Use

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the Directory**: Change your working directory to the location where the `main.py` file is located.
   ```bash
   cd path/to/directory
   ```
3. **Run the Script**: Execute the script using Python to see the output.
   ```bash
   python main.py
   ```

## Additional Information

- **Prime Number Definition**: A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. This software efficiently checks for prime numbers using a helper function `is_prime`.

- **Performance Considerations**: The algorithm used is efficient for small to medium-sized inputs. For very large inputs, consider optimizing the algorithm or using more advanced techniques.

This software is designed to be simple and educational, providing a clear example of how to work with prime numbers in Python.
```