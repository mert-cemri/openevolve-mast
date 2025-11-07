# Odd Collatz Sequence Finder

This software provides a function to compute the odd numbers in the Collatz sequence for a given positive integer. The Collatz conjecture is a mathematical sequence that starts with any positive integer `n`. Each subsequent term is derived from the previous term: if the previous term is even, the next term is half of the previous term; if the previous term is odd, the next term is three times the previous term plus one. The sequence is conjectured to always reach 1, regardless of the starting integer.

## Main Function

### `get_odd_collatz(n)`

- **Description**: This function takes a positive integer `n` and returns a sorted list of the odd numbers in the Collatz sequence starting from `n`.
- **Parameters**: 
  - `n` (int): A positive integer to start the Collatz sequence.
- **Returns**: 
  - A list of odd integers in the Collatz sequence, sorted in increasing order.

### Example

```python
result = get_odd_collatz(5)
print(result)  # Output: [1, 5]
```

## Installation

This project does not require any external dependencies. It is implemented purely in Python, so you only need a Python environment to run it.

### Quick Install

1. **Ensure Python is installed**: You need Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: If you have access to the repository, clone it to your local machine.

3. **Navigate to the project directory**: Open your terminal or command prompt and navigate to the directory where the project is located.

4. **Run the script**: You can directly run the `main.py` script using Python.

```bash
python main.py
```

## Usage

1. **Import the function**: If you are using this function in another script, import it from `main.py`.

```python
from main import get_odd_collatz
```

2. **Call the function**: Pass a positive integer to the function to get the sorted list of odd numbers in its Collatz sequence.

```python
odd_numbers = get_odd_collatz(7)
print(odd_numbers)  # Example output: [1, 7]
```

## Documentation

For further information on the Collatz conjecture and its mathematical implications, you may refer to various mathematical resources and documentation available online. This software provides a simple implementation to explore the odd numbers in the sequence for any given starting integer.