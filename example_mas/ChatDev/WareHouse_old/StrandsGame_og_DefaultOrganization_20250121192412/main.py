'''
Main file to run the Strands game application.
'''
import tkinter as tk
from gui import StrandsGUI
def main():
    root = tk.Tk()
    root.title("Strands Game")
    app = StrandsGUI(master=root)
    app.mainloop()
if __name__ == "__main__":
    main()