'''
This module contains the Feedback class, which handles the feedback mechanism, determining how many colors are correct and in the correct position.
'''
class Feedback:
    @staticmethod
    def evaluate(secret_sequence, guess_sequence):
        correct_position = sum(s == g for s, g in zip(secret_sequence, guess_sequence))
        # Create a copy of the secret sequence to track used colors
        secret_copy = secret_sequence[:]
        # Create a copy of the guess sequence to track used guesses
        guess_copy = guess_sequence[:]
        # Remove correctly positioned colors from both copies
        for i in range(len(secret_sequence)):
            if secret_sequence[i] == guess_sequence[i]:
                secret_copy.remove(secret_sequence[i])
                guess_copy.remove(guess_sequence[i])
        # Calculate correct color ignoring positions
        correct_color = 0
        for color in guess_copy:
            if color in secret_copy:
                correct_color += 1
                secret_copy.remove(color)
        return {'correct_position': correct_position, 'correct_color': correct_color}