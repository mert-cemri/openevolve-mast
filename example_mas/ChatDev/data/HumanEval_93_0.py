'''
This module contains the encode function which encodes a message by swapping the case of all letters and replacing vowels with the letter that appears two places ahead in the English alphabet.
'''
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # Mapping of vowels to their replacements
    vowel_map = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    # Initialize an empty list to store the encoded characters
    encoded_message = []
    # Iterate over each character in the message
    for char in message:
        # Swap case of the character
        swapped_char = char.swapcase()
        # Replace the character if it's a vowel
        if swapped_char in vowel_map:
            encoded_message.append(vowel_map[swapped_char])
        else:
            encoded_message.append(swapped_char)
    # Join the list into a string and return
    return ''.join(encoded_message)
# Example usage
if __name__ == "__main__":
    print(encode('test'))  # Output: 'TGST'
    print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'