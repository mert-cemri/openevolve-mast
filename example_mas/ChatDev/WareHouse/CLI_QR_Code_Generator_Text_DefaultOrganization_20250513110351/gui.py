'''
GUI setup for the QR code generator application using tkinter.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from qr_generator import QRGenerator
def create_gui() -> None:
    def generate_qr():
        text = entry.get()
        if not text:
            messagebox.showerror("Error", "Please enter text or URL.")
            return
        qr_gen = QRGenerator()
        qr = qr_gen.generate_qr_code(text)
        if save_var.get():
            filename = filedialog.asksaveasfilename(defaultextension=".png",
                                                    filetypes=[("PNG files", "*.png")])
            if filename:
                qr_gen.save_as_image(qr, filename)
                messagebox.showinfo("Success", f"QR code saved as {filename}")
        if ascii_var.get():
            ascii_art = qr_gen.display_as_ascii(qr)
            ascii_window = tk.Toplevel(root)
            ascii_window.title("QR Code ASCII Art")
            text_widget = tk.Text(ascii_window, wrap='none')
            text_widget.insert(tk.END, ascii_art)
            text_widget.pack(expand=True, fill='both')
    root = tk.Tk()
    root.title("QR Code Generator")
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)
    tk.Label(frame, text="Enter Text or URL:").grid(row=0, column=0, sticky='w')
    entry = tk.Entry(frame, width=50)
    entry.grid(row=0, column=1, padx=5, pady=5)
    save_var = tk.BooleanVar()
    ascii_var = tk.BooleanVar()
    tk.Checkbutton(frame, text="Save as Image", variable=save_var).grid(row=1, column=0, sticky='w')
    tk.Checkbutton(frame, text="Display as ASCII", variable=ascii_var).grid(row=1, column=1, sticky='w')
    tk.Button(frame, text="Generate QR Code", command=generate_qr).grid(row=2, columnspan=2, pady=10)
    root.mainloop()