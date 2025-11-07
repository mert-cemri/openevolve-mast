'''
This module contains a function to determine if a bank account balance falls below zero
at any point given a list of deposit and withdrawal operations.
'''
from typing import List
def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.
    Args:
    operations (List[int]): A list of integers representing deposit (positive) and withdrawal (negative) operations.
    Returns:
    bool: True if the balance falls below zero at any point, otherwise False.
    Examples:
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False