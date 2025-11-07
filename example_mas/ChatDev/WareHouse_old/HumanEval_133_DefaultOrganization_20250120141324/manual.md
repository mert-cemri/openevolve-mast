manual.md

```
# Sum Squares Function

This software provides a simple Python function to calculate the sum of squared numbers in a given list. Each number in the list is first rounded up to the nearest integer (using the ceiling function) before being squared and summed.

## Main Functionality

The main function provided by this software is `sum_squares(lst)`. This function takes a list of numbers as input and returns the sum of the squares of these numbers after rounding each number up to the nearest integer.

### Function Definition

```python
def sum_squares(lst):
    """
    You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    return sum(math.ceil(x) ** 2 for x in lst)
```

## Installation

### Environment Setup

This function does not require any external dependencies beyond the standard Python library. Ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

### Requirements

There are no additional packages required for this function. The `math` module used in the function is part of the Python Standard Library.

## Usage

To use the `sum_squares` function, follow these steps:

1. **Create a Python Script:**

   Create a new Python file, e.g., `main.py`, and include the function definition provided above.

2. **Call the Function:**

   You can call the `sum_squares` function by passing a list of numbers as an argument. For example:

   ```python
   result = sum_squares([1.4, 4.2, 0])
   print(result)  # Output: 29
   ```

3. **Run the Script:**

   Execute your Python script using a Python interpreter. Open a terminal or command prompt, navigate to the directory containing your script, and run:

   ```bash
   python main.py
   ```

## Example

Here is an example of how to use the `sum_squares` function:

```python
# Example usage of sum_squares function
numbers = [1.4, 4.2, 0]
result = sum_squares(numbers)
print(f"The sum of squares is: {result}")
```

This will output:

```
The sum of squares is: 29
```

## Conclusion

The `sum_squares` function is a straightforward utility for calculating the sum of squared numbers from a list, with each number rounded up to the nearest integer. It is easy to integrate into any Python project that requires this functionality.
```