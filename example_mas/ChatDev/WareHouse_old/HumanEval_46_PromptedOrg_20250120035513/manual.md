# Fib4 Sequence Calculator

This software provides a function to compute the n-th element of the Fib4 number sequence, which is a variation of the Fibonacci sequence. The sequence is defined as follows:

- fib4(0) -> 0
- fib4(1) -> 0
- fib4(2) -> 2
- fib4(3) -> 0
- fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

The function is implemented to compute the sequence efficiently without using recursion.

## Quick Install

There are no external dependencies required for this software. You only need Python installed on your system.

## How to Use

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Change to the directory where the `main.py` file is located:

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function:**

   You can use the `fib4` function by importing it into your Python script or by running it directly in the Python interpreter. Here is an example of how to use the function:

   ```python
   from main import fib4

   # Example usage
   print(fib4(5))  # Output: 4
   print(fib4(6))  # Output: 8
   print(fib4(7))  # Output: 14
   ```

4. **Modify and Extend:**

   Feel free to modify the code to suit your needs or extend its functionality. The current implementation is designed to be simple and efficient for calculating the Fib4 sequence.

## Documentation

The function is documented with a docstring explaining its purpose and usage. You can view the docstring by using the `help` function in Python:

```python
help(fib4)
```

This will display the function's documentation, including its parameters and return value.

## Support

For any issues or questions, please contact the development team through the repository's issue tracker or by reaching out to the support email provided in the repository.

---

This manual provides all the necessary information to get started with the Fib4 Sequence Calculator. Enjoy exploring the sequence and integrating it into your projects!