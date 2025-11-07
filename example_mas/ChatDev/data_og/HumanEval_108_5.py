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
    def digit_sum(n):
        # Convert number to string to handle each digit
        s = str(n)
        # Initialize sum
        total = 0
        # If negative, start with the first digit as negative
        if s[0] == '-':
            total += int(s[0] + s[1])  # Add the first digit as negative
            s = s[2:]  # Remove the first two characters
        # Add the rest of the digits
        total += sum(int(d) for d in s)
        return total
    # Count numbers with digit sum > 0
    count = sum(1 for num in arr if digit_sum(num) > 0)
    return count