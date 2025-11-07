'''
Defines the QuestionBank class for managing a collection of questions.
'''
from question import Question
class QuestionBank:
    def __init__(self):
        self.questions = []
    def add_question(self, question):
        self.questions.append(question)
    def get_question(self, index):
        return self.questions[index]