from moviepy.editor import *


def add_sound_to_video(video_path, sound_path, output_path):
    """
    This function adds an audio file to a video file and saves the result to a new file.

    Parameters:
    video_path (str): The path of the video file.
    sound_path (str): The path of the audio file.
    output_path (str): The path of the output file.

    Returns:
    None
    """

    # Load the video and audio files
    video_clip = VideoFileClip(video_path)
    sound_clip = AudioFileClip(sound_path)

    # Add the audio to the video
    video_clip = video_clip.set_audio(sound_clip)

    # Write the result to a new file, specifying the codec
    video_clip.write_videofile(output_path, codec='libx264')

    # Close the clips
    video_clip.close()
    sound_clip.close()
