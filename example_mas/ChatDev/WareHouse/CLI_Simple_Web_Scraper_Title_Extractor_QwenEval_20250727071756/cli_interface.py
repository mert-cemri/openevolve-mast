'''
Handles the command-line interface interactions.
'''
class CLIInterface:
    def get_user_input(self):
        '''
        Prompts the user for a URL.
        '''
        return input("Enter the URL: ")
    def display_title(self, title):
        '''
        Displays the extracted title to the user.
        '''
        print(f"Title: {title}")