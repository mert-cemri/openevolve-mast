# FibFib Sequence Calculator

This software provides a function to compute the n-th element of the FibFib number sequence, a sequence similar to the Fibonacci sequence but with a unique definition.

## Main Function

The main function provided by this software is `fibfib(n: int)`, which calculates the n-th element of the FibFib sequence. The sequence is defined as follows:

- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- For `n >= 3`, `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`

### Example Usage

```python
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
```

## Installation

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

Clone the repository or download the `main.py` file to your local machine.

## How to Use

1. **Run the Script:**

   You can run the script directly using Python. Open a terminal or command prompt, navigate to the directory containing `main.py`, and execute the following command:

   ```bash
   python main.py
   ```

2. **Import the Function:**

   If you want to use the `fibfib` function in another script, you can import it:

   ```python
   from main import fibfib

   # Now you can use the function
   result = fibfib(5)
   print(result)  # Output will be 4
   ```

3. **Testing:**

   The script includes a `doctest` module to verify the function's correctness. When you run `main.py`, it will automatically execute the tests defined in the docstring.

## Documentation

The function is documented within the code itself. You can refer to the docstring for a detailed explanation of the function's behavior and example usage.

For any further questions or support, please contact our support team or visit our website for more information.