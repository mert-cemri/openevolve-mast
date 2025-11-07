'''
This module contains the encode function which encodes a message by swapping the case of all letters and replacing vowels with the letter that appears two places ahead in the English alphabet.
'''
def encode(message):
    """
    Encodes a message by swapping the case of all letters and replacing vowels with the letter that appears two places ahead in the English alphabet.
    Args:
    message (str): The message to encode.
    Returns:
    str: The encoded message.
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = 'aeiouAEIOU'
    vowel_replacements = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
                          'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
    encoded_message = []
    for char in message:
        if char in vowels:
            encoded_message.append(vowel_replacements[char])
        else:
            encoded_message.append(char.swapcase())
    return ''.join(encoded_message)
# Example usage
if __name__ == "__main__":
    print(encode('test'))  # Output: 'TGST'
    print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'