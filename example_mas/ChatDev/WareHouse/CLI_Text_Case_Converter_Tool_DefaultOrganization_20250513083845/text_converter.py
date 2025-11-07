'''
Text conversion functions for converting text to different cases.
'''
def to_uppercase(text):
    '''Convert text to uppercase.'''
    return text.upper()
def to_lowercase(text):
    '''Convert text to lowercase.'''
    return text.lower()
def to_titlecase(text):
    '''Convert text to title case.'''
    return text.title()
def to_sentencecase(text):
    '''Convert text to sentence case.'''
    sentences = text.split('. ')
    sentences = [sentence.capitalize() for sentence in sentences]
    return '. '.join(sentences)