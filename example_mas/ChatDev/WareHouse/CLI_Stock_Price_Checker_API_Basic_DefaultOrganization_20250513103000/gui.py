'''
Provides a graphical user interface for the stock price checker application.
'''
import tkinter as tk
from tkinter import messagebox
from stock_price_checker import StockPriceChecker
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Stock Price Checker")
        self.create_widgets()
    def create_widgets(self):
        self.ticker_label = tk.Label(self.root, text="Enter Ticker Symbol:")
        self.ticker_label.pack()
        self.ticker_entry = tk.Entry(self.root)
        self.ticker_entry.pack()
        self.check_button = tk.Button(self.root, text="Check Price", command=self.check_price)
        self.check_button.pack()
    def check_price(self):
        ticker = self.ticker_entry.get()
        checker = StockPriceChecker()
        try:
            price, change = checker.get_current_price(ticker)
            messagebox.showinfo("Stock Price", f"Current price of {ticker}: ${price:.2f}\nChange: ${change:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def run(self):
        self.root.mainloop()