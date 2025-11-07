'''
This module contains the implementation of the function `count_nums` which
counts the number of integers in an array whose sum of digits is greater than 0.
'''
def sum_of_digits(n):
    """
    Calculate the sum of digits of an integer n.
    If n is negative, the first digit is considered negative.
    """
    n_str = str(n)
    if n_str[0] == '-':
        # If the number is negative, start with the negative of the first digit
        digit_sum = -int(n_str[1])
        start_index = 2
    else:
        digit_sum = int(n_str[0])
        start_index = 1
    # Add the rest of the digits
    for char in n_str[start_index:]:
        digit_sum += int(char)
    return digit_sum
def count_nums(arr):
    """
    Count the number of elements in the array whose sum of digits is greater than 0.
    :param arr: List of integers
    :return: Integer count of elements with sum of digits > 0
    """
    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1
    return count
# Example usage
if __name__ == "__main__":
    print(count_nums([]))  # Output: 0
    print(count_nums([-1, 11, -11]))  # Output: 1
    print(count_nums([1, 1, 2]))  # Output: 3