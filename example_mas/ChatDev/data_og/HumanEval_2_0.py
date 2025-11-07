'''
Given a positive floating point number, it can be decomposed into
an integer part (largest integer smaller than given number) and decimals
(leftover part always smaller than 1).
Return the decimal part of the number.
>>> truncate_number(3.5)
0.5
'''
def truncate_number(number: float) -> float:
    # Extract the integer part using int() and subtract it from the original number
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
# Example usage
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output should be 0.5