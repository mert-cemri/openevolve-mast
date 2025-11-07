'''
This module contains the function `rounded_avg` which calculates the average of integers
from n to m, rounds it to the nearest integer, and converts it to a binary string.
If n is greater than m, it returns -1.
'''
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n > m:
        return -1
    # Calculate the sum of integers from n to m
    total_sum = sum(range(n, m + 1))
    # Calculate the count of integers from n to m
    count = m - n + 1
    # Calculate the average and round it to the nearest integer
    average = round(total_sum / count)
    # Convert the rounded average to binary
    binary_average = bin(average)
    return binary_average