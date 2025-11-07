```markdown
# Greatest Common Divisor (GCD) Calculator

This software module provides a simple and efficient way to compute the greatest common divisor (GCD) of two integers using the Euclidean algorithm. The GCD is the largest positive integer that divides each of the integers without leaving a remainder.

## Main Function

The main function provided by this module is:

- `greatest_common_divisor(a: int, b: int) -> int`: This function takes two integers `a` and `b` as input and returns their greatest common divisor.

### Example Usage

```python
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
```

## Installation

This project does not require any external dependencies, so you can use it directly without installing additional packages. However, you need to have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

## How to Use

1. **Open a terminal or command prompt**.

2. **Navigate to the directory** where `main.py` is located.

3. **Run Python interactive shell** or create a Python script to use the function:

   - **Interactive Shell**:
     ```bash
     python
     ```

     Then, within the Python shell, you can import and use the function:
     ```python
     from main import greatest_common_divisor
     print(greatest_common_divisor(3, 5))
     print(greatest_common_divisor(25, 15))
     ```

   - **Python Script**:
     Create a new Python file, say `test_gcd.py`, and add the following code:
     ```python
     from main import greatest_common_divisor

     print(greatest_common_divisor(3, 5))
     print(greatest_common_divisor(25, 15))
     ```

     Run the script using:
     ```bash
     python test_gcd.py
     ```

## Documentation

This module is designed to be simple and straightforward, with a single function that performs the GCD calculation. For more information on the Euclidean algorithm, you can refer to [Euclidean algorithm on Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm).

Feel free to modify and extend the code as needed for your specific use cases.
```
