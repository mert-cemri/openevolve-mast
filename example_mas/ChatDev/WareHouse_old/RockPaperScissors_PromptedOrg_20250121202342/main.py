'''
This module implements a simple Rock-Paper-Scissors game where the user plays against the computer.
The user chooses one option, and the computer randomly picks one. The game compares results using the usual rules:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
The outcome is displayed, and the user can choose to replay the game.
'''
import random
class Game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
    def get_user_choice(self):
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        while user_choice not in self.choices:
            print("Invalid choice. Please try again.")
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        return user_choice
    def get_computer_choice(self):
        return random.choice(self.choices)
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "You win!"
        else:
            return "Computer wins!"
    def play(self):
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            replay = input("Do you want to play again? (yes/no): ").lower()
            if replay != "yes":
                print("Thanks for playing!")
                break
if __name__ == "__main__":
    game = Game()
    game.play()