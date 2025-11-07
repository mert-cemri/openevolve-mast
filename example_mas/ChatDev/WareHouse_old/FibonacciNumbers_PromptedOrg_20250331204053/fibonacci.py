'''
Module responsible for generating Fibonacci numbers.
'''
def generate_fibonacci_upto(limit):
    '''
    Generate Fibonacci numbers up to a given limit.
    Parameters:
        limit (int): The upper limit for Fibonacci numbers generation.
    Returns:
        list: A list of Fibonacci numbers up to the given limit.
    '''
    fibonacci_numbers = []
    a, b = 0, 1
    while a <= limit:
        fibonacci_numbers.append(a)
        a, b = b, a + b
    return fibonacci_numbers