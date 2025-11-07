'''
Main application file for the NYT Strands puzzle game.
'''
import tkinter as tk
from word_segment import WordSegment
from game_logic import GameLogic
# Removed playsound import due to missing module
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NYT Strands Puzzle")
        self.game_logic = GameLogic(["hello", "world", "python", "programming"])
        self.segments = []
        self.selected_segments = []
        self.setup_ui()
    def setup_ui(self):
        self.start_game()
        self.message_label = tk.Label(self.root, text="")
        self.message_label.pack()
    def start_game(self):
        # Example word segments
        words = ["hel", "lo", "wor", "ld", "py", "thon", "pro", "gram", "ming"]
        for i, word in enumerate(words):
            segment = WordSegment(self.root, word, i, self.on_segment_click)
            self.segments.append(segment)
    def on_segment_click(self, segment):
        if segment not in self.selected_segments:
            self.selected_segments.append(segment)
            segment.highlight()
            self.display_message(f"Selected: {segment.text}")
        else:
            self.selected_segments.remove(segment)
            segment.unhighlight()
            self.display_message(f"Deselected: {segment.text}")
        self.check_solution()
    def check_solution(self):
        selected_text = ''.join([seg.text for seg in self.selected_segments])
        if self.game_logic.validate(selected_text):
            self.display_message("Correct!")
            for segment in self.selected_segments:
                segment.button.config(bg='green')  # Change color to indicate success
            # Removed playsound due to missing module
        else:
            self.display_message("Try again.")
    def display_message(self, message):
        self.message_label.config(text=message)
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError:
        print("Error: Unable to initialize Tkinter. Ensure you have a display environment.")