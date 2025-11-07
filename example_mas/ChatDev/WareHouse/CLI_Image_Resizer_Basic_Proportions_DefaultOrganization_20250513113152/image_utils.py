'''
Utility functions for image processing, including resizing images while maintaining aspect ratio.
'''
from PIL import Image
def resize_image(image, target_width=None, target_height=None):
    original_width, original_height = image.size
    if target_width and not target_height:
        ratio = target_width / original_width
        target_height = int(original_height * ratio)
    elif target_height and not target_width:
        ratio = target_height / original_height
        target_width = int(original_width * ratio)
    elif not target_width and not target_height:
        raise ValueError("Either target width or target height must be specified")
    resized_image = image.resize((target_width, target_height), Image.ANTIALIAS)
    return resized_image