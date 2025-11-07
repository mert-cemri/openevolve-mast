import os
import sys
import moviepy
from moviepy.editor import VideoFileClip
def convert_video_to_gif(video_file_path, output_file_path, fps=10):
    # Create a VideoFileClip object from the video file
    video_clip = VideoFileClip(video_file_path)
    # Get the first 5 seconds of the video clip
    video_clip_5_seconds = video_clip.subclip(0, 5)
    # Convert the video clip to an animated GIF
    video_clip_5_seconds.write_gif(output_file_path, fps=fps)
def convert_video_to_mp4(video_file_path, output_file_path):
    # Create a VideoFileClip object from the video file
    video_clip = VideoFileClip(video_file_path)
    # Convert the video clip to an MP4 file
    video_clip.write_videofile(output_file_path, fps=10)