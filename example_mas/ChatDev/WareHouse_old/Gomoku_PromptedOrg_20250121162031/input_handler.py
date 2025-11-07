'''
InputHandler class to handle user input for the Gomoku game.
'''
class InputHandler:
    def get_valid_input(self, prompt, size):
        while True:
            try:
                value = int(input(prompt))
                if 0 <= value < size:
                    return value
                else:
                    print(f"Please enter a number between 0 and {size - 1}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")