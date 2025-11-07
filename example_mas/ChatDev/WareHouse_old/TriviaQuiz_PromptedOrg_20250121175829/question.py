'''
This module contains the Question class, which represents a single quiz question, including the question text, possible answers, and the correct answer.
'''
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def is_correct(self, user_answer):
        return user_answer.lower() == self.answer.lower()