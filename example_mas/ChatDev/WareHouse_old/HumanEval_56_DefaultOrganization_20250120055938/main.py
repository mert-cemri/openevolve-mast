'''
Function to check if every opening bracket has a corresponding closing bracket.
brackets is a string of "<" and ">".
return True if every opening bracket has a corresponding closing bracket.
>>> correct_bracketing("<")
False
>>> correct_bracketing("<>")
True
>>> correct_bracketing("<<><>>")
True
>>> correct_bracketing("><<>")
False
'''
def correct_bracketing(brackets: str) -> bool:
    count = 0
    for char in brackets:
        if char == '<':
            count += 1
        elif char == '>':
            count -= 1
        # If count is negative, there are unmatched closing brackets
        if count < 0:
            return False
    # If count is zero, all brackets are matched
    return count == 0