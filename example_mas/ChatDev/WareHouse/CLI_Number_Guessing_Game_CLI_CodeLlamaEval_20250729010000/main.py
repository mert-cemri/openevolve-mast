import random
import sys
def main():
    print("Welcome to the CLI number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 chances to guess it.")
    number = random.randint(1, 100)
    guess = 0
    chances = 10
    while guess != number and chances > 0:
        guess = int(input("Guess a number: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You guessed it!")
            break
        chances -= 1
    if guess == number:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost. The correct answer was", number)
if __name__ == "__main__":
    main()