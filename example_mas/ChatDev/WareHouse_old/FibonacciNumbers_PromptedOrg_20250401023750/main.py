'''
Main executable file for generating Fibonacci numbers.
'''
from fibonacci_generator import generate_fibonacci_upto
def main():
    '''
    Entry point of the application. Handles user input and prints Fibonacci numbers.
    '''
    try:
        user_input = input("Enter a non-negative integer to generate Fibonacci numbers up to: ")
        n = int(user_input)
        fibonacci_numbers = generate_fibonacci_upto(n)
        print(f"Fibonacci numbers up to {n}: {fibonacci_numbers}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()