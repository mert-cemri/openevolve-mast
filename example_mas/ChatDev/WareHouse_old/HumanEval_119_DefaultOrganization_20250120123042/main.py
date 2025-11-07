'''
You are given a list of two strings, both strings consist of open
parentheses '(' or close parentheses ')' only.
Your job is to check if it is possible to concatenate the two strings in
some order, that the resulting string will be good.
A string S is considered to be good if and only if all parentheses in S
are balanced. For example: the string '(())()' is good, while the string
'())' is not.
Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.
Examples:
match_parens(['()(', ')']) == 'Yes'
match_parens([')', ')']) == 'No'
'''
def match_parens(lst):
    def unmatched_parens(s):
        open_count = 0
        close_count = 0
        for char in s:
            if char == '(':
                open_count += 1
            elif char == ')':
                if open_count > 0:
                    open_count -= 1
                else:
                    close_count += 1
        return open_count, close_count
    open1, close1 = unmatched_parens(lst[0])
    open2, close2 = unmatched_parens(lst[1])
    # Check both concatenation orders
    if (open1 == close2 and open2 == close1) or (open1 + open2 == close1 + close2):
        return 'Yes'
    else:
        return 'No'