'''
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
'''
def encode(message):
    vowels = 'aeiouAEIOU'
    vowel_replacements = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    encoded_message = []
    for char in message:
        if char in vowels:
            # Replace vowel with the letter 2 places ahead
            encoded_char = vowel_replacements[char]
        else:
            # Keep the character as is
            encoded_char = char
        # Swap case
        if encoded_char.islower():
            encoded_message.append(encoded_char.upper())
        else:
            encoded_message.append(encoded_char.lower())
    return ''.join(encoded_message)
# Example usage
if __name__ == "__main__":
    print(encode('test'))  # Output: 'TGST'
    print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'