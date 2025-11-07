'''
Given two positive integers a and b, return the even digits between a
and b, in ascending order.
For example:
generate_integers(2, 8) => [2, 4, 6, 8]
generate_integers(8, 2) => [2, 4, 6, 8]
generate_integers(10, 14) => []
'''
def generate_integers(a, b):
    # Ensure a is the smaller number and b is the larger number
    start, end = min(a, b), max(a, b)
    # Generate even numbers between start and end inclusive
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    return even_numbers