'''
QR code generation class.
'''
import qrcode
class QRCode:
    def __init__(self, text):
        self.text = text
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        self.qr.add_data(self.text)
        self.qr.make(fit=True)
    def save(self, filename):
        self.qr.save(filename)
    def show(self):
        self.qr.show()