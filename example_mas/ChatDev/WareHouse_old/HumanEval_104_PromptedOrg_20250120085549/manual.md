# Unique Digits Software

This software provides a function to filter and sort a list of positive integers, returning only those numbers that do not contain any even digits. The function is useful for applications where you need to process numbers based on their digit composition.

## Main Functionality

The main function provided by this software is `unique_digits(x)`, which takes a list of positive integers and returns a sorted list of numbers that do not contain any even digits.

### Example Usage

```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```

## Installation

To use this software, you need to have Python installed on your system. The software does not require any additional dependencies, so you can directly use the function in your Python environment.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `unique_digits` function.

3. **Run the function**: You can use the function in your Python scripts or interactive sessions.

## How to Use

1. **Import the function**: If you have the `main.py` file in your project, you can import the function using:

    ```python
    from main import unique_digits
    ```

2. **Call the function**: Pass a list of positive integers to the function to get the filtered and sorted list.

    ```python
    result = unique_digits([15, 33, 1422, 1])
    print(result)  # Output: [1, 15, 33]
    ```

## Documentation

The function `unique_digits(x)` works by iterating through each number in the list `x`, checking if the number contains any even digits. If a number does not contain any even digits, it is included in the result list. The result list is then sorted in increasing order before being returned.

### Function Definition

```python
def unique_digits(x):
    def has_even_digit(n):
        """Check if the number contains any even digit."""
        while n > 0:
            digit = n % 10
            if digit % 2 == 0:
                return True
            n //= 10
        return False
    # Filter numbers that do not have any even digits
    result = [num for num in x if not has_even_digit(num)]
    # Return the sorted result
    return sorted(result)
```

This function is designed to be efficient and easy to integrate into larger projects where filtering numbers based on digit composition is required.