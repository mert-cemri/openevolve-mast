'''
This is the main file that initializes and runs the trivia quiz program.
'''
from quiz import Quiz
from question import Question
def main():
    '''
    Main function to run the trivia quiz.
    '''
    quiz = Quiz()
    # Example questions
    q1 = Question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris")
    q2 = Question("What is 2 + 2?", ["3", "4", "5", "6"], "4")
    q3 = Question("Who wrote 'Hamlet'?", ["Charles Dickens", "William Shakespeare", "Mark Twain", "J.K. Rowling"], "William Shakespeare")
    q4 = Question("What is the chemical symbol for water?", [], "H2O")
    # Add questions to the quiz
    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)
    quiz.add_question(q4)
    # Conduct the quiz
    quiz.conduct_quiz()
    # Display the final score
    quiz.display_score()
if __name__ == "__main__":
    main()