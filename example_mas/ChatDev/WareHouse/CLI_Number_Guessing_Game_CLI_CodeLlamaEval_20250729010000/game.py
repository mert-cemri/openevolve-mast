import random
class Game:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guess = 0
        self.chances = 10
    def play(self):
        while self.guess != self.number and self.chances > 0:
            self.guess = int(input("Guess a number: "))
            if self.guess < self.number:
                print("Too low!")
            elif self.guess > self.number:
                print("Too high!")
            else:
                print("You guessed it!")
                break
            self.chances -= 1
        if self.guess == self.number:
            print("Congratulations, you won!")
        else:
            print("Sorry, you lost. The correct answer was", self.number)
        return self.guess == self.number