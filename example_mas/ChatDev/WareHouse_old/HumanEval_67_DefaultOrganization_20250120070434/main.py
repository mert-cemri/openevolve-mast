'''
This module contains the function `fruit_distribution` which calculates the number of mangoes in a basket given a string describing the number of apples and oranges, and an integer representing the total number of fruits.
'''
def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.
    Parameters:
    s (str): A string containing the number of apples and oranges.
    n (int): The total number of fruits in the basket.
    Returns:
    int: The number of mango fruits in the basket.
    """
    # Split the string to extract numbers
    parts = s.split()
    apples = int(parts[0])  # First number is apples
    oranges = int(parts[3])  # Fourth element is the number of oranges
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    return mangoes