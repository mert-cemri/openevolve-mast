'''
Defines the Question class for the machine learning quiz.
'''
class Question:
    def __init__(self, text, options, correct_answer):
        '''
        Initialize the question with text, options, and the index of the correct answer.
        '''
        self.text = text
        self.options = options
        self.correct_answer = correct_answer