'''
Handles the graphical user interface interactions using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from rss_fetcher import RSSFetcher
from rss_parser import RSSParser
class GUIInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RSS Feed Reader")
        self.root.geometry("400x300")
        self.url_label = tk.Label(self.root, text="Enter RSS Feed URL:")
        self.url_label.pack(pady=10)
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack(pady=5)
        self.fetch_button = tk.Button(self.root, text="Fetch Articles", command=self.fetch_articles)
        self.fetch_button.pack(pady=10)
        self.articles_text = tk.Text(self.root, width=50, height=10)
        self.articles_text.pack(pady=5)
    def fetch_articles(self):
        url = self.url_entry.get()
        fetcher = RSSFetcher()
        parser = RSSParser()
        try:
            content = fetcher.fetch(url)
            articles = parser.parse(content)
            self.articles_text.delete(1.0, tk.END)
            for title, link in articles:
                self.articles_text.insert(tk.END, f"Title: {title}\nLink: {link}\n\n")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    def run(self):
        self.root.mainloop()