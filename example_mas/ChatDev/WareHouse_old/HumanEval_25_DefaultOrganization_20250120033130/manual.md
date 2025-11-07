# Factorize

A simple Python application to factorize an integer into its prime factors.

## Introduction

The `factorize` function takes an integer as input and returns a list of its prime factors in ascending order. Each factor is listed as many times as it appears in the factorization of the number. This function is useful for mathematical computations and educational purposes where understanding the prime factorization of numbers is required.

### Main Function

- **factorize(n: int) -> List[int]**: This function returns a list of prime factors of the given integer `n`. The factors are returned in ascending order, and each factor appears as many times as it divides `n`.

#### Example Usage

```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```

## Installation

### Environment Setup

This application does not require any external dependencies, making it easy to set up and run. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: If the code is hosted on a version control system, clone the repository to your local machine.

3. **Navigate to the project directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

4. **Run the script**: You can execute the script using Python by running the following command in your terminal:

   ```bash
   python main.py
   ```

## How to Use

1. **Open your Python environment**: You can use any Python IDE or a simple terminal to run the script.

2. **Import the function**: If you are using this function in another script, make sure to import it.

   ```python
   from main import factorize
   ```

3. **Call the function**: Pass the integer you want to factorize as an argument to the `factorize` function.

   ```python
   result = factorize(56)
   print(result)  # Output: [2, 2, 2, 7]
   ```

4. **View the output**: The function will return a list of prime factors, which you can print or use in further calculations.

## Conclusion

This simple yet powerful function allows you to break down any integer into its prime components, providing a foundational tool for various mathematical and computational applications. With no external dependencies, it is easy to integrate into larger projects or use as a standalone utility.