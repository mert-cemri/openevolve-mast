'''
Handles the resizing of images while maintaining aspect ratio.
'''
from PIL import Image
import os
class ImageResizer:
    def __init__(self, input_path, output_path, target_width=None, target_height=None):
        self.input_path = input_path
        self.output_path = output_path
        self.target_width = target_width
        self.target_height = target_height
    def resize_image(self):
        if not os.path.exists(self.input_path):
            raise ValueError(f"Input file does not exist: {self.input_path}")
        if os.path.isdir(self.output_path):
            raise ValueError(f"Output path is a directory, not a file: {self.output_path}")
        try:
            with Image.open(self.input_path) as img:
                width, height = img.size
                if self.target_width and self.target_height:
                    raise ValueError("Only one of target width or height should be specified.")
                elif self.target_width:
                    ratio = self.target_width / width
                    new_height = int(height * ratio)
                    new_width = self.target_width
                elif self.target_height:
                    ratio = self.target_height / height
                    new_width = int(width * ratio)
                    new_height = self.target_height
                else:
                    raise ValueError("Either target width or height should be specified.")
                resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
                resized_img.save(self.output_path)
        except IOError:
            raise ValueError(f"Could not open or identify image file: {self.input_path}")
        except Exception as e:
            raise ValueError(f"An error occurred: {str(e)}")
    def get_output_path(self):
        return self.output_path