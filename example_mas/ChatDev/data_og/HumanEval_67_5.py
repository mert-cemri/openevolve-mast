'''
This module contains the function `fruit_distribution` which calculates the number of mangoes in a basket given a string that specifies the number of apples and oranges, and an integer that represents the total number of fruits in the basket.
'''
def fruit_distribution(s, n):
    """
    Calculate the number of mangoes in the basket.
    Parameters:
    s (str): A string containing the number of apples and oranges.
    n (int): An integer representing the total number of fruits in the basket.
    Returns:
    int: The number of mangoes in the basket.
    """
    # Extract numbers from the string
    parts = s.split()
    apples = int(parts[0])
    oranges = int(parts[3])
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    return mangoes