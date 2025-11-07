# Fizz Buzz Digit Counter

This software is designed to solve a specific problem: counting the number of times the digit '7' appears in integers less than a given number `n`, where these integers are divisible by either 11 or 13. This is a simple Python application that can be used for educational purposes or as a utility in larger projects.

## Main Functionality

The core functionality of this software is encapsulated in the `fizz_buzz` function. This function takes an integer `n` as input and returns the count of the digit '7' in numbers less than `n` that are divisible by 11 or 13.

### Function Definition

```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count
```

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/).

## Usage

To use the `fizz_buzz` function, follow these steps:

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can use the Python interpreter to run the function. For example, open a Python shell and import the function:

   ```bash
   python
   ```

   Then, in the Python shell:

   ```python
   from main import fizz_buzz
   result = fizz_buzz(79)
   print(result)  # Output should be 3
   ```

4. **Modify the Input**: You can change the input value `n` to test the function with different numbers.

## Example

Here is an example of how the function works:

```python
>>> fizz_buzz(50)
0
>>> fizz_buzz(78)
2
>>> fizz_buzz(79)
3
```

In the above examples, the function correctly counts the occurrences of the digit '7' in numbers less than `n` that are divisible by 11 or 13.

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The code is straightforward and well-commented to assist in understanding its functionality.