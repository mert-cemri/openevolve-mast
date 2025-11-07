'''
Change numerical base of input number x to base.
Return string representation after the conversion.
Base numbers are less than 10.
'''
def change_base(x: int, base: int) -> str:
    if x == 0:
        return "0"
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    # The digits are collected in reverse order
    digits.reverse()
    return ''.join(digits)
# Example usage
if __name__ == "__main__":
    print(change_base(8, 3))  # Output: '22'
    print(change_base(8, 2))  # Output: '1000'
    print(change_base(7, 2))  # Output: '111'