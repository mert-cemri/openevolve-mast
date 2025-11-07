'''
For a given number n, find the largest number that divides n evenly, smaller than n.
'''
def largest_divisor(n: int) -> int:
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
# Example usage
if __name__ == "__main__":
    print(largest_divisor(15))  # Output should be 5