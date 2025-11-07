'''
quiz.py
This module contains the Quiz class, which manages the quiz process, including loading questions, tracking the score, and displaying results.
'''
from question import Question
class Quiz:
    def __init__(self, questions):
        '''
        Initialize a new Quiz instance.
        :param questions: A list of Question objects.
        '''
        self.questions = questions
        self.score = 0
    def start(self):
        '''
        Start the quiz, presenting each question to the user and tracking the score.
        '''
        for question in self.questions:
            self.present_question(question)
        self.display_score()
    def present_question(self, question):
        '''
        Present a question to the user and check the answer.
        :param question: A Question object.
        '''
        print(question.text)
        for i, option in enumerate(question.options, 1):
            print(f"{i}. {option}")
        while True:
            try:
                answer = int(input("Enter the number of your answer: "))
                if 1 <= answer <= len(question.options):
                    break
                else:
                    print("Please enter a number corresponding to one of the options.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        if question.check_answer(question.options[answer - 1]):
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer was: {question.correct_answer}\n")
    def display_score(self):
        '''
        Display the user's total score after the quiz.
        '''
        print(f"Your total score is: {self.score}/{len(self.questions)}")