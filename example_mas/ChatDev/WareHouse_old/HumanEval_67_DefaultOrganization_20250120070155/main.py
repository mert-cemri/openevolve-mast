'''
This module contains a function to calculate the number of mango fruits in a basket
given a description of the number of apples and oranges and the total number of fruits.
Function:
    fruit_distribution(s: str, n: int) -> int
'''
def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.
    Parameters:
    s (str): A string representing the number of apples and oranges.
    n (int): An integer representing the total number of fruits in the basket.
    Returns:
    int: The number of mango fruits in the basket.
    """
    # Split the string to extract numbers
    parts = s.split()
    apples = int(parts[0])  # First number in the string
    oranges = int(parts[3])  # Second number in the string
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    return mangoes