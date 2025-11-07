'''
This module contains a function to count even and odd digits in an integer.
'''
def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.
    Args:
        num (int): The integer to be analyzed.
    Returns:
        tuple: A tuple containing the count of even digits and odd digits.
    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Convert the number to a string and remove the negative sign if present
    num_str = str(abs(num))
    even_count = 0
    odd_count = 0
    # Iterate over each character in the string
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)