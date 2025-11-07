'''
Handles command-line interface interactions.
'''
class CLI:
    def get_command(self):
        return input("Enter command: ").strip().lower()
    def display_message(self, message):
        print(message)