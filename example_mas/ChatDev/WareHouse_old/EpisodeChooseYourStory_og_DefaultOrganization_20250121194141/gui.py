'''
GUI module to handle the graphical user interface using Tkinter.
'''
import tkinter as tk
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Interactive Storytelling Game")
        self.text_area = tk.Text(self.root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        self.choice_buttons = []
        self.game = None
    def create_main_window(self):
        self.root.mainloop()
    def display_scene(self, scene):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, scene.narrative)
        for button in self.choice_buttons:
            button.destroy()
        self.choice_buttons = []
        for choice_id, choice in scene.get_choices().items():
            button = tk.Button(self.root, text=choice.description, command=lambda cid=choice_id: self.make_choice(cid))
            button.pack(fill=tk.X)
            self.choice_buttons.append(button)
    def make_choice(self, choice_id):
        if self.game:
            self.game.make_choice(choice_id)
    def display_error(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        tk.Label(error_window, text=message).pack()
        tk.Button(error_window, text="OK", command=error_window.destroy).pack()