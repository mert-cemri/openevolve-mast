manual.md

```
# FibFib Sequence Calculator

This software provides a function to compute the n-th element of the FibFib number sequence, a sequence similar to the Fibonacci sequence. The FibFib sequence is defined as follows:
- fibfib(0) == 0
- fibfib(1) == 0
- fibfib(2) == 1
- fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n > 2

## Main Functionality

The main functionality of this software is to compute the n-th element of the FibFib sequence efficiently using an iterative approach.

## Quick Install

This software does not require any external dependencies, so you can run it directly with Python. Ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository:**
   - Clone the repository to your local machine using the following command:
     ```
     git clone <repository-url>
     ```

2. **Navigate to the Directory:**
   - Change into the directory where the `main.py` file is located:
     ```
     cd <repository-directory>
     ```

3. **Run the Software:**
   - Execute the `main.py` file using Python to compute the FibFib sequence for specific values:
     ```
     python main.py
     ```

   - You can modify the `main.py` file to compute the FibFib sequence for different values of `n` by changing the arguments in the `print(fibfib(n))` statements.

## Example Usage

The `main.py` file includes example usage of the `fibfib` function:
```python
if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
```

These examples demonstrate how to compute the FibFib sequence for `n = 1`, `n = 5`, and `n = 8`.

## Documentation

For further understanding of the code and its logic, please refer to the comments within the `main.py` file. The code is straightforward and well-documented to help you understand the iterative approach used to compute the FibFib sequence.

```