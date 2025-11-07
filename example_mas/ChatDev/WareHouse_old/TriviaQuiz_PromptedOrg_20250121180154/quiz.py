'''
This file contains the Quiz class, which manages the quiz process.
'''
from question import Question
class Quiz:
    def __init__(self):
        '''
        Initialize a new Quiz instance.
        '''
        self.questions = []
        self.score = 0
    def add_question(self, question):
        '''
        Add a question to the quiz.
        :param question: An instance of the Question class.
        '''
        self.questions.append(question)
    def conduct_quiz(self):
        '''
        Conduct the quiz by asking each question to the user.
        '''
        for question in self.questions:
            print(question.text)
            if question.options:
                for i, option in enumerate(question.options, 1):
                    print(f"{i}. {option}")
                while True:
                    try:
                        answer = int(input("Enter the number of your answer: "))
                        if 1 <= answer <= len(question.options):
                            user_answer = question.options[answer - 1]
                            break
                        else:
                            print("Please enter a number corresponding to the options.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            else:
                user_answer = input("Enter your answer: ")
            if question.check_answer(user_answer):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {question.correct_answer}")
            print()
    def display_score(self):
        '''
        Display the user's total score after the quiz.
        '''
        print(f"Your total score is: {self.score}/{len(self.questions)}")