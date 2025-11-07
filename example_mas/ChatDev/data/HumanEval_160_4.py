'''
This function takes a list of operators and a list of operands, constructs an algebraic expression, and evaluates it.
Parameters:
- operator (list): A list of strings representing basic algebra operations.
- operand (list): A list of non-negative integers.
Returns:
- int: The result of the evaluated algebraic expression.
Example:
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)
# result should be 9
'''
def do_algebra(operator, operand):
    # Start with the first operand
    result = operand[0]
    # Iterate over the operators and remaining operands
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
# Example usage
# operator = ['+', '*', '-']
# operand = [2, 3, 4, 5]
# print(do_algebra(operator, operand))  # Output: 9