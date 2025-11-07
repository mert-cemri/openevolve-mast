'''
Handles the conversion of video files to GIF using ffmpeg.
'''
import subprocess
import os
class VideoConverter:
    def __init__(self, video_path):
        self.video_path = video_path
        self.output_path = os.path.splitext(video_path)[0] + ".gif"
    def convert(self):
        # Command to convert the first 5 seconds of the video to GIF
        command = [
            "ffmpeg",
            "-t", "5",  # Duration of the segment
            "-i", self.video_path,  # Input file
            "-vf", "fps=10,scale=320:-1:flags=lanczos",  # Video filter for frame rate and scaling
            "-c:v", "gif",  # Output format
            self.output_path  # Output file
        ]
        try:
            # Run the command and capture output
            subprocess.run(command, check=True, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            error_message = e.stderr.decode('utf-8').strip()  # Decode the bytes to a string
            raise RuntimeError(f"ffmpeg error: {error_message}")