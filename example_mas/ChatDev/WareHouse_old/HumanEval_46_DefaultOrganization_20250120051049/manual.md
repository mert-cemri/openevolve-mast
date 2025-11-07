manual.md

```
# Fib4 Sequence Calculator

This software provides a function to compute the n-th element of the Fib4 number sequence, which is a variation of the Fibonacci sequence. The sequence is defined as follows:
- fib4(0) -> 0
- fib4(1) -> 0
- fib4(2) -> 2
- fib4(3) -> 0
- fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

## Main Functions

The main function provided by this software is `fib4(n: int) -> int`, which calculates the n-th element of the Fib4 sequence without using recursion. It uses an iterative approach to efficiently compute the sequence.

### Example Usage

To use the `fib4` function, you can call it with an integer argument representing the position in the sequence you wish to calculate. Here are some examples:

```python
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

## Installation

This project does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

3. Run the `main.py` file using Python to test the function:

```bash
python main.py
```

This will execute the example usage and display the results for `fib4(5)`, `fib4(6)`, and `fib4(7)`.

## Documentation

The `fib4` function is straightforward and does not require additional libraries or complex setup. The code is self-contained within the `main.py` file, and you can modify or extend it as needed for your specific use cases.

For further inquiries or support, please contact our development team at ChatDev.
```
