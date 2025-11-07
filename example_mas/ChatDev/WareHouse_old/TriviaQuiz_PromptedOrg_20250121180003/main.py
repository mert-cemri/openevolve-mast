'''
main.py
This is the main module to run the trivia quiz application.
'''
from quiz import Quiz
from question import Question
def main():
    '''
    Main function to run the quiz application.
    '''
    questions = [
        Question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris"),
        Question("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
        Question("Who wrote 'Hamlet'?", ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"], "William Shakespeare")
    ]
    quiz = Quiz(questions)
    quiz.start()
if __name__ == "__main__":
    main()