'''
question.py
This module contains the Question class, which represents a single quiz question.
'''
class Question:
    def __init__(self, text, options, correct_answer):
        '''
        Initialize a new Question instance.
        :param text: The question text.
        :param options: A list of possible answers.
        :param correct_answer: The correct answer.
        '''
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
    def check_answer(self, answer):
        '''
        Check if the provided answer is correct.
        :param answer: The user's answer.
        :return: True if the answer is correct, False otherwise.
        '''
        return str(answer).lower() == str(self.correct_answer).lower()