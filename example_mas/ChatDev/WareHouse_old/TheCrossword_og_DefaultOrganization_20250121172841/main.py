'''
Main entry point for the crossword puzzle application.
'''
from tkinter import Tk
from crossword_grid import CrosswordGrid
from clue_manager import ClueManager
from word_entry import WordEntry
class CrosswordApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Crossword Puzzle")
        self.clue_manager = ClueManager()
        self.crossword_grid = CrosswordGrid(self.root, self.clue_manager)
        self.word_entry = WordEntry(self.root, self.crossword_grid, self.clue_manager)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = CrosswordApp()
    app.run()