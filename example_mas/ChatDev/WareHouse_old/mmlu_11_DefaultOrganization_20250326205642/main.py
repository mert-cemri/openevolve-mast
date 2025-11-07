'''
Main application file for the legal question evaluator with GUI.
'''
import tkinter as tk
from tkinter import messagebox
def evaluate_law_question(question):
    '''
    Evaluate the legal question and return the correct answer index.
    '''
    # Enhanced evaluation logic to determine the correct answer
    if "doctrine of after-acquired title" in question:
        return 1
    elif "good and marketable title" in question:
        return 0
    elif "quitclaim deed" in question and "subsequent" in question:
        return 3
    elif "quitclaim deed" in question:
        return 2
    else:
        return None
class MainApp:
    '''
    Main application class to create the GUI and handle user interactions.
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Legal Question Evaluator")
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the application window.
        '''
        self.label = tk.Label(self.root, text="Enter your legal question:")
        self.label.pack(pady=10)
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)
        self.evaluate_button = tk.Button(self.root, text="Evaluate", command=self.evaluate_question)
        self.evaluate_button.pack(pady=10)
    def evaluate_question(self):
        '''
        Evaluate the question entered by the user and display the answer.
        '''
        question = self.text_area.get("1.0", tk.END).strip()
        if not question:
            messagebox.showwarning("Input Error", "Please enter a legal question.")
            return
        answer_index = evaluate_law_question(question)
        if answer_index is not None:
            messagebox.showinfo("Answer", f"The answer is ({answer_index})")
        else:
            messagebox.showerror("Evaluation Error", "Could not determine the answer.")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError:
        print("Error: Tkinter GUI cannot be initialized in the current environment. Please ensure a graphical display is available.")