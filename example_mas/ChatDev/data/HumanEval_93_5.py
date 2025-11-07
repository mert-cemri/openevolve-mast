'''
This module contains the encode function which transforms a given message by swapping the case of all letters and replacing vowels with the letter that appears two places ahead in the English alphabet.
'''
def encode(message):
    """
    Encode a message by swapping the case of all letters and replacing
    vowels with the letter that appears 2 places ahead in the alphabet.
    Parameters:
    message (str): The input message consisting of only letters.
    Returns:
    str: The encoded message.
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # Define the vowel mapping
    vowel_mapping = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    # Swap case and replace vowels
    encoded_message = []
    for char in message:
        # Swap case
        swapped_char = char.swapcase()
        # Replace vowel if applicable
        if swapped_char in vowel_mapping:
            encoded_message.append(vowel_mapping[swapped_char])
        else:
            encoded_message.append(swapped_char)
    return ''.join(encoded_message)