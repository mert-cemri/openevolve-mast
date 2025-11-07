# Largest Divisor Finder

This software provides a simple utility to find the largest divisor of a given integer `n` that is smaller than `n` itself. This can be useful in various mathematical computations and applications where divisors are needed.

## Main Functionality

The main function provided by this software is:

- `largest_divisor(n: int) -> int`: This function takes an integer `n` as input and returns the largest integer that divides `n` evenly and is smaller than `n`.

### Example Usage

```python
>>> largest_divisor(15)
5
```

In this example, the largest divisor of 15 that is smaller than 15 is 5.

## Installation

This project does not require any external Python packages, so you can run it in any standard Python environment without additional installations.

### Quick Start

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd <project-directory>
   ```

3. **Run the Script**

   You can run the script directly using Python:

   ```bash
   python main.py
   ```

   This will execute the script and run any embedded tests.

## How to Use

To use the `largest_divisor` function in your own projects:

1. **Import the Function**

   You can import the function from the `main.py` file:

   ```python
   from main import largest_divisor
   ```

2. **Call the Function**

   Pass an integer to the function to get the largest divisor:

   ```python
   result = largest_divisor(28)
   print(result)  # Output will be 14
   ```

## Testing

The script includes a simple test using Python's `doctest` module. To run the test, execute the script as shown in the Quick Start section. The test will verify that the function works as expected.

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The function is documented with a docstring that includes a usage example.

This software is designed to be simple and efficient, making it easy to integrate into larger projects or use as a standalone utility.