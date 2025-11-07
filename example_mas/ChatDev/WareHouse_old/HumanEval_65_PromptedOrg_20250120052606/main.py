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
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string to manipulate the digits
    x_str = str(x)
    num_digits = len(x_str)
    # If shift is greater than or equal to the number of digits, return reversed digits
    if shift >= num_digits:
        return x_str[::-1]
    # Calculate the effective shift
    effective_shift = shift % num_digits
    # Perform the circular shift
    shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]
    return shifted_str
# Example usage
if __name__ == "__main__":
    print(circular_shift(12, 1))  # Output: "21"
    print(circular_shift(12, 2))  # Output: "12"