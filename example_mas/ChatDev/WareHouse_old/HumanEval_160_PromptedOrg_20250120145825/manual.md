# Algebra Expression Evaluator

This software provides a function to evaluate algebraic expressions constructed from a list of operators and operands. It is designed to handle basic algebra operations such as addition, subtraction, multiplication, floor division, and exponentiation.

## Main Functionality

The main function of this software is `do_algebra(operator, operand)`, which takes two lists as input:

- `operator`: A list of strings representing basic algebra operations. Supported operations include:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Floor division (`//`)
  - Exponentiation (`**`)

- `operand`: A list of non-negative integers that serve as the operands for the algebraic expression.

The function constructs an algebraic expression using the provided operators and operands and returns the evaluated result.

### Example

```python
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)
# result should be 9
```

## Installation

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/).

## How to Use

1. **Clone the Repository**: Download the code to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Code**: You can run the code using a Python interpreter. For example, in the terminal, you can execute:

   ```bash
   python main.py
   ```

4. **Modify the Example**: You can modify the example usage in the `main.py` file to test different operators and operands.

## Documentation

The code is straightforward and documented with comments explaining each part of the function. If you need further assistance, please refer to the comments within the `main.py` file for guidance on how the function processes the input lists to evaluate the expression.

Feel free to reach out for support if you encounter any issues or have questions about using the software.