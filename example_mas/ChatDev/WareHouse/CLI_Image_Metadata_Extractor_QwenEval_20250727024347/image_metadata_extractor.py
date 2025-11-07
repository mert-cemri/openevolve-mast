'''
Handles the extraction of metadata from image files.
'''
from PIL import Image
import exifread
class ImageMetadataExtractor:
    def extract_metadata(self, image_path):
        '''
        Extracts metadata from the given image file.
        Handles exceptions for unsupported formats and invalid files.
        Returns a dictionary containing the format, resolution, and creation date.
        '''
        try:
            with open(image_path, 'rb') as f:
                tags = exifread.process_file(f)
                image = Image.open(image_path)
        except IOError:
            return {
                'format': 'Unknown',
                'resolution': 'Unknown',
                'creation_date': 'Not available'
            }
        format = image.format
        resolution = image.size
        creation_date = self.get_creation_date(tags)
        return {
            'format': format,
            'resolution': resolution,
            'creation_date': creation_date
        }
    def get_creation_date(self, tags):
        '''
        Retrieves the creation date from the EXIF data.
        Returns a user-friendly message if the creation date is not available.
        '''
        date_tag = tags.get('EXIF DateTimeOriginal', tags.get('Image DateTime'))
        if date_tag:
            return date_tag.values
        return "Not available"