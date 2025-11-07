'''
Main application file for the professional law quiz using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    '''
    A class to represent a multiple choice question.
    '''
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    '''
    Main application class to handle the quiz logic and UI.
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Law Quiz")
        # Define the question
        self.question = Question(
            text="A city imposes a municipal excise tax of $200 per year on commercial artists' studios in that city. "
                 "It also imposes an excise tax of $100 per year on every itinerant commercial figure drawer for the "
                 "privilege of using the streets and sidewalks. A credit is allowed against this latter tax for any "
                 "excise tax paid to the city by the drawer or his employer in respect to the maintenance of an artist's "
                 "studio in the city. A gallery, located in a neighboring state, has been sending two itinerant artists "
                 "into the city. Their practice is to draw a picture of a pedestrian, ask him to order a finished painting, "
                 "and collect a payment of $2.00. The drawing is sent to a studio, which frames it and mails the framed "
                 "painting to the customer. The neighboring state does not impose a tax on artists' studios. The gallery "
                 "challenges the constitutionality of the $100 per year excise tax that is imposed upon its itinerant artists "
                 "in the city. The court will most likely declare this tax",
            options=[
                "constitutional, as a valid ad valorem tax on interstate commerce.",
                "constitutional, since the tax was levied not on the commercial art business as a whole but on the local activity of drawing pictures.",
                "unconstitutional, since a state or municipality may not impose a license tax on orders for goods or services to be performed in another state.",
                "unconstitutional, as a discriminatory privilege tax."
            ],
            correct_index=1
        )
        self.selected_option = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and display the quiz widgets.
        '''
        # Display the question
        question_label = tk.Label(self.root, text=self.question.text, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Display the options as radio buttons
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=idx)
            radio_button.pack(anchor="w")
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check the selected answer and display the result.
        '''
        selected_index = self.selected_option.get()
        if selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", "Incorrect. Try again.")
if __name__ == "__main__":
    # Check if the DISPLAY environment variable is set
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Please ensure you are running this on a system with a graphical interface or use X11 forwarding.")
    else:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()