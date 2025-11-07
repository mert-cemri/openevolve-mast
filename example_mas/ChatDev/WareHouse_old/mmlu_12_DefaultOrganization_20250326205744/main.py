'''
Main application file for the moral scenario evaluator GUI.
'''
import tkinter as tk
from evaluator import ScenarioEvaluator
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moral Scenario Evaluator")
        self.label1 = tk.Label(root, text="Scenario 1:")
        self.label1.pack()
        self.scenario1_entry = tk.Entry(root, width=50)
        self.scenario1_entry.pack()
        self.label2 = tk.Label(root, text="Scenario 2:")
        self.label2.pack()
        self.scenario2_entry = tk.Entry(root, width=50)
        self.scenario2_entry.pack()
        self.evaluate_button = tk.Button(root, text="Evaluate", command=self.evaluate_scenarios)
        self.evaluate_button.pack()
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
    def evaluate_scenarios(self):
        scenario1 = self.scenario1_entry.get()
        scenario2 = self.scenario2_entry.get()
        evaluator = ScenarioEvaluator()
        result = evaluator.evaluate(scenario1, scenario2)
        self.display_result(result)
    def display_result(self, result):
        self.result_label.config(text=f"The answer is ({result})")
def run_gui():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
def run_non_gui(scenario1, scenario2):
    evaluator = ScenarioEvaluator()
    result = evaluator.evaluate(scenario1, scenario2)
    print(f"The answer is ({result})")
if __name__ == "__main__":
    import os
    if os.environ.get('DISPLAY'):
        run_gui()
    else:
        # Example scenarios for non-GUI mode
        scenario1 = "I built a snowman inside the beautiful home."
        scenario2 = "I popped the balloon and gave it back to the child."
        run_non_gui(scenario1, scenario2)