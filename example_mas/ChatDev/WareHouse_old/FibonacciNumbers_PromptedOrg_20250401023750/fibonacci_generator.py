'''
Module to generate Fibonacci numbers up to a given number.
'''
def generate_fibonacci_upto(n: int) -> list[int]:
    '''
    Generates a list of Fibonacci numbers up to and including the given number n.
    Parameters:
        n (int): The upper limit for the Fibonacci numbers to generate.
    Returns:
        list[int]: A list containing Fibonacci numbers up to n.
    '''
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    fibonacci_numbers = [0, 1]
    if n == 0:
        return [0]
    next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    while next_number <= n:
        fibonacci_numbers.append(next_number)
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    return fibonacci_numbers