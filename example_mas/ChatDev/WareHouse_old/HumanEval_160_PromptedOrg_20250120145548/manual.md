# Algebra Expression Evaluator

This software provides a function `do_algebra` that evaluates an algebraic expression constructed from a list of operators and a list of operands. It supports basic algebra operations such as addition, subtraction, multiplication, floor division, and exponentiation.

## Main Function

### `do_algebra(operator, operand)`

- **Description**: Evaluates an algebraic expression based on the provided operators and operands.
- **Parameters**:
  - `operator`: A list of strings representing basic algebra operations. Supported operations are:
    - Addition (`+`)
    - Subtraction (`-`)
    - Multiplication (`*`)
    - Floor division (`//`)
    - Exponentiation (`**`)
  - `operand`: A list of non-negative integers. The length of this list is one more than the length of the operator list.
- **Returns**: The result of the evaluated expression as an integer.
- **Example**:
  ```python
  operator = ['+', '*', '-']
  operand = [2, 3, 4, 5]
  result = do_algebra(operator, operand)
  # result will be 9, as the expression evaluates to 2 + 3 * 4 - 5
  ```

## Installation

There are no external dependencies required for this software. You can directly use the provided `main.py` file in your Python environment.

## Usage

1. **Clone the Repository**: Download or clone the repository to your local machine.
2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing `main.py`.
3. **Run the Function**: You can use the `do_algebra` function in your Python scripts by importing it from `main.py`.

### Example Usage

```python
from main import do_algebra

operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)
print(f"The result of the expression is: {result}")
```

## Notes

- Ensure that the operator list has at least one operator and the operand list has at least two operands.
- The length of the operator list should be equal to the length of the operand list minus one.
- The software handles basic algebra operations and raises a `ValueError` if an unsupported operator is encountered.

This manual provides all the necessary information to effectively use the algebra expression evaluator. If you encounter any issues or have further questions, please refer to the documentation or contact support.