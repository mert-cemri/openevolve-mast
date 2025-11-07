'''
This script contains a function to calculate the number of mangoes in a basket
given a string that specifies the number of apples and oranges, and an integer
that represents the total number of fruits in the basket.
'''
def fruit_distribution(s, n):
    """
    Calculate the number of mangoes in the basket.
    Parameters:
    s (str): A string containing the number of apples and oranges.
    n (int): The total number of fruits in the basket.
    Returns:
    int: The number of mangoes in the basket.
    """
    # Split the string to extract numbers
    parts = s.split()
    apples = int(parts[0])  # First number is apples
    oranges = int(parts[3])  # Fourth part is the number of oranges
    # Calculate mangoes
    mangoes = n - apples - oranges
    return mangoes
# Example usage
if __name__ == "__main__":
    print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
    print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
    print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
    print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19