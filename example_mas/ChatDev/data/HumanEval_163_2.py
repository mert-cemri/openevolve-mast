'''
Given two positive integers a and b, return the even numbers between a
and b, in ascending order.
For example:
generate_integers(2, 8) => [2, 4, 6, 8]
generate_integers(8, 2) => [2, 4, 6, 8]
generate_integers(10, 14) => []
'''
def generate_integers(a, b):
    start = min(a, b)
    end = max(a, b)
    even_numbers = [n for n in range(start, end + 1) if n % 2 == 0]
    return even_numbers