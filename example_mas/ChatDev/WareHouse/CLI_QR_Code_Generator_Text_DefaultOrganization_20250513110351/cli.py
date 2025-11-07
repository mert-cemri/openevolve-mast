'''
CLI class for handling command-line interface operations.
'''
import argparse
from qr_generator import QRGenerator
class CLI:
    def parse_arguments(self) -> argparse.Namespace:
        parser = argparse.ArgumentParser(description="Generate a QR code from text or URL.")
        parser.add_argument("text", help="Text or URL to encode in the QR code.")
        parser.add_argument("-o", "--output", help="Output file to save the QR code image.")
        parser.add_argument("--ascii", action="store_true", help="Display QR code as ASCII art.")
        parser.add_argument("--gui", action="store_true", help="Launch the GUI application.")
        return parser.parse_args()
    def execute(self) -> None:
        args = self.parse_arguments()
        qr_gen = QRGenerator()
        qr = qr_gen.generate_qr_code(args.text)
        if args.output:
            qr_gen.save_as_image(qr, args.output)
            print(f"QR code saved as {args.output}")
        if args.ascii:
            ascii_art = qr_gen.display_as_ascii(qr)
            print(ascii_art)