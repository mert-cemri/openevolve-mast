'''
Defines the Question class to represent each quiz question.
'''
class Question:
    def __init__(self, text, correct_answer, choices=None):
        self.text = text
        self.correct_answer = correct_answer
        self.choices = choices  # Add choices parameter to support multiple-choice questions