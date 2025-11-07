'''
QR code generation GUI class.
'''
import tkinter as tk
from qrcode import QRCode
class QRCodeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('QR Code Generator')
        self.text_label = tk.Label(self.master, text='Enter text:')
        self.text_label.pack()
        self.text_entry = tk.Entry(self.master)
        self.text_entry.pack()
        self.generate_button = tk.Button(self.master, text='Generate', command=self.generate_qr)
        self.generate_button.pack()
        self.qr_label = tk.Label(self.master, text='QR Code:')
        self.qr_label.pack()
        self.qr_canvas = tk.Canvas(self.master, width=200, height=200)
        self.qr_canvas.pack()
    def generate_qr(self):
        text = self.text_entry.get()
        qr = QRCode(text)
        qr.show()
        self.qr_canvas.create_image(100, 100, image=qr.image)