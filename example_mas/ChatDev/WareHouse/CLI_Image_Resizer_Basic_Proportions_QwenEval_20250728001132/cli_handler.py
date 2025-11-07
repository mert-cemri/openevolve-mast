'''
Handles command-line arguments for the Image Resizer CLI application.
'''
import argparse
from image_resizer import ImageResizer
class CLIHandler:
    def __init__(self, args):
        self.args = args
    def run(self):
        parser = argparse.ArgumentParser(description="Resize an image while maintaining aspect ratio.")
        parser.add_argument("input_path", help="Path to the input image file.")
        parser.add_argument("output_path", help="Path to the output image file.")
        parser.add_argument("--width", type=int, help="Target width of the image.")
        parser.add_argument("--height", type=int, help="Target height of the image.")
        args = parser.parse_args(self.args[1:])
        try:
            if args.width is None and args.height is None:
                raise ValueError("Either --width or --height must be specified.")
            resizer = ImageResizer(args.input_path, args.output_path, args.width, args.height)
            resizer.resize_image()
            print(f"Image resized and saved to {resizer.get_output_path()}")
        except ValueError as e:
            print(f"Error: {str(e)}")