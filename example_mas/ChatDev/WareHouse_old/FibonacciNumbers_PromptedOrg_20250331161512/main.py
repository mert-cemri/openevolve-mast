'''
This module provides a function to generate Fibonacci numbers up to a given number
and a main block to execute the program.
'''
def generate_fibonacci(n):
    '''
    Generates Fibonacci numbers up to a given number n.
    Parameters:
    n (int): The upper limit for the Fibonacci sequence.
    Returns:
    list: A list of Fibonacci numbers up to n.
    '''
    if n < 0:
        return []
    fibonacci_sequence = []
    a, b = 0, 1
    while a <= n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence
if __name__ == "__main__":
    # Prompt the user for input
    try:
        user_input = int(input("Enter a number to generate Fibonacci numbers up to: "))
        # Generate and display the Fibonacci sequence
        fibonacci_sequence = generate_fibonacci(user_input)
        print(f"Fibonacci numbers up to {user_input}: {fibonacci_sequence}")
    except ValueError:
        print("Please enter a valid integer.")