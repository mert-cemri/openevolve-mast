'''
Utility functions for the Video to GIF Converter tool.
This file contains functions to handle video conversion and input validation.
'''
import os
import subprocess
import mimetypes
def convert_video_to_gif(file_path):
    '''
    Convert the first 5 seconds of a video file to an animated GIF.
    Args:
        file_path (str): Path to the video file.
    '''
    output_path = os.path.splitext(file_path)[0] + ".gif"
    command = [
        "ffmpeg",
        "-i", file_path,
        "-t", "5",
        "-vf", "fps=10,scale=320:-1:flags=lanczos",
        "-c:v", "gif",
        output_path
    ]
    try:
        subprocess.run(command, check=True, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("Error: ffmpeg is not installed or not in the system's PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {e.stderr.decode('utf-8')}")
    except Exception as e:
        print(f"Conversion failed: {str(e)}")
def validate_input(file_path):
    '''
    Validate the input file path to ensure it is a valid video file.
    Args:
        file_path (str): Path to the video file.
    Returns:
        bool: True if the file path is valid, False otherwise.
    '''
    if not os.path.isfile(file_path):
        print("Error: File does not exist.")
        return False
    if not os.access(file_path, os.R_OK):
        print("Error: File is not readable.")
        return False
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None or not mime_type.startswith('video/'):
        print("Error: File is not a valid video file.")
        return False
    return True