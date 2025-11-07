'''
This function checks if there is a valid subsequence of brackets
where at least one bracket in the subsequence is nested.
'''
def is_nested(string):
    # Initialize a counter to track the balance of brackets
    balance = 0
    # Flag to indicate if we have seen a nested bracket
    nested = False
    # Iterate through each character in the string
    for char in string:
        if char == '[':
            balance += 1
            # Check if we have a nested bracket
            if balance > 1:
                nested = True
        elif char == ']':
            balance -= 1
        # Check for invalid sequence
        if balance < 0:
            return False
    # Return True if a nested bracket was found, otherwise False
    return nested