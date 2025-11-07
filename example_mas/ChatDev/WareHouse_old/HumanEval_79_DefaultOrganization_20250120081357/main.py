'''
This module contains a function to convert a decimal number to a binary string
with specific formatting requirements.
'''
def decimal_to_binary(decimal):
    """Convert a decimal number to a binary string with 'db' at the beginning and end.
    Args:
        decimal (int): The decimal number to convert.
    Returns:
        str: The binary representation of the decimal number with 'db' at the beginning and end.
    """
    # Convert the decimal number to binary and remove the '0b' prefix
    binary_str = bin(decimal)[2:]
    # Add 'db' at the beginning and end of the binary string
    formatted_binary_str = f"db{binary_str}db"
    return formatted_binary_str
# Example usage:
# print(decimal_to_binary(15))  # Output: "db1111db"
# print(decimal_to_binary(32))  # Output: "db100000db"