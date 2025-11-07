'''
Main application file for the professional law multiple-choice question GUI.
'''
import tkinter as tk
from tkinter import messagebox
class Question:
    '''
    A class to represent a multiple-choice question.
    '''
    def __init__(self, question_text, options, correct_index):
        self.question_text = question_text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    '''
    A class to create the main application window for the quiz.
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Law Quiz")
        # Define the question
        self.question = Question(
            "In a criminal prosecution the government must prove that the defendant affixed a rubber-stamp containing his signature to certain fraudulent letters mailed to the victim. The defendant denied that he stamped the letters. There were no witnesses to the defendant stamping the letters. The prosecution attempted to present a co-worker to testify that defendant maintained sole control of the stamp and used it once daily at 3 p.m. to sign all outgoing letters, and then immediately returned it to his safe. The co-worker would testify that he saw the defendant using the stamp in that habitual manner over a period of many years. The defense objected because this did not prove that the defendant's practice was followed on the dates in question. Under the Federal Rules of Evidence, what will the court rule?",
            [
                "The testimony is inadmissible because evidence of habit is not admissible in a criminal case under the Federal Rules of Evidence.",
                "The testimony is inadmissible because evidence of prior habit will only distract the jury from deciding whether the defendant actually acted that way on the specified dates.",
                "The testimony is admissible because it proves that the defendant was the only person who could have used the stamp.",
                "The testimony is admissible because habit and routine practice are admissible under the Federal Rules of Evidence."
            ],
            3
        )
        self.selected_option = tk.IntVar()
        # Display the question
        self.display_question()
    def display_question(self):
        '''
        Displays the question and options in the GUI.
        '''
        question_label = tk.Label(self.root, text=self.question.question_text, wraplength=400, justify="left")
        question_label.pack(pady=10)
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=idx)
            radio_button.pack(anchor="w")
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Checks if the selected answer is correct and displays a message box with the result.
        '''
        selected_index = self.selected_option.get()
        if selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (3).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (3).")
if __name__ == "__main__":
    import os
    import subprocess
    if os.environ.get('DISPLAY','') == '':
        # Start Xvfb if not already running
        subprocess.Popen(['Xvfb', ':99', '-screen', '0', '1024x768x16'])
        os.environ.__setitem__('DISPLAY', ':99')
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()