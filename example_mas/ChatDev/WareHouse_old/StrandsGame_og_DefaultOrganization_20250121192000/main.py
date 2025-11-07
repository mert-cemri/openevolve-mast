'''
Main application file for the Strands word-segmentation puzzle. Initializes the GUI and manages user interactions.
'''
import tkinter as tk
from puzzle import StrandsPuzzle
class StrandsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Strands Puzzle")
        self.puzzle = StrandsPuzzle()
        self.selected_strands = []
        self.create_widgets()
    def create_widgets(self):
        # Create and place widgets
        self.instructions_label = tk.Label(self.root, text="Combine the strands to form meaningful words or phrases.")
        self.instructions_label.pack()
        self.strands_frame = tk.Frame(self.root)
        self.strands_frame.pack()
        self.strands_buttons = []
        for strand in self.puzzle.get_strands():
            button = tk.Button(self.strands_frame, text=strand, command=lambda s=strand: self.select_strand(s))
            button.pack(side="left", padx=5, pady=5)
            self.strands_buttons.append(button)
        self.selected_label = tk.Label(self.root, text="Selected: ")
        self.selected_label.pack(pady=10)
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_solution)
        self.submit_button.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
    def select_strand(self, strand):
        self.selected_strands.append(strand)
        self.update_selected_label()
    def update_selected_label(self):
        self.selected_label.config(text="Selected: " + " ".join(self.selected_strands))
    def check_solution(self):
        user_input = "".join(self.selected_strands)
        if self.puzzle.check_solution(user_input):
            self.result_label.config(text="Correct! Puzzle Solved!", fg="green")
        else:
            self.result_label.config(text="Incorrect. Try Again.", fg="red")
        self.selected_strands.clear()
        self.update_selected_label()
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = StrandsApp(root)
        root.mainloop()
    except tk.TclError:
        print("Error: Unable to initialize the GUI. Please ensure you are running this in a graphical environment.")