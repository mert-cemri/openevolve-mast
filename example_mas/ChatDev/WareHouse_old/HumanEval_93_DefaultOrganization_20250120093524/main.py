'''
This module contains the encode function which transforms a given message by swapping the case of all letters and replacing vowels with the letter that appears two places ahead in the English alphabet.
'''
def encode(message):
    """
    Encodes the message by swapping case of all letters and replacing all vowels
    with the letter that appears 2 places ahead of that vowel in the English alphabet.
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
    vowels = 'aeiouAEIOU'
    vowel_replacement = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
                         'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
    encoded_message = []
    for char in message:
        if char in vowels:
            encoded_message.append(vowel_replacement[char])
        else:
            encoded_message.append(char.swapcase())
    return ''.join(encoded_message)