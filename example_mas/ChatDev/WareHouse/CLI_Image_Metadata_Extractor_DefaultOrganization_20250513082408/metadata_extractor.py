'''
Module to extract metadata from image files using Pillow.
'''
from PIL import Image
from PIL.ExifTags import TAGS
import os
class ImageMetadataExtractor:
    def extract_metadata(self, file_path):
        try:
            with Image.open(file_path) as img:
                metadata = {
                    "Format": img.format,
                    "Resolution": f"{img.width}x{img.height}"
                }
                # Extract EXIF data if available
                exif_data = img._getexif()
                if exif_data:
                    for tag_id, value in exif_data.items():
                        tag = TAGS.get(tag_id, tag_id)
                        if tag == 'DateTime':
                            metadata["Creation Date"] = value
                # Format metadata for display
                metadata_str = "\n".join(f"{key}: {value}" for key, value in metadata.items())
                return metadata_str
        except Exception as e:
            print(f"Error extracting metadata: {e}")
            return None