# Fib4 Sequence Calculator

This software provides a function to compute the n-th element of the Fib4 number sequence, which is a variation of the Fibonacci sequence. The Fib4 sequence is defined as follows:

- fib4(0) -> 0
- fib4(1) -> 0
- fib4(2) -> 2
- fib4(3) -> 0
- fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

## Main Functionality

The main function provided by this software is `fib4(n: int) -> int`, which computes the n-th element of the Fib4 sequence without using recursion. It uses an iterative approach to efficiently calculate the sequence values.

## Installation

### Environment Setup

This software does not require any external dependencies, making it straightforward to set up. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine. Otherwise, download the `main.py` file.

3. **Navigate to the Directory**: Open a terminal and navigate to the directory where `main.py` is located.

## Usage

To use the Fib4 sequence calculator, follow these steps:

1. **Open Terminal**: Open your terminal or command prompt.

2. **Run Python**: Execute the Python script by running the following command:

   ```bash
   python main.py
   ```

3. **Call the Function**: You can call the `fib4` function directly in the Python environment to compute the desired element of the Fib4 sequence. For example:

   ```python
   >>> fib4(5)
   4
   >>> fib4(6)
   8
   >>> fib4(7)
   14
   ```

These commands will return the 5th, 6th, and 7th elements of the Fib4 sequence, respectively.

## Documentation

For further details on the implementation and usage, you can refer to the comments within the `main.py` file. The function is designed to be simple and efficient, making it easy to integrate into other projects or use as a standalone tool for sequence calculations.

If you encounter any issues or have questions, please feel free to reach out for support.