'''
Main entry point for the CLI tool to extract and display image metadata.
'''
import sys
from metadata_extractor import ImageMetadataExtractor
class ImageMetadataCLI:
    def __init__(self):
        self.extractor = ImageMetadataExtractor()
    def run(self, file_path):
        if file_path:
            metadata = self.extractor.extract_metadata(file_path)
            if metadata:
                print("Image Metadata:\n", metadata)
            else:
                print("Error: Could not extract metadata.")
        else:
            print("Error: No file path provided. Please provide an image file path.")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_file_path>")
    else:
        file_path = sys.argv[1]
        cli = ImageMetadataCLI()
        cli.run(file_path)