'''
Main application file for the video to GIF converter tool using command-line interface.
'''
import argparse
import os
from ffmpeg_utils import run_ffmpeg
def main():
    parser = argparse.ArgumentParser(description='Convert a video file segment to an animated GIF.')
    parser.add_argument('video_path', type=str, help='Path to the input video file.')
    parser.add_argument('output_path', type=str, help='Path to save the output GIF file.')
    args = parser.parse_args()
    video_path = args.video_path
    output_path = args.output_path
    if not os.path.exists(video_path):
        print("Please provide a valid video file path.")
        return
    success = run_ffmpeg(video_path, output_path)
    if success:
        print(f"Conversion successful! GIF saved at {output_path}")
    else:
        print("Conversion failed. Please check the video file and try again.")
if __name__ == "__main__":
    main()