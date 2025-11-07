'''
QR code generation CLI class.
'''
import argparse
from qrcode import QRCode
class QRCodeCLI:
    def __init__(self, text):
        self.text = text
        self.qr = QRCode(self.text)
    def save(self, filename):
        self.qr.save(filename)
    def show(self):
        self.qr.show()