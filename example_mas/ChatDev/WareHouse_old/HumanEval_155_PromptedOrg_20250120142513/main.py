'''
Given an integer, return a tuple that has the number of even and odd digits respectively.
Example:
    even_odd_count(-12) ==> (1, 1)
    even_odd_count(123) ==> (1, 2)
'''
def even_odd_count(num):
    # Convert the number to its absolute value
    num = abs(num)
    # Convert the number to a string to iterate over each digit
    num_str = str(num)
    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0
    # Iterate over each character in the string representation of the number
    for digit in num_str:
        # Convert character back to integer
        digit = int(digit)
        # Check if the digit is even or odd
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    # Return the tuple with the counts of even and odd digits
    return (even_count, odd_count)