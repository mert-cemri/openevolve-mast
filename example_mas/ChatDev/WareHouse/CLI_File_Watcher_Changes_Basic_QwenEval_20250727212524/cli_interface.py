'''
CLIInterface class to handle command-line interactions.
Accepts user input and starts the file watcher.
'''
import sys
from filewatcher import FileWatcher
class CLIInterface:
    def __init__(self, path):
        self.path = path
    def run(self):
        '''
        Main method to run the CLI interface.
        Starts the file watcher.
        '''
        watcher = FileWatcher(self.path, self.print_notification)
        watcher.start()
    def print_notification(self, message):
        '''
        Callback method to print notifications to the console.
        :param message: The notification message to print.
        '''
        print(message)