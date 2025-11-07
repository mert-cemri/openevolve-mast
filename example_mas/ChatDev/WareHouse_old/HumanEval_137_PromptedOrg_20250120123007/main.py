'''
Create a function that takes integers, floats, or strings representing
real numbers, and returns the larger variable in its given variable type.
Return None if the values are equal.
Note: If a real number is represented as a string, the floating point might be . or ,
compare_one(1, 2.5) ➞ 2.5
compare_one(1, "2,3") ➞ "2,3"
compare_one("5,1", "6") ➞ "6"
compare_one("1", 1) ➞ None
'''
def compare_one(a, b):
    def parse_value(value):
        if isinstance(value, str):
            # Replace comma with dot for float conversion
            value = value.replace(',', '.')
            try:
                return float(value)
            except ValueError:
                return value  # Return original if not a valid float
        return value
    # Parse both values
    parsed_a = parse_value(a)
    parsed_b = parse_value(b)
    # Compare the parsed values
    if parsed_a == parsed_b:
        return None
    elif parsed_a > parsed_b:
        return a
    else:
        return b