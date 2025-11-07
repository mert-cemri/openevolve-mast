import os
import sys
import ffmpeg
from PIL import Image
from moviepy.editor import VideoFileClip
def main():
    # Get the video file path from the command line arguments
    video_file_path = sys.argv[1]
    # Get the output file path from the command line arguments
    output_file_path = sys.argv[2]
    # Create a VideoFileClip object from the video file
    video_clip = VideoFileClip(video_file_path)
    # Get the first 5 seconds of the video clip
    video_clip_5_seconds = video_clip.subclip(0, 5)
    # Convert the video clip to an animated GIF
    video_clip_5_seconds.write_gif(output_file_path, fps=10)
if __name__ == "__main__":
    main()