'''
This module contains a function to convert a decimal number to a binary string
with 'db' at the beginning and end.
'''
def decimal_to_binary(decimal):
    """Convert a decimal number to a binary string with 'db' at the beginning and end.
    Args:
        decimal (int): The decimal number to convert.
    Returns:
        str: The binary representation of the decimal number, formatted with 'db' at the beginning and end.
    """
    # Convert the decimal number to binary and remove the '0b' prefix
    binary_representation = bin(decimal)[2:]
    # Format the binary string with 'db' at the beginning and end
    return f"db{binary_representation}db"
# Example usage:
# print(decimal_to_binary(15))  # Output: "db1111db"
# print(decimal_to_binary(32))  # Output: "db100000db"