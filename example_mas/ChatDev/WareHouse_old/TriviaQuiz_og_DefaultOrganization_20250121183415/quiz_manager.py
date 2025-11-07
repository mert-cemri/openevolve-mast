'''
Manages the list of questions, tracks the current question, and calculates the score.
'''
from question import Question
class QuizManager:
    def __init__(self):
        self.questions = [
            Question("What is the capital of France?", "Paris", ["Paris", "London", "Berlin", "Madrid"]),
            Question("What is 2 + 2?", "4"),
            Question("What is the largest planet in our solar system?", "Jupiter", ["Mars", "Earth", "Jupiter", "Saturn"]),
            # Add more questions as needed
        ]
        self.current_index = 0
    def get_next_question(self):
        if self.current_index < len(self.questions):
            question = self.questions[self.current_index]
            self.current_index += 1
            return question
        else:
            return None
    def total_questions(self):
        return len(self.questions)