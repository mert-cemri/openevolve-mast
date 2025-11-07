'''
Utility functions for running ffmpeg commands.
'''
import subprocess
def is_ffmpeg_installed():
    '''
    Check if ffmpeg is installed and accessible from the command line.
    Returns:
    - installed: Boolean indicating if ffmpeg is installed.
    '''
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
def run_ffmpeg(input_path, output_path):
    '''
    Run the ffmpeg command to convert a video segment to a GIF.
    Parameters:
    - input_path: Path to the input video file.
    - output_path: Path to save the output GIF file.
    Returns:
    - success: Boolean indicating if the conversion was successful.
    '''
    if not is_ffmpeg_installed():
        print("Error: ffmpeg is not installed or not found in the system's PATH.")
        return False
    try:
        # Command to extract the first 5 seconds and convert to GIF
        command = [
            "ffmpeg", "-y", "-i", input_path, "-t", "5", "-vf", "fps=10,scale=320:-1:flags=lanczos", output_path
        ]
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed with error: {e}")
        return False