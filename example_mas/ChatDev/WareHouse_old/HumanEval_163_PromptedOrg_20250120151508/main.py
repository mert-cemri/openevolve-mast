'''
Given two positive integers a and b, return the even digits between a
and b, in ascending order.
For example:
generate_integers(2, 8) => [2, 4, 6, 8]
generate_integers(8, 2) => [2, 4, 6, 8]
generate_integers(10, 14) => []
'''
def generate_integers(a, b):
    # Ensure a is less than or equal to b
    if a > b:
        a, b = b, a
    # Generate even integers between a and b
    even_integers = [i for i in range(a, b + 1) if i % 2 == 0]
    return even_integers