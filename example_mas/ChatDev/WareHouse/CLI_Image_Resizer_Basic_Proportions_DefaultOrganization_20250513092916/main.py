'''
This script provides a command-line interface (CLI) for resizing images while maintaining aspect ratio using the Pillow library.
'''
import argparse
from PIL import Image
def resize_image(input_path, output_path, target_width=None, target_height=None):
    '''
    Resizes an image to the target width or height while maintaining aspect ratio.
    Parameters:
    - input_path: Path to the input image file.
    - output_path: Path to save the resized image.
    - target_width: Desired width of the resized image.
    - target_height: Desired height of the resized image.
    '''
    with Image.open(input_path) as img:
        original_width, original_height = img.size
        if target_width and not target_height:
            target_height = int((target_width / original_width) * original_height)
        elif target_height and not target_width:
            target_width = int((target_height / original_height) * original_width)
        img = img.resize((target_width, target_height), Image.ANTIALIAS)
        img.save(output_path)
def main():
    '''
    Parses command-line arguments and calls the resize_image function.
    '''
    parser = argparse.ArgumentParser(description='Resize an image while maintaining aspect ratio.')
    parser.add_argument('input_path', type=str, help='Path to the input image file.')
    parser.add_argument('output_path', type=str, help='Path to save the resized image.')
    parser.add_argument('--width', type=int, help='Target width of the resized image.')
    parser.add_argument('--height', type=int, help='Target height of the resized image.')
    args = parser.parse_args()
    if not args.width and not args.height:
        print("Error: Please specify either target width or height.")
        return
    resize_image(args.input_path, args.output_path, args.width, args.height)
if __name__ == "__main__":
    main()