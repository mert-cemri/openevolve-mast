'''
This module contains the QuizInterface class, which handles user interaction, presenting questions, collecting answers, and displaying the final score.
'''
class QuizInterface:
    def __init__(self, quiz):
        self.quiz = quiz
    def start_quiz(self):
        while self.quiz.has_more_questions():
            question = self.quiz.get_next_question()
            self.display_question(question)
            user_answer = input("Your answer: ")
            if self.quiz.check_answer(question, user_answer):
                print("Correct!\n")
            else:
                print(f"Wrong! The correct answer was: {question.answer}\n")
        self.display_final_score()
    def display_question(self, question):
        print(f"Q: {question.text}")
        for i, choice in enumerate(question.choices):
            print(f"{i + 1}. {choice}")
    def display_final_score(self):
        score = self.quiz.get_score()
        total = self.quiz.get_total_questions()
        print(f"Quiz finished! Your score: {score}/{total}")