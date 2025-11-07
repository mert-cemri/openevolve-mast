'''
Main application file for the video to GIF converter tool using argparse for CLI.
'''
import argparse
from video_converter import VideoConverter
def main():
    parser = argparse.ArgumentParser(description='Convert a video file segment to an animated GIF.')
    parser.add_argument('video_path', type=str, help='Path to the video file')
    args = parser.parse_args()
    try:
        converter = VideoConverter(args.video_path)
        converter.convert()
        print("Video converted to GIF successfully!")
    except Exception as e:
        print(f"Failed to convert video: {e}")
if __name__ == "__main__":
    main()