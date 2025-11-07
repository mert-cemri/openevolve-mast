# Fib4 Sequence Calculator

This software module provides a function to compute the n-th element of the Fib4 number sequence, which is a variation of the Fibonacci sequence. The Fib4 sequence is defined as follows:

- fib4(0) -> 0
- fib4(1) -> 0
- fib4(2) -> 2
- fib4(3) -> 0
- fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

## Main Functionality

The main functionality of this software is to compute the n-th element of the Fib4 sequence using an iterative approach, which is efficient and avoids the pitfalls of recursion.

## Installation

This project does not require any external dependencies, so there is no need for a complex installation process. You only need Python installed on your system.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

To use the Fib4 sequence calculator, follow these steps:

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can run the function directly in a Python environment. For example, to compute the 5th element of the Fib4 sequence, you can do the following:

    ```python
    from main import fib4

    result = fib4(5)
    print(result)  # Output will be 4
    ```

4. **Modify as Needed**: You can modify the `n` value in the `fib4(n)` function call to compute different elements of the sequence.

## Examples

Here are some examples of how to use the `fib4` function:

```python
>>> fib4(5)
4
>>> fib4(6)
8
>>> fib4(7)
14
```

These examples demonstrate how to compute specific elements of the Fib4 sequence using the provided function.

## Documentation

For further documentation and detailed explanation of the code, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the function.

## Support

If you encounter any issues or have questions, please feel free to reach out to our support team or open an issue in the repository.

---

This manual provides all the necessary information to understand, install, and use the Fib4 sequence calculator. Enjoy computing the Fib4 sequence efficiently!