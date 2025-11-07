import difflib
def calculate_difference(text1, text2):
    diff = difflib.ndiff(text1, text2)
    return diff