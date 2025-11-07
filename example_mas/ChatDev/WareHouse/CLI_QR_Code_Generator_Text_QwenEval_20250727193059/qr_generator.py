'''
Module for generating QR codes.
Includes functions to generate QR codes, save them as image files, and convert them to ASCII art.
'''
import qrcode
from PIL import Image
def generate_qr_code(data):
    '''
    Generate a QR code from the given data.
    :param data: The text string or URL to encode in the QR code.
    :return: A PIL Image object containing the QR code.
    '''
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img
def save_qr_code(qr_code, filename):
    '''
    Save the QR code image to a file.
    :param qr_code: A PIL Image object containing the QR code.
    :param filename: The filename to save the QR code image.
    '''
    qr_code.save(filename)
def qr_to_ascii(qr_code):
    '''
    Convert the QR code image to ASCII art.
    :param qr_code: A PIL Image object containing the QR code.
    :return: A string containing the ASCII art representation of the QR code.
    '''
    # Convert image to grayscale
    qr_code = qr_code.convert('L')
    # Resize image to fit within a reasonable width for ASCII art
    qr_code = qr_code.resize((qr_code.width // 10, qr_code.height // 10))
    # Define ASCII characters to use for different shades of gray
    ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    # Convert image to ASCII art
    ascii_art = ""
    pixels = qr_code.getdata()
    for pixel in pixels:
        ascii_art += ascii_chars[pixel * (len(ascii_chars) - 1) // 255]
    # Split ASCII art into lines
    width = qr_code.width
    ascii_art = [ascii_art[i:i + width] for i in range(0, len(ascii_art), width)]
    return "\n".join(ascii_art)