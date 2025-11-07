'''
Defines the WordSegment class for the NYT Strands puzzle game.
'''
import tkinter as tk
class WordSegment:
    def __init__(self, root, text, position, click_callback):
        '''
        Initialize a WordSegment instance.
        '''
        self.text = text
        self.position = position
        self.click_callback = click_callback
        self.button = tk.Button(root, text=text, command=lambda: click_callback(self))
        self.button.pack(side=tk.LEFT, padx=5, pady=5)
    def connect(self, other_segment):
        '''
        Logic to visually connect segments (if needed).
        '''
        # Currently, this method is a placeholder for future visual connection logic.
        pass
    def highlight(self):
        '''
        Highlight the segment to indicate selection.
        '''
        self.button.config(bg='lightblue')
    def unhighlight(self):
        '''
        Remove highlight from the segment to indicate deselection.
        '''
        self.button.config(bg='SystemButtonFace')