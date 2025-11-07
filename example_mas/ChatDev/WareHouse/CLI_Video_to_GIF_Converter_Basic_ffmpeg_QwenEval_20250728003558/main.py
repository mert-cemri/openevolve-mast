'''
Main application file for the Video to GIF Converter tool.
This file initializes the application and sets up the CLI.
'''
import argparse
from video_converter import convert_video_to_gif, validate_input
def main():
    '''
    Main function to handle command-line arguments and execute the conversion process.
    '''
    parser = argparse.ArgumentParser(description="Convert a short video file segment into an animated GIF.")
    parser.add_argument("file_path", type=str, help="Path to the video file")
    args = parser.parse_args()
    file_path = args.file_path
    if not validate_input(file_path):
        return
    try:
        convert_video_to_gif(file_path)
        print("GIF conversion successful!")
    except FileNotFoundError:
        print("Error: ffmpeg is not installed or not in the system's PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {e.stderr.decode('utf-8')}")
    except Exception as e:
        print(f"Conversion failed: {str(e)}")
if __name__ == "__main__":
    main()