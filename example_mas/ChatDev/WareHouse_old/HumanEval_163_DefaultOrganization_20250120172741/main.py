'''
Given two positive integers a and b, return the even digits between a
and b, in ascending order.
For example:
generate_integers(2, 8) => [2, 4, 6, 8]
generate_integers(8, 2) => [2, 4, 6, 8]
generate_integers(10, 14) => []
'''
def generate_integers(a, b):
    # Determine the start and end of the range
    start = min(a, b)
    end = max(a, b)
    # Collect even numbers in the range [start, end]
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    return even_numbers