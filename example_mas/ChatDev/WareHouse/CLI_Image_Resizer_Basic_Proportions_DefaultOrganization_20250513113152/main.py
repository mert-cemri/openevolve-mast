'''
Main entry point for the CLI Image Resizer application. Processes command-line arguments and resizes the image.
'''
import argparse
from PIL import Image
from image_utils import resize_image
def main():
    parser = argparse.ArgumentParser(description="Resize an image while maintaining aspect ratio.")
    parser.add_argument("image_path", type=str, help="Path to the input image file.")
    parser.add_argument("--width", type=int, help="Target width for the resized image.")
    parser.add_argument("--height", type=int, help="Target height for the resized image.")
    parser.add_argument("output_path", type=str, help="Path to save the resized image.")
    args = parser.parse_args()
    try:
        original_image = Image.open(args.image_path)
        resized_image = resize_image(original_image, args.width, args.height)
        resized_image.save(args.output_path)
        print(f"Image saved to {args.output_path}")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()