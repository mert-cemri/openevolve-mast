'''
Given an integer, return a tuple that has the number of even and odd digits respectively.
Example:
    even_odd_count(-12) ==> (1, 1)
    even_odd_count(123) ==> (1, 2)
'''
def even_odd_count(num):
    # Convert the number to its absolute value
    num = abs(num)
    # Initialize counts
    even_count = 0
    odd_count = 0
    # Convert the number to a string to iterate over each digit
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    # Return the counts as a tuple
    return (even_count, odd_count)