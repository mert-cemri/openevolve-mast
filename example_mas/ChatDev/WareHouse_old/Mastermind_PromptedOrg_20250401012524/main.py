'''
Main executable file for the Mastermind game.
'''
from game import MastermindGame
def main():
    print("🎲 Welcome to Mastermind! 🎲")
    code_length = 4
    max_attempts = 10
    digit_range = 6  # Digits from 0 to 5
    game = MastermindGame(code_length, max_attempts, digit_range)
    print(f"\n🔒 I have selected a hidden sequence of {code_length} digits (0-{digit_range - 1}).")
    print(f"You have {max_attempts} attempts to guess it correctly. Good luck! 🍀\n")
    attempts = 0
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess (e.g., 1234): ")
        if len(guess) != code_length or not guess.isdigit() or any(int(digit) >= digit_range for digit in guess):
            print(f"❗ Invalid guess. Please enter exactly {code_length} digits between 0 and {digit_range - 1}. ❗\n")
            continue
        exact, partial = game.evaluate_guess(guess)
        attempts += 1
        if game.is_correct_guess(guess):
            print(f"\n🎉 Congratulations! You've cracked the code '{game.hidden_code}' in {attempts} attempts! 🎉")
            break
        else:
            print(f"✅ Exact matches (correct digit and position): {exact}")
            print(f"🔄 Partial matches (correct digit, wrong position): {partial}\n")
    else:
        print(f"\n❌ Game Over! You've used all {max_attempts} attempts. The correct code was '{game.hidden_code}'. ❌")
if __name__ == "__main__":
    main()