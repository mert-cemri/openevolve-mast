'''
Write a function count_nums which takes an array of integers and returns
the number of elements which has a sum of digits > 0.
If a number is negative, then its first signed digit will be negative:
e.g. -123 has signed digits -1, 2, and 3.
>>> count_nums([]) == 0
>>> count_nums([-1, 11, -11]) == 1
>>> count_nums([1, 1, 2]) == 3
'''
def count_nums(arr):
    def sum_of_digits(n):
        # Convert number to string to iterate over digits
        s = str(n)
        # Initialize sum
        total = 0
        # If the number is negative, handle the first digit separately
        if s[0] == '-':
            total += int(s[0:2])  # Add the negative first digit
            s = s[2:]  # Remove the negative sign and first digit
        # Add the rest of the digits
        total += sum(int(digit) for digit in s)
        return total
    # Count numbers with sum of digits > 0
    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1
    return count
# Example usage
if __name__ == "__main__":
    print(count_nums([]))          # Output: 0
    print(count_nums([-1, 11, -11]))  # Output: 1
    print(count_nums([1, 1, 2]))   # Output: 3