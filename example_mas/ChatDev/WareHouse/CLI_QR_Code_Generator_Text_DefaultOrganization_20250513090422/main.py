'''
Main application file for the QR code generator CLI tool.
'''
import argparse
from qr_utils import generate_qr_code, display_ascii_art, save_qr_image
def main():
    parser = argparse.ArgumentParser(description="Generate a QR code from a text string or URL.")
    parser.add_argument("text", help="The text or URL to encode in the QR code.")
    parser.add_argument("--ascii", action="store_true", help="Output the QR code as ASCII art in the terminal.")
    parser.add_argument("--save", metavar="FILE", help="Save the QR code as an image file.")
    args = parser.parse_args()
    qr = generate_qr_code(args.text)
    if args.ascii:
        display_ascii_art(qr)
    if args.save:
        qr_image = qr.make_image(fill_color="black", back_color="white")
        save_qr_image(qr_image, args.save)
        print(f"QR code saved as {args.save}")
if __name__ == "__main__":
    main()