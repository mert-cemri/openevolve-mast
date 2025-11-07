# Tribonacci Sequence Generator

This software module provides a function to generate the Tribonacci sequence, a lesser-known sequence similar to the Fibonacci sequence. The Tribonacci sequence is defined by specific recurrence relations and is useful for mathematical exploration and educational purposes.

## Main Functionality

The primary function provided by this module is `tri(n)`, which computes the first `n + 1` numbers of the Tribonacci sequence. The sequence is defined as follows:

- `tri(1) = 3`
- For even `n`: `tri(n) = 1 + n / 2`
- For odd `n`: `tri(n) = tri(n - 1) + tri(n - 2) + tri(n - 3)`

### Example

For example, calling `tri(3)` will return the list `[1, 3, 2, 8]`.

## Installation

This project does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/).

## Usage

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

2. **Run the Script**: You can execute the script directly to see the Tribonacci sequence in action. Open a terminal and navigate to the directory containing `main.py`, then run:

   ```bash
   python main.py
   ```

3. **Use the Function in Your Code**: You can import the `tri` function into your own Python scripts to generate Tribonacci sequences as needed. Here's an example of how to use it:

   ```python
   from main import tri

   # Generate the first 4 numbers of the Tribonacci sequence
   sequence = tri(3)
   print(sequence)  # Output: [1, 3, 2, 8]
   ```

## Documentation

The function is documented within the code itself. You can view the docstring by using Python's built-in help function:

```python
help(tri)
```

This will display the function's purpose, arguments, and return value.

## Conclusion

This module provides a simple yet effective way to generate the Tribonacci sequence. It is designed to be easy to use and integrate into other projects. Feel free to explore the sequence and modify the code to suit your needs.