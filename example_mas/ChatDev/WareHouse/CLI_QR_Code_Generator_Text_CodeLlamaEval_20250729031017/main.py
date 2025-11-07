'''
Entry point for the CLI tool.
'''
import argparse
from qrcode import QRCode
def main():
    parser = argparse.ArgumentParser(description='Generate a QR code from a given text string or URL.')
    parser.add_argument('text', help='Text string or URL to generate QR code from.')
    parser.add_argument('-o', '--output', help='Output file name.')
    args = parser.parse_args()
    qr = QRCode(args.text)
    if args.output:
        qr.save(args.output)
    else:
        qr.show()
if __name__ == '__main__':
    main()