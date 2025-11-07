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
    while x:
        digits.append(str(x % base))
        x //= base
    return ''.join(reversed(digits))
# Example usage
if __name__ == "__main__":
    print(change_base(8, 3))  # Output: '22'
    print(change_base(8, 2))  # Output: '1000'
    print(change_base(7, 2))  # Output: '111'