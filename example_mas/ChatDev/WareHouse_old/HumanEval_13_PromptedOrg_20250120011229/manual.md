# Greatest Common Divisor (GCD) Calculator

This software module provides a simple function to calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm. The GCD is the largest positive integer that divides each of the integers without leaving a remainder.

## Main Function

The main function provided in this module is:

- `greatest_common_divisor(a: int, b: int) -> int`: This function takes two integers `a` and `b` as input and returns their greatest common divisor.

### Example Usage

```python
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
```

## Installation

To use this software, you need to have Python installed on your system. If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to where the `main.py` file is located:
   ```bash
   cd <directory-name>
   ```

3. **Run the Code**: You can execute the `main.py` file directly if you want to test the function:
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: In your Python script, import the `greatest_common_divisor` function from the module where it is defined.

   ```python
   from main import greatest_common_divisor
   ```

2. **Call the Function**: Use the function by passing two integers as arguments.

   ```python
   result = greatest_common_divisor(48, 18)
   print(f"The GCD is: {result}")
   ```

3. **Output**: The function will return the greatest common divisor of the two integers provided.

## Documentation

For further documentation and examples, please refer to the docstring provided within the code. The docstring includes example usages and expected outputs.

## Support

If you encounter any issues or have questions, please contact our support team or refer to the documentation provided within the code.