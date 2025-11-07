# Tribonacci Sequence Generator

This software module provides a simple implementation of a Tribonacci sequence generator. The Tribonacci sequence is a variation of the Fibonacci sequence, where each term is the sum of the three preceding ones, starting from a base case.

## Main Functions

The main function provided by this module is:

- `tri(n)`: Generates the first `n + 1` numbers of the Tribonacci sequence. The sequence is defined by the following rules:
  - `tri(1) = 3`
  - `tri(n) = 1 + n / 2`, if `n` is even.
  - `tri(n) = tri(n - 1) + tri(n - 2) + tri(n - 3)`, if `n` is odd.

### Example Usage

To generate the first `n + 1` numbers of the Tribonacci sequence, you can use the `tri` function as follows:

```python
# Example usage
print(tri(3))  # Output should be [1, 3, 2, 8]
```

## Installation

This project does not require any external dependencies, so you can run it directly with Python. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change into the directory where the project is located.

   ```bash
   cd <project-directory>
   ```

3. **Run the Code**: You can run the `main.py` file directly to see the Tribonacci sequence generator in action.

   ```bash
   python main.py
   ```

## How to Use

1. **Open the `main.py` file**: This file contains the implementation of the Tribonacci sequence generator.

2. **Modify the `tri(n)` Function Call**: Change the argument `n` in the `tri(n)` function call to generate the desired number of terms in the sequence.

3. **Run the Script**: Execute the script to see the output of the Tribonacci sequence.

## Documentation

For further information and detailed documentation, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the Tribonacci sequence generation.

Feel free to reach out if you have any questions or need further assistance with using this software.