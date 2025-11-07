'''
This module contains the Quiz class, which manages the quiz logic, including loading questions, tracking the score, and displaying results.
'''
from question import Question
class Quiz:
    def __init__(self, questions_data):
        self.questions = [Question(q["question"], q["choices"], q["answer"]) for q in questions_data]
        self.score = 0
        self.current_question_index = 0
    def has_more_questions(self):
        return self.current_question_index < len(self.questions)
    def get_next_question(self):
        question = self.questions[self.current_question_index]
        self.current_question_index += 1
        return question
    def check_answer(self, question, answer):
        if question.is_correct(answer):
            self.score += 1
            return True
        return False
    def get_score(self):
        return self.score
    def get_total_questions(self):
        return len(self.questions)