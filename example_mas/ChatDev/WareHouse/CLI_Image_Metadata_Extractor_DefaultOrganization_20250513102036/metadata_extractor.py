'''
Module to extract metadata from image files.
'''
from PIL import Image
from PIL.ExifTags import TAGS
def extract_metadata(file_path):
    '''
    Extracts metadata such as resolution, format, and creation date from the given image file.
    :param file_path: Path to the image file.
    :return: Dictionary containing metadata.
    '''
    metadata = {}
    try:
        with Image.open(file_path) as img:
            metadata['Format'] = img.format
            metadata['Resolution'] = img.size
            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    decoded_tag = TAGS.get(tag, tag)
                    if decoded_tag == 'DateTime':
                        metadata['Creation Date'] = value
    except Exception as e:
        metadata['Error'] = str(e)
    return metadata