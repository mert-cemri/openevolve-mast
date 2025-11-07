'''
Change numerical base of input number x to base.
Return string representation after the conversion.
Base numbers are less than 10.
'''
def change_base(x: int, base: int) -> str:
    if x < 0 or base <= 1 or base >= 10:
        raise ValueError("Invalid input: x must be non-negative and base must be between 2 and 9.")
    if x == 0:
        return "0"
    digits = []
    while x > 0:
        remainder = x % base
        digits.append(str(remainder))
        x = x // base
    # Reverse the list to get the correct order
    digits.reverse()
    # Join the list into a string
    return ''.join(digits)
# Example usage
if __name__ == "__main__":
    print(change_base(8, 3))  # Output: '22'
    print(change_base(8, 2))  # Output: '1000'
    print(change_base(7, 2))  # Output: '111'