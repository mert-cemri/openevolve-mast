'''
This script implements a simple Rock-Paper-Scissors game where the user plays against the computer.
The user chooses one of Rock, Paper, or Scissors, and the computer randomly selects one.
The game determines the winner based on the standard rules and allows the user to play multiple rounds.
'''
import random
def main():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        if not play_again():
            break
    print("Thank you for playing!")
def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please try again.")
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"
def display_result(user_choice, computer_choice, winner):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")
def play_again():
    while True:
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input in ['yes', 'no']:
            return play_again_input == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
if __name__ == "__main__":
    main()