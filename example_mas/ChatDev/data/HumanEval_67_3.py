'''
This module contains a function to calculate the number of mangoes in a basket
given a string describing the number of apples and oranges, and an integer
representing the total number of fruits.
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
    # Split the string to extract numbers
    parts = s.split()
    # Extract the number of apples and oranges
    apples = int(parts[0])
    oranges = int(parts[3])
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    return mangoes