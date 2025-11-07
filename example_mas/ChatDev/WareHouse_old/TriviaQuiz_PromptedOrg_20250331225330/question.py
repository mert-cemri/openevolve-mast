'''
Defines the Question class used to represent quiz questions.
'''
class Question:
    def __init__(self, text, correct_answer, options=None):
        '''
        Initializes a question.
        :param text: The question text.
        :param correct_answer: The correct answer (string).
        :param options: List of options for multiple-choice questions. None for short-answer questions.
        '''
        self.text = text
        self.correct_answer = correct_answer.lower().strip()
        self.options = options
    def is_correct(self, answer):
        '''
        Checks if the provided answer is correct.
        :param answer: User's answer.
        :return: Boolean indicating correctness.
        '''
        return answer.lower().strip() == self.correct_answer
    def display(self):
        '''
        Displays the question and options if available.
        '''
        print("\n" + self.text)
        if self.options:
            for idx, option in enumerate(self.options, start=1):
                print(f"{idx}. {option}")