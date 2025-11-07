'''
This module contains the implementation of the do_algebra function, which evaluates an algebraic expression
formed by a list of operators and a list of operands.
'''
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebraic 
    expression and return the evaluation of this expression.
    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 
    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9
    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
    """
    # Start with the first operand
    result = operand[0]
    # Iterate through the operators and operands
    for i, op in enumerate(operator):
        if op == '+':
            result += operand[i + 1]
        elif op == '-':
            result -= operand[i + 1]
        elif op == '*':
            result *= operand[i + 1]
        elif op == '//':
            result //= operand[i + 1]
        elif op == '**':
            result **= operand[i + 1]
        else:
            raise ValueError(f"Unsupported operator: {op}")
    return result
# Example usage:
# operator = ['+', '*', '-']
# operand = [2, 3, 4, 5]
# print(do_algebra(operator, operand))  # Output should be 9