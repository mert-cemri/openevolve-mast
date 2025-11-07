'''
This file contains the implementation of a GUI-based quiz application using tkinter.
The application presents a multiple-choice question about professional law and checks the user's answer.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    def __init__(self, prompt, choices, correct_index):
        self.prompt = prompt
        self.choices = choices
        self.correct_index = correct_index
class QuizApp:
    def __init__(self, root, question):
        self.root = root
        self.question = question
        self.selected_answer = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        # Display the question
        question_label = tk.Label(self.root, text=self.question.prompt, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Display the choices as radio buttons
        for index, choice in enumerate(self.question.choices):
            radio_button = tk.Radiobutton(self.root, text=choice, variable=self.selected_answer, value=index)
            radio_button.pack(anchor="w")
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        selected_index = self.selected_answer.get()
        if selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", "Incorrect. Try again.")
def main():
    # Check if the script is running in an environment without a display
    if os.environ.get('DISPLAY', '') == '':
        print('No display found. Running in headless mode.')
        os.environ['DISPLAY'] = ':0'
    # Define the question and choices
    question_text = (
        "A city imposes a municipal excise tax of $200 per year on commercial artists' studios in that city. "
        "It also imposes an excise tax of $100 per year on every itinerant commercial figure drawer for the privilege "
        "of using the streets and sidewalks. A credit is allowed against this latter tax for any excise tax paid to the "
        "city by the drawer or his employer in respect to the maintenance of an artist's studio in the city. A gallery, "
        "located in a neighboring state, has been sending two itinerant artists into the city. Their practice is to draw "
        "a picture of a pedestrian, ask him to order a finished painting, and collect a payment of $2.00. The drawing is "
        "sent to a studio, which frames it and mails the framed painting to the customer. The neighboring state does not "
        "impose a tax on artists' studios. The gallery challenges the constitutionality of the $100 per year excise tax "
        "that is imposed upon its itinerant artists in the city. The court will most likely declare this tax"
    )
    choices = [
        "constitutional, as a valid ad valorem tax on interstate commerce.",
        "constitutional, since the tax was levied not on the commercial art business as a whole but on the local activity of drawing pictures.",
        "unconstitutional, since a state or municipality may not impose a license tax on orders for goods or services to be performed in another state.",
        "unconstitutional, as a discriminatory privilege tax."
    ]
    correct_index = 1  # The correct answer is index 1
    # Create the main window
    root = tk.Tk()
    root.title("Professional Law Quiz")
    root.geometry("500x400")
    # Create the quiz app
    app = QuizApp(root, Question(question_text, choices, correct_index))
    # Start the main loop
    root.mainloop()
if __name__ == "__main__":
    main()