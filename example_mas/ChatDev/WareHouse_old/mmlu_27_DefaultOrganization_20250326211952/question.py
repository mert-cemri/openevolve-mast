'''
This file contains the Question class which holds the question text, options, and the correct answer index.
'''
class Question:
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index
    def get_correct_answer(self):
        return self.correct_index