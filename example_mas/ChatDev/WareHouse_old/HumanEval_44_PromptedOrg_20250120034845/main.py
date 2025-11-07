'''
Change numerical base of input number x to base.
Return string representation after the conversion.
Base numbers are less than 10.
'''
def change_base(x: int, base: int) -> str:
    if x == 0:
        return "0"
    digits = []
    while x > 0:
        remainder = x % base
        digits.append(str(remainder))
        x = x // base
    # Reverse the digits to get the correct order
    digits.reverse()
    return ''.join(digits)