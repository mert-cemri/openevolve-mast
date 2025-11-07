manual.md

```
# Fib4 Sequence Calculator

This software provides a function to compute the n-th element of the Fib4 sequence, a sequence similar to the Fibonacci sequence. The Fib4 sequence is defined as follows:

- fib4(0) -> 0
- fib4(1) -> 0
- fib4(2) -> 2
- fib4(3) -> 0
- fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

## Main Functionality

The main functionality of this software is to compute the n-th element of the Fib4 sequence using an iterative approach, which avoids the inefficiencies of recursion.

## Installation

### Environment Setup

This project does not require any external dependencies, so setting up the environment is straightforward. You only need Python installed on your system.

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: If you have the code in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

## Usage

To use the Fib4 sequence calculator, you can run the `main.py` file. This file contains the `fib4` function, which you can use to compute the desired element of the sequence.

### Running the Code

1. **Open a terminal** and navigate to the directory where `main.py` is located.

2. **Run the script** using Python:
   ```bash
   python main.py
   ```

3. **Testing with Doctest**: The script includes doctests that verify the correctness of the `fib4` function. When you run the script, these tests will automatically execute to ensure everything is working as expected.

### Example Usage

You can use the `fib4` function directly in your Python code. Here’s an example:

```python
from main import fib4

# Compute the 5th element of the Fib4 sequence
result = fib4(5)
print(result)  # Output: 4

# Compute the 6th element of the Fib4 sequence
result = fib4(6)
print(result)  # Output: 8
```

## Documentation

For further details on the implementation and usage of the `fib4` function, please refer to the comments and docstrings within the `main.py` file. The code is well-documented to help you understand the logic and flow of the sequence calculation.

```