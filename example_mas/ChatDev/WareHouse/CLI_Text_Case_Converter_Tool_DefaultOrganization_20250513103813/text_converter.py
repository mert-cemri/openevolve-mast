'''
Text conversion functions for different cases.
'''
def to_uppercase(text):
    return text.upper()
def to_lowercase(text):
    return text.lower()
def to_title_case(text):
    return text.title()
def to_sentence_case(text):
    sentences = text.split('. ')
    sentences = [s.capitalize() for s in sentences]
    return '. '.join(sentences)