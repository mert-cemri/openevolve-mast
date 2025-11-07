'''
Change numerical base of input number x to base.
Return string representation after the conversion.
Base numbers are less than 10.
'''
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9, inclusive.")
    if x == 0:
        return "0"
    digits = []
    while x > 0:
        remainder = x % base
        digits.append(str(remainder))
        x = x // base
    # Reverse the digits to get the correct order
    digits.reverse()
    # Join the list into a string
    return ''.join(digits)