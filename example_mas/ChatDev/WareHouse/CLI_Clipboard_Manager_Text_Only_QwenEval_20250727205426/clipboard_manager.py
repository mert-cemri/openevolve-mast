'''
Clipboard manager class to handle clipboard operations.
'''
class ClipboardManager:
    def __init__(self):
        self.clipboard = ""
        self.history = []
    def copy(self, text):
        '''
        Copy text to the clipboard and add it to the history if it's not a duplicate of the last entry.
        '''
        self.clipboard = text
        if not self.history or self.history[-1] != text:
            self.history.append(text)
    def paste(self):
        '''
        Return the current text in the clipboard or an appropriate message if the clipboard is empty.
        '''
        if not self.clipboard:
            return "Clipboard is empty. Nothing to paste."
        return self.clipboard
    def get_history(self):
        '''
        Return the history of copied texts.
        '''
        return self.history
    def clear(self, part="all"):
        '''
        Clear the clipboard and optionally the history.
        :param part: "all" to clear both clipboard and history, "clipboard" to clear only the clipboard, "history" to clear only the history.
        '''
        if part == "all" or part == "clipboard":
            self.clipboard = ""
        if part == "all" or part == "history":
            self.history = []
    def show_version(self):
        '''
        Display the version of the clipboard manager.
        '''
        return "CLI Clipboard Manager version 1.0"