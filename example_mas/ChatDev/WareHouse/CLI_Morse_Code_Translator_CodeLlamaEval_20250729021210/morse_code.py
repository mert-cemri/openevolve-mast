import string
numbers = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}
morse_code_map = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}
def translate(text):
    # Convert text to uppercase
    text = text.upper()
    # Replace spaces with dots
    text = text.replace(" ", ".")
    # Replace letters with Morse code
    for letter in text:
        if letter in morse_code_map:
            text = text.replace(letter, morse_code_map[letter])
    # Replace numbers with Morse code
    for number in text:
        if number in numbers:
            text = text.replace(number, numbers[number])
    # Replace punctuation with Morse code
    for punctuation in text:
        if punctuation in punctuation:
            text = text.replace(punctuation, punctuation[ord(punctuation)])
    # Return translated text
    return text