'''
Manages the list of questions and tracks the current question and score.
'''
from question import Question
class QuizManager:
    def __init__(self):
        self.questions = [
            Question("What is the capital of France?", "Paris"),
            Question("What is 2 + 2?", "4"),
            Question("What is the largest planet in our solar system?", "Jupiter"),
        ]
        self.current_index = 0
    def get_current_question(self):
        return self.questions[self.current_index]
    def check_answer(self, answer):
        return self.questions[self.current_index].is_correct(answer)
    def next_question(self):
        if self.current_index < len(self.questions) - 1:
            self.current_index += 1
            return True
        return False
    def total_questions(self):
        return len(self.questions)