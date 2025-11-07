'''
This module contains the encode function which transforms a given message by swapping the case of all letters and replacing vowels with the letter that appears two places ahead in the English alphabet.
'''
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the English alphabet. 
    Assume only letters. 
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # Define a mapping for vowels to their replacements
    vowel_map = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    # Swap case and replace vowels
    encoded_message = []
    for char in message:
        # Swap case
        swapped_char = char.swapcase()
        # Replace vowel if applicable
        if swapped_char in vowel_map:
            encoded_message.append(vowel_map[swapped_char])
        else:
            encoded_message.append(swapped_char)
    return ''.join(encoded_message)
# Example usage
if __name__ == "__main__":
    print(encode('test'))  # Output: 'TGST'
    print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'