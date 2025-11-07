'''
Main application file to initialize the CLI for the image metadata extractor.
'''
import argparse
from metadata_extractor import extract_metadata
def main():
    parser = argparse.ArgumentParser(description='Extract metadata from image files.')
    parser.add_argument('file_path', type=str, help='Path to the image file')
    args = parser.parse_args()
    metadata = extract_metadata(args.file_path)
    if 'Error' in metadata:
        print(f"Error: {metadata['Error']}")
    else:
        for key, value in metadata.items():
            print(f"{key}: {value}")
if __name__ == "__main__":
    main()