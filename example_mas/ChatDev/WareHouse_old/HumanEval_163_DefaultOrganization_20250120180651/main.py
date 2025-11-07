'''
Given two positive integers a and b, return the even digits between a
and b, in ascending order.
For example:
generate_integers(2, 8) => [2, 4, 6, 8]
generate_integers(8, 2) => [2, 4, 6, 8]
generate_integers(10, 14) => []
'''
def generate_integers(a, b):
    # Ensure a is less than or equal to b for range determination
    if a > b:
        a, b = b, a
    # Generate the list of even numbers between a and b inclusive
    even_numbers = [num for num in range(a, b + 1) if num % 2 == 0]
    return even_numbers