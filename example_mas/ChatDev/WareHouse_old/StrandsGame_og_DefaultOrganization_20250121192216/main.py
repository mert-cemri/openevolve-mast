'''
Main file for the Strands game application. Handles the GUI and game logic.
'''
import tkinter as tk
from strand import Strand
from validator import StrandsValidator
class StrandsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Strands Game")
        # Initialize strands and validator
        self.strands = [Strand("hel"), Strand("lo"), Strand("wor"), Strand("ld")]
        self.validator = StrandsValidator(["hello", "world"])
        self.selected_strands = []
        # Create GUI components
        self.create_widgets()
    def create_widgets(self):
        self.strand_buttons = []
        for strand in self.strands:
            button = tk.Button(self.master, text=strand.get_text(), font=("Arial", 16),
                               command=lambda s=strand: self.select_strand(s))
            button.pack(side=tk.LEFT, padx=5)
            self.strand_buttons.append(button)
        self.check_button = tk.Button(self.master, text="Check", command=self.check_solution)
        self.check_button.pack(side=tk.LEFT, padx=5)
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game)
        self.reset_button.pack(side=tk.LEFT, padx=5)
        self.result_label = tk.Label(self.master, text="", font=("Arial", 16))
        self.result_label.pack(side=tk.LEFT, padx=5)
    def select_strand(self, strand):
        self.selected_strands.append(strand.get_text())
        self.update_selected_display()
    def update_selected_display(self):
        combined_text = "".join(self.selected_strands)
        self.result_label.config(text=combined_text, fg="black")
    def check_solution(self):
        combined_text = "".join(self.selected_strands)
        if self.validator.is_valid(combined_text):
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text="Try Again!", fg="red")
    def reset_game(self):
        self.selected_strands = []
        self.result_label.config(text="", fg="black")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        game = StrandsGame(root)
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Ensure you have a display environment set up.")
        print(e)