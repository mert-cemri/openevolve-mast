'''
Handles the graphical user interface interactions for the Calendar tool.
'''
import tkinter as tk
from tkinter import messagebox
import calendar
from calendar_utils import CalendarUtils
class CalendarGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calendar Tool")
        self.root.geometry("400x300")
        self.month_label = tk.Label(self.root, text="Month (1-12 or name):")
        self.month_label.pack(pady=5)
        self.month_entry = tk.Entry(self.root)
        self.month_entry.pack(pady=5)
        self.year_label = tk.Label(self.root, text="Year:")
        self.year_label.pack(pady=5)
        self.year_entry = tk.Entry(self.root)
        self.year_entry.pack(pady=5)
        self.display_button = tk.Button(self.root, text="Display Calendar", command=self.display_calendar)
        self.display_button.pack(pady=20)
    def run(self):
        self.root.mainloop()
    def display_calendar(self):
        month = self.month_entry.get()
        year = self.year_entry.get()
        try:
            year = int(year)
            if month.isdigit():
                month = int(month)
            else:
                month = CalendarUtils.month_name_to_number(month)
            cal = calendar.month(year, month)
            messagebox.showinfo("Calendar", cal)
        except ValueError as e:
            messagebox.showerror("Error", str(e))