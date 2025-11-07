'''
This module contains a function to encode a message by swapping the case of all letters and replacing vowels with the letter that appears two places ahead in the alphabet.
'''
def encode(message):
    """
    Encode a message by swapping case and replacing vowels.
    Args:
    message (str): The input message consisting of letters.
    Returns:
    str: The encoded message with swapped case and modified vowels.
    """
    # Define a mapping for vowels to their replacements
    vowel_mapping = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    # Initialize an empty list to store the encoded characters
    encoded_message = []
    # Iterate over each character in the message
    for char in message:
        # Swap the case of the character
        swapped_char = char.swapcase()
        # Replace the vowel if it is in the mapping
        if swapped_char in vowel_mapping:
            encoded_message.append(vowel_mapping[swapped_char])
        else:
            encoded_message.append(swapped_char)
    # Join the list into a string and return
    return ''.join(encoded_message)