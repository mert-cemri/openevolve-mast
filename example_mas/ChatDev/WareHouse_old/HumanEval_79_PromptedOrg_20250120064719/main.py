'''
This module contains a function to convert a decimal number to a binary string
with specific formatting.
'''
def decimal_to_binary(decimal):
    """Convert a decimal number to a binary string with 'db' at the start and end.
    Args:
        decimal (int): The decimal number to convert.
    Returns:
        str: The binary representation of the decimal number with 'db' at the start and end.
    """
    # Convert the decimal number to binary and remove the '0b' prefix
    binary_str = bin(decimal)[2:]
    # Format the binary string with 'db' at the start and end
    formatted_binary = f"db{binary_str}db"
    return formatted_binary