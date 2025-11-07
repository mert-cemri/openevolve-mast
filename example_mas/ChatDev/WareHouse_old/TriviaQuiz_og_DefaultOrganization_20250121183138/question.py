'''
Defines the Question class to represent a single quiz question.
'''
class Question:
    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer
    def is_correct(self, answer):
        return self.correct_answer.lower() == answer.lower()