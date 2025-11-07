'''
Main module to execute the Fibonacci number generator application.
'''
from fibonacci import generate_fibonacci_upto
def main():
    '''
    Main function to interact with the user and display Fibonacci numbers.
    '''
    try:
        limit = int(input("Enter the upper limit for Fibonacci numbers: "))
        if limit < 0:
            print("Please enter a non-negative integer.")
            return
        fibonacci_numbers = generate_fibonacci_upto(limit)
        print(f"Fibonacci numbers up to {limit}:")
        print(", ".join(map(str, fibonacci_numbers)))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()