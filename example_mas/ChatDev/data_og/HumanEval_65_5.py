'''
Circular shift the digits of the integer x, shift the digits right by shift
and return the result as a string.
If shift > number of digits, return digits reversed.
>>> circular_shift(12, 1)
"21"
>>> circular_shift(12, 2)
"12"
'''
def circular_shift(x, shift):
    # Convert the integer to a string to work with its digits
    x_str = str(x)
    num_digits = len(x_str)
    # If shift is greater than the number of digits, return the reversed string
    if shift >= num_digits:
        return x_str[::-1]
    # Perform the circular shift
    shift = shift % num_digits  # In case shift is greater than num_digits
    shifted_str = x_str[-shift:] + x_str[:-shift]
    return shifted_str