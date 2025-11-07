manual.md

```
# Even Odd Digit Counter

A simple Python application to count the number of even and odd digits in an integer.

## Overview

This application provides a function `even_odd_count` that takes an integer as input and returns a tuple containing the count of even and odd digits in the integer. It handles both positive and negative integers.

### Main Function

- **even_odd_count(num):**
  - **Input:** An integer `num`.
  - **Output:** A tuple `(even_count, odd_count)` where `even_count` is the number of even digits and `odd_count` is the number of odd digits in the integer.
  - **Example Usage:**
    - `even_odd_count(-12)` returns `(1, 1)`
    - `even_odd_count(123)` returns `(1, 2)`

## Installation

This application does not have any external dependencies, so you don't need to install any additional packages. It runs on any standard Python environment.

### Quick Start

1. **Ensure you have Python installed.** You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository or download the `main.py` file.**

3. **Run the application:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing `main.py`.
   - Run the Python script using the command:
     ```
     python main.py
     ```

## Usage

To use the `even_odd_count` function, you can either import it into another Python script or run it directly from the command line.

### Example

```python
from main import even_odd_count

# Example usage
result = even_odd_count(12345)
print(f"Even digits: {result[0]}, Odd digits: {result[1]}")
```

### Command Line

You can also test the function directly in the Python interactive shell:

```bash
$ python
>>> from main import even_odd_count
>>> even_odd_count(6789)
(2, 2)
```

## Documentation

For more information or to report issues, please contact our support team or visit our GitHub repository.

```