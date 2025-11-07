'''
This file contains the Question class, which represents a trivia question.
'''
class Question:
    def __init__(self, text, options, correct_answer):
        '''
        Initialize a new Question instance.
        :param text: The text of the question.
        :param options: A list of possible answers.
        :param correct_answer: The correct answer to the question.
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
        return answer.lower() == self.correct_answer.lower()