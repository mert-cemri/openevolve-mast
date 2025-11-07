'''
ClipboardManager class to manage clipboard operations.
'''
class ClipboardManager:
    def __init__(self):
        '''Initialize the clipboard manager with an empty history.'''
        self.history = []
    def copy(self, text):
        '''Copy text to the clipboard.'''
        self.history.append(text)
        print(f'Text copied: "{text}"')
    def paste(self):
        '''Paste the most recently copied text.'''
        if self.history:
            print(f'Pasted text: "{self.history[-1]}"')
            return self.history[-1]
        else:
            print('Clipboard is empty.')
            return None
    def show_history(self):
        '''Return the clipboard history.'''
        if self.history:
            print('Clipboard History:')
            for index, text in enumerate(self.history, start=1):
                print(f'{index}: {text}')
        else:
            print('Clipboard history is empty.')