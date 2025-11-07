'''
This module contains the encode function which transforms a given message by swapping the case of all letters and replacing vowels with the letter that appears two places ahead in the English alphabet.
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
    vowels = 'aeiouAEIOU'
    vowel_replacement = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
                         'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
    encoded_message = []
    for char in message:
        if char in vowels:
            # Replace vowel with the letter 2 places ahead
            encoded_message.append(vowel_replacement[char])
        else:
            # Swap case for consonants
            encoded_message.append(char.swapcase())
    return ''.join(encoded_message)
# Example usage
if __name__ == "__main__":
    print(encode('test'))  # Output: 'TGST'
    print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'