'''
Main script to run the QR code generator CLI tool.
Handles command-line arguments and invokes the appropriate functions.
'''
import argparse
from qr_generator import generate_qr_code, save_qr_code, qr_to_ascii
def main():
    parser = argparse.ArgumentParser(description='Generate a QR code from a given text string or URL.')
    parser.add_argument('data', type=str, help='The text string or URL to encode in the QR code.')
    parser.add_argument('--output', type=str, help='The filename to save the QR code image. If not provided, the QR code will be displayed as ASCII art in the terminal.')
    args = parser.parse_args()
    qr_code = generate_qr_code(args.data)
    if args.output:
        save_qr_code(qr_code, args.output)
        print(f'QR code saved to {args.output}')
    else:
        ascii_art = qr_to_ascii(qr_code)
        print(ascii_art)
if __name__ == '__main__':
    main()