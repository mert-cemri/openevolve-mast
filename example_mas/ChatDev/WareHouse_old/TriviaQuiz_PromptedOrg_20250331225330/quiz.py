'''
Defines the Quiz class and the function to load questions.
'''
from question import Question
class Quiz:
    def __init__(self, questions, show_answers=False):
        '''
        Initializes the quiz.
        :param questions: List of Question objects.
        :param show_answers: Boolean indicating if correct answers should be shown after quiz.
        '''
        self.questions = questions
        self.score = 0
        self.show_answers = show_answers
        self.user_answers = []
    def start(self):
        '''
        Starts the quiz, presents questions, and collects answers.
        '''
        for question in self.questions:
            question.display()
            answer = input("Your answer: ").strip()
            if question.options:
                # Validate numeric answer and convert to option text if applicable
                while True:
                    if answer.isdigit() and 1 <= int(answer) <= len(question.options):
                        answer = question.options[int(answer) - 1]
                        break
                    else:
                        matched_options = [opt for opt in question.options if opt.lower() == answer.lower().strip()]
                        if matched_options:
                            answer = matched_options[0]  # Normalize to exact option text
                            break
                        else:
                            print("Invalid input. Please enter the option number or exact option text.")
                            answer = input("Your answer: ").strip()
            self.user_answers.append((question, answer))
            if question.is_correct(answer):
                self.score += 1
        self.display_results()
    def display_results(self):
        '''
        Displays the final score and optionally the correct answers.
        '''
        print("\nQuiz Completed!")
        print(f"Your total score: {self.score}/{len(self.questions)}")
        if self.show_answers:
            print("\nCorrect Answers:")
            for idx, (question, user_answer) in enumerate(self.user_answers, start=1):
                correctness = "Correct" if question.is_correct(user_answer) else "Incorrect"
                print(f"{idx}. {question.text}")
                print(f"Your answer: {user_answer} ({correctness})")
                print(f"Correct answer: {question.correct_answer}\n")
def load_questions():
    '''
    Loads and returns a configurable set of questions.
    '''
    # Example question bank, can be expanded or loaded from external sources
    return [
        Question(
            text="What is the capital of France?",
            correct_answer="Paris",
            options=["Paris", "London", "Berlin", "Madrid"]
        ),
        Question(
            text="Who wrote 'Romeo and Juliet'?",
            correct_answer="William Shakespeare",
            options=["William Shakespeare", "Charles Dickens", "Leo Tolstoy", "Mark Twain"]
        ),
        Question(
            text="What is the chemical symbol for water?",
            correct_answer="H2O"
        ),
        Question(
            text="Which planet is known as the Red Planet?",
            correct_answer="Mars",
            options=["Earth", "Mars", "Jupiter", "Saturn"]
        ),
        Question(
            text="In which year did the Titanic sink?",
            correct_answer="1912"
        )
    ]