# Sum to N Function

This software provides a simple Python function to calculate the sum of all integers from 1 to a given number `n`. The function is efficient and leverages the mathematical formula for the sum of an arithmetic series.

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

## Quick Install

This software does not require any external dependencies. You only need Python installed on your system to use this function.

### Installation Steps

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `sum_to_n` function.

3. **Run the function**: You can use the function directly in your Python environment or include it in your Python scripts.

## How to Use

1. **Open your Python environment**: This could be a Python shell, a script file, or an integrated development environment (IDE) like PyCharm or VSCode.

2. **Import or define the function**: If you have the `main.py` file, you can import the function or copy the function definition into your script.

3. **Call the function**: Use the function by passing an integer `n` to it, and it will return the sum of all integers from 1 to `n`.

### Example

```python
# Assuming the function is defined in your script or imported
result = sum_to_n(10)
print(f"The sum of numbers from 1 to 10 is: {result}")
```

This will output:

```
The sum of numbers from 1 to 10 is: 55
```

## Documentation

For further details or questions, please refer to the comments within the `main.py` file, which provide additional context and examples for using the `sum_to_n` function.