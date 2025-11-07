'''
This module contains the implementation of the fruit_distribution function
which calculates the number of mangoes in a basket given the number of apples
and oranges and the total number of fruits.
'''
import re
def fruit_distribution(s, n):
    """
    Calculate the number of mangoes in the basket.
    Parameters:
    s (str): A string containing the number of apples and oranges.
    n (int): The total number of fruits in the basket.
    Returns:
    int: The number of mangoes in the basket.
    """
    # Use regular expression to find all numbers in the string
    numbers = re.findall(r'\d+', s)
    # Convert the extracted numbers to integers
    apples = int(numbers[0])
    oranges = int(numbers[1])
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    return mangoes