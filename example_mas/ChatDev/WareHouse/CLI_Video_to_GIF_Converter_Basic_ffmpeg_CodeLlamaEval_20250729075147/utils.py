import os
import sys
def get_video_file_path(video_file_name):
    # Get the video file path from the command line arguments
    video_file_path = sys.argv[1]
    # Check if the video file exists
    if not os.path.exists(video_file_path):
        raise ValueError("Video file does not exist")
    return video_file_path
def get_output_file_path(output_file_name):
    # Get the output file path from the command line arguments
    output_file_path = sys.argv[2]
    # Check if the output file exists
    if os.path.exists(output_file_path):
        raise ValueError("Output file already exists")
    return output_file_path