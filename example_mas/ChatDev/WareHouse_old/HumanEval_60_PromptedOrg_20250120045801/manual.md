# Sum to N Function

This software provides a simple function to calculate the sum of all integers from 1 to a given number `n`. The function is implemented in Python and is designed to be efficient and easy to use.

## Main Functionality

The main function provided by this software is `sum_to_n(n: int) -> int`. This function calculates the sum of all integers from 1 to `n` using the formula:

\[ \text{Sum} = \frac{n \times (n + 1)}{2} \]

### Example Usage

```python
>>> sum_to_n(30)
465
>>> sum_to_n(100)
5050
>>> sum_to_n(5)
15
>>> sum_to_n(10)
55
>>> sum_to_n(1)
1
```

## Installation

This software does not require any external dependencies, so you can use it directly with a standard Python installation.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are required since there are no external dependencies.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. You can use the Python interactive shell or create a script to call the `sum_to_n` function.

### Using Python Interactive Shell

- Open the Python interactive shell by typing `python` in your terminal or command prompt.

- Import the function from `main.py`:

  ```python
  from main import sum_to_n
  ```

- Call the function with your desired integer value:

  ```python
  result = sum_to_n(10)
  print(result)  # Output: 55
  ```

### Using a Python Script

- Create a new Python script file, for example, `test_sum.py`.

- Write the following code in `test_sum.py`:

  ```python
  from main import sum_to_n

  result = sum_to_n(10)
  print(result)  # Output: 55
  ```

- Run the script using the command:

  ```bash
  python test_sum.py
  ```

## Documentation

For further details, you can refer to the docstring provided in the `main.py` file, which includes example usages and the mathematical formula used for the calculation.

This software is designed to be straightforward and efficient, making it suitable for educational purposes or simple applications where calculating the sum of integers is required.