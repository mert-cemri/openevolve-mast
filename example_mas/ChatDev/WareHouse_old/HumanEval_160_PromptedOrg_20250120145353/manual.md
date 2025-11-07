# Algebraic Expression Evaluator

This software module provides a function to evaluate algebraic expressions constructed from a list of operators and a list of operands. It supports basic algebraic operations such as addition, subtraction, multiplication, floor division, and exponentiation.

## Main Functionality

The main function provided by this module is `do_algebra`, which takes two lists as input:

- `operator`: A list of algebraic operators (`+`, `-`, `*`, `//`, `**`).
- `operand`: A list of non-negative integers.

The function constructs an algebraic expression using these lists and evaluates the result.

### Example

Given:
- `operator = ['+', '*', '-']`
- `operand = [2, 3, 4, 5]`

The function evaluates the expression `2 + 3 * 4 - 5`, resulting in `9`.

## Installation

This project does not require any external dependencies. You can directly use the provided Python code in your environment.

## How to Use

1. **Clone the Repository:**

   Clone the repository to your local machine to access the `main.py` file.

2. **Run the Code:**

   You can run the code by importing the `do_algebra` function from the `main.py` file in your Python script or interactive session.

   ```python
   from main import do_algebra

   operator = ['+', '*', '-']
   operand = [2, 3, 4, 5]
   result = do_algebra(operator, operand)
   print(result)  # Output: 9
   ```

3. **Modify Inputs:**

   You can modify the `operator` and `operand` lists to evaluate different expressions. Ensure that the length of the `operator` list is one less than the length of the `operand` list.

## Error Handling

The function raises a `ValueError` if an unsupported operator is encountered. Ensure that only the supported operators (`+`, `-`, `*`, `//`, `**`) are used in the `operator` list.

## Documentation

For further details on how to use the function, refer to the docstring provided in the `main.py` file. This includes information on the expected input format and examples of usage.

Feel free to reach out if you have any questions or need further assistance with using this module.