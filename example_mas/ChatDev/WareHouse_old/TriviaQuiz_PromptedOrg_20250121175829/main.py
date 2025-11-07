'''
This is the main entry point for the trivia quiz application. It initializes the quiz and starts the game.
'''
from quiz import Quiz
from quiz_interface import QuizInterface
def main():
    # Initialize the quiz with a set of questions
    questions = [
        {"question": "What is the capital of France?", "choices": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
        {"question": "What is 2 + 2?", "choices": ["3", "4", "5", "6"], "answer": "4"},
        {"question": "What is the largest planet in our solar system?", "choices": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"}
    ]
    quiz = Quiz(questions)
    interface = QuizInterface(quiz)
    interface.start_quiz()
if __name__ == "__main__":
    main()