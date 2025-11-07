'''
This module contains the encode function which swaps the case of all letters in a message
and replaces all vowels with the letter that appears two places ahead in the English alphabet.
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
    # Define the vowel mapping
    vowel_mapping = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    # Initialize the encoded message
    encoded_message = []
    # Iterate over each character in the message
    for char in message:
        if char in vowel_mapping:
            # Replace vowel with the mapped letter
            encoded_message.append(vowel_mapping[char])
        else:
            # Swap case of consonants
            encoded_message.append(char.swapcase())
    # Join the list into a string and return
    return ''.join(encoded_message)
# Example usage
if __name__ == "__main__":
    print(encode('test'))  # Output: 'TGST'
    print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'