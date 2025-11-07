'''
Main file to run the trivia quiz application.
'''
from quiz import Quiz, load_questions
def main():
    print("Welcome to the Trivia Quiz!")
    questions = load_questions()
    # Ask user if they want to see correct answers after the quiz
    show_answers_input = input("Would you like to see correct answers after the quiz? (yes/no): ").strip().lower()
    while show_answers_input not in ('yes', 'no'):
        print("Please enter 'yes' or 'no'.")
        show_answers_input = input("Would you like to see correct answers after the quiz? (yes/no): ").strip().lower()
    show_answers = show_answers_input == 'yes'
    quiz = Quiz(questions, show_answers)
    quiz.start()
if __name__ == "__main__":
    main()