'''
Calculate the number of mangoes in a basket given a string describing the number of apples and oranges,
and an integer representing the total number of fruits.
Parameters:
s (str): A string containing the number of apples and oranges in the format "X apples and Y oranges".
n (int): The total number of fruits in the basket.
Returns:
int: The number of mangoes in the basket.
Examples:
fruit_distribution("5 apples and 6 oranges", 19) -> 8
fruit_distribution("0 apples and 1 oranges", 3) -> 2
fruit_distribution("2 apples and 3 oranges", 100) -> 95
fruit_distribution("100 apples and 1 oranges", 120) -> 19
'''
def fruit_distribution(s, n):
    # Extract the number of apples and oranges from the string
    parts = s.split()
    apples = int(parts[0])
    oranges = int(parts[3])
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    return mangoes