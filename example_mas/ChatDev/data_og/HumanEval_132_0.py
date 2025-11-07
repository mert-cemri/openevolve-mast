'''
Create a function that takes a string as input which contains only square brackets.
The function should return True if and only if there is a valid subsequence of brackets 
where at least one bracket in the subsequence is nested.
is_nested('[[]]') ➞ True
is_nested('[]]]]]]][[[[[]') ➞ False
is_nested('[][]') ➞ False
is_nested('[]') ➞ False
is_nested('[[][]]') ➞ True
is_nested('[[]][[') ➞ True
'''
def is_nested(string):
    # Initialize a counter to track the balance of brackets
    balance = 0
    # Flag to check if any nesting is found
    nested = False
    # Iterate through each character in the string
    for char in string:
        if char == '[':
            balance += 1
        elif char == ']':
            balance -= 1
        # Check if there is nesting
        if balance > 1:
            nested = True
        # If balance goes negative, it means there are unmatched closing brackets
        if balance < 0:
            return False
    # Ensure all brackets are matched and at least one nesting was found
    return nested and balance == 0