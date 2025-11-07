# cli.py
'''
Handles the Command Line Interface (CLI) for the Image Metadata Extractor tool.
'''
import sys
from image_metadata_extractor import ImageMetadataExtractor
def main():
    if len(sys.argv) != 2:
        print("Usage: python cli.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    extractor = ImageMetadataExtractor()
    metadata = extractor.extract_metadata(image_path)
    print(f"Format: {metadata['format']}")
    print(f"Resolution: {metadata['resolution']}")
    print(f"Creation Date: {metadata['creation_date']}")
if __name__ == "__main__":
    main()