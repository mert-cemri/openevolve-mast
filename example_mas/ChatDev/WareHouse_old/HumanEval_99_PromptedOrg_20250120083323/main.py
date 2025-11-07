'''
This module contains a function to find the closest integer to a given number,
rounding away from zero when the number is equidistant from two integers.
'''
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.
    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    # Convert the string to a float
    num = float(value)
    # Use the round function with a custom rounding rule
    if num > 0:
        return int(num + 0.5)
    else:
        return int(num - 0.5)
# Example usage
if __name__ == "__main__":
    print(closest_integer("10"))   # Output: 10
    print(closest_integer("15.3")) # Output: 15
    print(closest_integer("14.5")) # Output: 15
    print(closest_integer("-14.5"))# Output: -15