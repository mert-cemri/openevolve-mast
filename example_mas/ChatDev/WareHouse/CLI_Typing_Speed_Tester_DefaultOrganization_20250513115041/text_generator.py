'''
Generates random paragraphs for the typing test.
'''
import random
def get_random_paragraph():
    paragraphs = [
        "The quick brown fox jumps over the lazy dog.",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Python is a great programming language for beginners.",
        "Typing speed tests are a fun way to improve your typing skills."
    ]
    return random.choice(paragraphs)