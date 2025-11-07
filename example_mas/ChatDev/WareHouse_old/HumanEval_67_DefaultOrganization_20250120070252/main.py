'''
This module contains a function to calculate the number of mangoes in a fruit basket
given the number of apples and oranges described in a string and the total number of fruits.
'''
def fruit_distribution(s, n):
    """
    Calculate the number of mangoes in the basket.
    Parameters:
    s (str): A string that contains the number of apples and oranges.
    n (int): The total number of fruits in the basket.
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