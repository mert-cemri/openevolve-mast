'''
Defines the Question class for the trivia quiz program.
'''
class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer