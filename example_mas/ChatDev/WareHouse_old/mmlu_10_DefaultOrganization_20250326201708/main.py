'''
Main application file for the professional law quiz GUI.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    def __init__(self, text, options, correct_index):
        '''
        Initialize a Question instance.
        :param text: The question text.
        :param options: A list of answer options.
        :param correct_index: The index of the correct answer in the options list.
        '''
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and components.
        :param root: The root window of the application.
        '''
        self.root = root
        self.root.title("Professional Law Quiz")
        self.question = load_question()
        self.selected_answer = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the main window.
        '''
        question_label = tk.Label(self.root, text=self.question.text, wraplength=400, justify="left")
        question_label.pack(pady=10)
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=idx)
            radio_button.pack(anchor="w")
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check if the selected answer is correct and display the result.
        '''
        if self.selected_answer.get() == self.question.correct_index:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", "Incorrect. Try again.")
def load_question():
    '''
    Load the question data.
    :return: A Question instance with the question text, options, and correct answer index.
    '''
    text = ("In a criminal prosecution the government must prove that the defendant affixed a rubber-stamp "
            "containing his signature to certain fraudulent letters mailed to the victim. The defendant denied "
            "that he stamped the letters. There were no witnesses to the defendant stamping the letters. The "
            "prosecution attempted to present a co-worker to testify that defendant maintained sole control of "
            "the stamp and used it once daily at 3 p.m. to sign all outgoing letters, and then immediately "
            "returned it to his safe. The co-worker would testify that he saw the defendant using the stamp in "
            "that habitual manner over a period of many years. The defense objected because this did not prove "
            "that the defendant's practice was followed on the dates in question. Under the Federal Rules of "
            "Evidence, what will the court rule?")
    options = [
        "The testimony is inadmissible because evidence of habit is not admissible in a criminal case under the Federal Rules of Evidence.",
        "The testimony is inadmissible because evidence of prior habit will only distract the jury from deciding whether the defendant actually acted that way on the specified dates.",
        "The testimony is admissible because it proves that the defendant was the only person who could have used the stamp.",
        "The testimony is admissible because habit and routine practice are admissible under the Federal Rules of Evidence."
    ]
    correct_index = 3
    return Question(text, options, correct_index)
if __name__ == "__main__":
    # Check if running in a non-GUI environment and set up a virtual display if necessary
    if os.environ.get('DISPLAY', '') == '':
        print('No display found. Ensure Xvfb is installed for virtual display.')
        try:
            from pyvirtualdisplay import Display
            display = Display(visible=0, size=(800, 600))
            display.start()
        except FileNotFoundError:
            print("Xvfb is not installed. Please install it to run the application in a headless environment.")
            exit(1)
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()