'''
Handles the graphical user interface interactions.
'''
import tkinter as tk
from scraper import WebScraper
class GUIInterface:
    def create_window(self):
        '''
        Creates the main window.
        '''
        self.window = tk.Tk()
        self.window.title("Web Scraper")
        self.window.geometry("400x200")
        self.label = tk.Label(self.window, text="Enter URL:")
        self.label.pack(pady=10)
        self.url_entry = tk.Entry(self.window, width=50)
        self.url_entry.pack(pady=5)
        self.scrape_button = tk.Button(self.window, text="Scrape", command=self.scrape_title)
        self.scrape_button.pack(pady=10)
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack(pady=10)
        self.window.mainloop()
    def scrape_title(self):
        '''
        Retrieves the URL input from the user and displays the extracted title.
        '''
        url = self.url_entry.get()
        scraper = WebScraper()
        try:
            html_content = scraper.fetch_url(url)
            title = scraper.extract_title(html_content)
            self.result_label.config(text=f"Title: {title}")
        except requests.exceptions.RequestException as e:
            self.result_label.config(text=f"Error fetching URL: {e}")