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
    depth = 0
    for char in string:
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        # Check if there is any nesting
        if depth > 1:
            return True
        # Check for unbalanced brackets
        if depth < 0:
            return False
    return False