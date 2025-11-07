'''
Utility functions for QR code generation, ASCII art conversion, and image saving.
'''
import qrcode
import qrcode.image.pil
def generate_qr_code(text):
    '''
    Generate a QR code from the given text or URL.
    '''
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    return qr  # Return the QRCode object instead of the image
def display_ascii_art(qr):
    '''
    Convert the QR code into ASCII art and display it in the terminal.
    '''
    qr_image = qr.make_image(fill_color="black", back_color="white").convert('1')  # Generate and convert to black and white
    ascii_art = ''
    for y in range(qr_image.size[1]):
        line = ''
        for x in range(qr_image.size[0]):
            line += '██' if qr_image.getpixel((x, y)) == 0 else '  '
        ascii_art += line + '\n'
    print(ascii_art)
def save_qr_image(qr_image, file_path):
    '''
    Save the generated QR code as an image file.
    '''
    qr_image.save(file_path)