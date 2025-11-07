'''
Question class to hold question data for the quiz application.
'''
class Question:
    def __init__(self, text, options, correct_answer):
        '''
        Initialize a new question.
        :param text: The question text.
        :param options: A list of answer options.
        :param correct_answer: The index of the correct answer in the options list.
        '''
        self.text = text
        self.options = options
        self.correct_answer = correct_answer