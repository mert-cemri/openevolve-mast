'''
Main application file for the professional law quiz application using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    def __init__(self, question_text, options, correct_index):
        self.question_text = question_text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Law Quiz")
        # Define the question
        self.question = Question(
            "A teachers union, a nongovernmental entity, seeks to picket the local city school board for its decision to require higher certification for instructors who wish to teach in the gifted and talented classes in elementary school. After a few days of picketing, the school board seeks a temporary injunction in the state court to restrain further picketing of the school board. The school board insists that the teachers union has violated Section 101 of the city's picketing ordinance. Section 101 reads as follows:\"Section 101. No picketing shall be permitted inside of, or on any sidewalk or street immediately adjacent or contiguous to public elementary and secondary schools without express permission of the mayor. Applications for such permission shall be filed at least three days before such picketing is intended to begin and shall state the purpose, place, and time of the proposed picketing. \"The court will most likely",
            [
                "grant relief, because the teachers union failed to follow the procedure outlined in the ordinance.",
                "grant relief, because the ordinance is constitutional.",
                "deny relief, because the picketing ordinance was unconstitutional on its face.",
                "deny relief, because the ordinance does not provide procedural due process."
            ],
            2
        )
        self.selected_option = tk.IntVar()
        self.display_question()
    def display_question(self):
        question_label = tk.Label(self.root, text=self.question.question_text, wraplength=400, justify="left")
        question_label.pack(pady=10)
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=idx)
            radio_button.pack(anchor="w")
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        selected_index = self.selected_option.get()
        if selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (2).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (2).")
if __name__ == "__main__":
    # Check if the DISPLAY environment variable is set
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Please ensure you are running this in an environment with GUI support.")
    else:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()