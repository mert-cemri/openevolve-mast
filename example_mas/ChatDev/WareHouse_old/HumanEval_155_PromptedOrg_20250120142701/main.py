'''
Given an integer, return a tuple that has the number of even and odd digits respectively.
Example:
    even_odd_count(-12) ==> (1, 1)
    even_odd_count(123) ==> (1, 2)
'''
def even_odd_count(num):
    # Convert the number to its absolute value and then to a string
    num_str = str(abs(num))
    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0
    # Iterate over each character in the string representation of the number
    for char in num_str:
        digit = int(char)  # Convert character back to integer
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    # Return the counts as a tuple
    return (even_count, odd_count)