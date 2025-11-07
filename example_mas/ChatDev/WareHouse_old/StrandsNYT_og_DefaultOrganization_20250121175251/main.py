'''
Main application file for the NYT Strands puzzle game.
'''
import tkinter as tk
from game_logic import GameLogic
from word_segment import WordSegment
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NYT Strands Puzzle")
        self.game_logic = GameLogic()
        self.selected_segments = []
        self.feedback_label = tk.Label(self.root)
        self.feedback_label.pack()
        self.start_game()
        self.root.mainloop()
    def start_game(self):
        self.segments = self.game_logic.load_segments()
        self.create_segment_buttons()
    def create_segment_buttons(self):
        for segment in self.segments:
            button = tk.Button(self.root, text=segment.get_text(), command=lambda s=segment: self.select_segment(s))
            button.pack()
    def select_segment(self, segment):
        self.selected_segments.append(segment)
        self.update_display()
        self.check_solution()  # Add this line to provide immediate feedback
    def update_display(self):
        # Update the display to show selected segments
        selected_text = " ".join([seg.get_text() for seg in self.selected_segments])
        print(f"Selected: {selected_text}")
    def check_solution(self):
        if self.game_logic.validate_solution(self.selected_segments):
            self.feedback_label.config(text="Correct!", fg="green")
            self.selected_segments.clear()  # Clear the selected segments after a correct solution
        else:
            self.feedback_label.config(text="Try again.", fg="red")
if __name__ == "__main__":
    try:
        app = MainApp()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Please ensure you have a display available.")
        print(e)