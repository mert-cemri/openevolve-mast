'''
Flashcard class to represent a single flashcard with a front and back.
'''
class Flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back
    def __str__(self):
        return f"Flashcard(front='{self.front}', back='{self.back}')"