# Fib4 Sequence Calculator

This software provides a function to compute the n-th element of the Fib4 sequence, a sequence similar to the Fibonacci sequence but with a different set of rules. The function is implemented in Python and uses an iterative approach to ensure efficiency.

## Main Functionality

The main functionality of this software is to calculate the n-th element of the Fib4 sequence. The sequence is defined as follows:

- fib4(0) -> 0
- fib4(1) -> 0
- fib4(2) -> 2
- fib4(3) -> 0
- fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

The function `fib4(n: int) -> int` computes the n-th element of this sequence without using recursion, making it efficient for larger values of n.

## Installation

This project does not require any external dependencies, so you can run it with a standard Python environment. Ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

## Usage

To use the Fib4 sequence calculator, follow these steps:

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory where the project files are located.

3. **Run the Code**: You can run the `main.py` file to test the `fib4` function. Use the following command in your terminal:

   ```bash
   python main.py
   ```

4. **Using the Function**: You can modify the `main.py` file to call the `fib4` function with different values of `n` to compute the desired element of the Fib4 sequence. For example:

   ```python
   print(fib4(5))  # Output: 4
   print(fib4(6))  # Output: 8
   print(fib4(7))  # Output: 14
   ```

## Documentation

The function is documented within the code using docstrings. You can view the documentation by opening the `main.py` file. The docstring provides a description of the function, its parameters, and examples of how to use it.

For any further questions or support, please contact our support team. We are here to help you with any issues you may encounter while using the Fib4 sequence calculator.