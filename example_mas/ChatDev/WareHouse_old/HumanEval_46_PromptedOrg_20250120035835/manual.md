# Fib4 Sequence Calculator

This software provides a function to compute the n-th element of the Fib4 number sequence, a sequence similar to the Fibonacci sequence but with a different set of rules. The software is implemented in Python and is designed to be efficient by avoiding recursion.

## Main Functions

The main function of this software is:

- **fib4(n: int) -> int**: Computes the n-th element of the Fib4 number sequence. The sequence is defined as follows:
  - fib4(0) -> 0
  - fib4(1) -> 0
  - fib4(2) -> 2
  - fib4(3) -> 0
  - fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

## Installation

This software does not require any external dependencies. You only need Python installed on your system to run the code.

### Steps to Install Python

1. **Download Python**: Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.

2. **Install Python**: Follow the instructions provided on the website to install Python on your system. Make sure to check the option to add Python to your system's PATH during installation.

3. **Verify Installation**: Open a terminal or command prompt and type `python --version` to verify that Python is installed correctly.

## How to Use

1. **Clone the Repository**: If the code is hosted on a version control system, clone the repository to your local machine. Otherwise, download the `main.py` file.

2. **Run the Code**: Open a terminal or command prompt, navigate to the directory containing `main.py`, and run the following command:

   ```bash
   python main.py
   ```

   This will execute the example usage of the `fib4` function, printing the results for `fib4(5)`, `fib4(6)`, and `fib4(7)`.

3. **Modify for Custom Input**: To compute the Fib4 sequence for a different value of `n`, open `main.py` in a text editor, modify the `print` statements at the bottom of the file with your desired input, and save the file. Then, rerun the code using the command above.

## Example Usage

The following example demonstrates how to use the `fib4` function:

```python
# Example usage
if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
```

This example calculates and prints the 5th, 6th, and 7th elements of the Fib4 sequence.

## Documentation

For further details on the implementation and usage of the `fib4` function, please refer to the comments within the `main.py` file. The code is self-contained and does not require additional libraries or frameworks.