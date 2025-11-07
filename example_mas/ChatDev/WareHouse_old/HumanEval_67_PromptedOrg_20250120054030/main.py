'''
This module contains the implementation of the fruit_distribution function
which calculates the number of mango fruits in a basket given a string
describing the number of apples and oranges, and an integer representing
the total number of fruits in the basket.
'''
import re
def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.
    Parameters:
    s (str): A string that represents the number of apples and oranges.
    n (int): An integer that represents the total number of fruits in the basket.
    Returns:
    int: The number of mango fruits in the basket.
    """
    # Extract numbers from the string
    numbers = list(map(int, re.findall(r'\d+', s)))
    # Calculate the number of mangoes
    mangoes = n - sum(numbers)
    return mangoes