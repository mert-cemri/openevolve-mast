# Algebra Expression Evaluator

This software provides a function to evaluate algebraic expressions formed by a list of operators and a list of operands. It is designed to handle basic algebra operations such as addition, subtraction, multiplication, floor division, and exponentiation.

## Main Functionality

The main function provided by this software is `do_algebra`, which takes two lists as input: `operator` and `operand`. The function evaluates the algebraic expression formed by these lists and returns the result.

### Supported Operations

- **Addition (`+`)**: Adds two numbers.
- **Subtraction (`-`)**: Subtracts the second number from the first.
- **Multiplication (`*`)**: Multiplies two numbers.
- **Floor Division (`//`)**: Divides the first number by the second and returns the largest integer not greater than the division result.
- **Exponentiation (`**`)**: Raises the first number to the power of the second.

### Example

Given:
- `operator = ['+', '*', '-']`
- `operand = [2, 3, 4, 5]`

The expression evaluated is: `2 + 3 * 4 - 5`, which results in `9`.

## Installation

This software does not require any external dependencies, making it straightforward to use. You only need Python installed on your system.

### Quick Install

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

2. **Run the Function**: You can use the `do_algebra` function by importing it into your Python script or by running it directly in a Python environment.

   ```python
   from main import do_algebra

   operator = ['+', '*', '-']
   operand = [2, 3, 4, 5]
   result = do_algebra(operator, operand)
   print(result)  # Output will be 9
   ```

3. **Modify Inputs**: You can change the `operator` and `operand` lists to evaluate different expressions. Ensure the length of the `operator` list is one less than the `operand` list.

## Error Handling

The function raises a `ValueError` if an unsupported operator is provided. Ensure that only the supported operators (`+`, `-`, `*`, `//`, `**`) are used in the `operator` list.

## Documentation

For further details, refer to the comments within the `main.py` file, which provide a comprehensive explanation of the function's logic and usage.

This manual serves as a guide to effectively utilize the algebra expression evaluator in your projects. Feel free to explore and modify the code to suit your specific needs.