'''
QR code generation test script.
'''
import unittest
from qrcode import QRCode
class TestQRCode(unittest.TestCase):
    def test_generate_qr(self):
        text = 'Hello, World!'
        qr = QRCode(text)
        self.assertEqual(qr.text, text)
        self.assertEqual(qr.qr.version, 1)
        self.assertEqual(qr.qr.error_correction, qrcode.constants.ERROR_CORRECT_L)
        self.assertEqual(qr.qr.box_size, 10)
        self.assertEqual(qr.qr.border, 4)
        self.assertEqual(qr.qr.data, text)