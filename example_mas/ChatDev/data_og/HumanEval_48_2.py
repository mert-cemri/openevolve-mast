'''
Checks if given string is a palindrome
'''
def is_palindrome(text: str) -> bool:
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    # Check if the cleaned text is equal to its reverse
    return cleaned_text == cleaned_text[::-1]