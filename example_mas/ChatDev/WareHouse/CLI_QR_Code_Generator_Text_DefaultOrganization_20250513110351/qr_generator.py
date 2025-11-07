'''
QRGenerator class for generating and handling QR codes.
'''
import qrcode
from qrcode.image.pil import PilImage
class QRGenerator:
    def generate_qr_code(self, text: str) -> qrcode.QRCode:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        return qr
    def save_as_image(self, qr: qrcode.QRCode, filename: str) -> None:
        img = qr.make_image(fill='black', back_color='white')
        img.save(filename)
    def display_as_ascii(self, qr: qrcode.QRCode) -> str:
        qr.make()
        matrix = qr.modules
        ascii_art = ""
        for row in matrix:
            line = "".join(['██' if cell else '  ' for cell in row])
            ascii_art += line + "\n"
        return ascii_art