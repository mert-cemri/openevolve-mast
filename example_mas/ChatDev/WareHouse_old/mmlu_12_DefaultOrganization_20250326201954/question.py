'''
Question class and create_question function for the moral scenarios quiz.
'''
class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
def create_question():
    text = ("For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, "
            "according to ordinary moral standards in the US as of 2020?\n"
            "Scenario 1 | I built a snowman inside the beautiful home.\n"
            "Scenario 2 | I popped the balloon and gave it back to the child.")
    options = [
        "Wrong, Wrong",
        "Wrong, Not wrong",
        "Not wrong, Wrong",
        "Not wrong, Not wrong"
    ]
    correct_answer = 1  # "Wrong, Not wrong"
    return Question(text, options, correct_answer)