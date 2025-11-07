'''
This module contains a function to convert a decimal number to a binary string
with a specific format.
'''
def decimal_to_binary(decimal):
    """Convert a decimal number to a binary string with 'db' at the start and end.
    Args:
        decimal (int): The decimal number to convert.
    Returns:
        str: The binary representation of the number with 'db' at the start and end.
    """
    # Convert the decimal number to binary and remove the '0b' prefix
    binary_str = bin(decimal)[2:]
    # Format the binary string with 'db' at the start and end
    return f"db{binary_str}db"