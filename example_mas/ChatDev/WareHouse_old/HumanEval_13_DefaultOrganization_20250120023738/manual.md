manual.md

```
# Greatest Common Divisor Calculator

This software provides a simple function to calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm. It is implemented in Python and is designed to be easy to use and integrate into other projects.

## Main Function

The main function provided by this software is `greatest_common_divisor(a: int, b: int) -> int`. This function takes two integer inputs and returns their greatest common divisor.

### Function Signature

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
```

### How It Works

The function uses the Euclidean algorithm, which is an efficient method for computing the greatest common divisor of two numbers. The algorithm is based on the principle that the GCD of two numbers also divides their difference. The process is repeated until the remainder is zero, at which point the divisor is the GCD.

## Installation

### Environment Dependencies

This software does not require any external dependencies beyond Python itself. It is compatible with Python 3.x.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone or download the repository containing the `main.py` file.

3. No additional installation steps are required since there are no external dependencies.

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory containing the `main.py` file.

3. You can use the function by importing it into your Python script or by running the script directly in a Python environment.

### Example Usage

```python
from main import greatest_common_divisor

# Example usage
result1 = greatest_common_divisor(3, 5)
print(f"The GCD of 3 and 5 is: {result1}")

result2 = greatest_common_divisor(25, 15)
print(f"The GCD of 25 and 15 is: {result2}")
```

This will output:

```
The GCD of 3 and 5 is: 1
The GCD of 25 and 15 is: 5
```

## Documentation

For further information on the Euclidean algorithm and its applications, you can refer to [Wikipedia's article on the Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm).

This manual provides all necessary information to understand, install, and use the GCD calculator function effectively. If you have any questions or need further assistance, please feel free to contact our support team.
```