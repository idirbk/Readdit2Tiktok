import cv2
import pyttsx3
import numpy as np
from moviepy import editor as mp

def add_text_and_sound_to_video(video_path, text, output_path, i, start_time=0):
    # Open the video
    video = cv2.VideoCapture(video_path)

    # Get the video properties
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    # Convert text to speech
    engine = pyttsx3.init()
    engine.save_to_file(text, "text_audio_{}.wav".format(i))  # Save the speech as an audio file
    engine.runAndWait()

    # Load the audio file
    audio = mp.AudioFileClip("text_audio_{}.wav".format(i))

    # Create a VideoFileClip object
    video = mp.VideoFileClip(video_path)

    # Trim the video to match the audio duration, starting from start_time
    video = video.subclip(start_time, start_time + audio.duration)

    # Set the audio for the video
    video = video.set_audio(audio)

    # Add a fade in and fade out effect
    video = video.crossfadein(2).crossfadeout(2)

    # Function to add text to each frame
    def add_text(image):
        img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Add the white text in the center of the frame with a custom font
        font = cv2.FONT_HERSHEY_SIMPLEX  # Change the font type or use a font file
        font_scale = 1  # Font scale factor
        line_type = 2  # Line thickness and type
        font_color = (255, 255, 255)  # White color

        # Calculate the width of each word in the text
        words = text.split(' ')
        word_widths = [cv2.getTextSize(word, font, font_scale, line_type)[0][0] for word in words]

        # Define the width available for the text (80% of the frame's width)
        text_width = int(0.8 * width)

        # Split the text into multiple lines
        lines = []
        current_line = words[0]
        current_width = word_widths[0]
        for i in range(1, len(words)):
            if current_width + word_widths[i] < text_width:
                current_line += ' ' + words[i]
                current_width += word_widths[i]
            else:
                lines.append(current_line)
                current_line = words[i]
                current_width = word_widths[i]
        lines.append(current_line)

        # Calculate the height of a line of text
        _, text_height = cv2.getTextSize('Test', font, font_scale, line_type)

        # Increase the space between lines (e.g., by 50%)
        line_spacing = int(3 * text_height)

        # Calculate the starting y coordinate for the text
        start_y = (height - line_spacing * len(lines)) // 2

        # Draw each line
        for i, line in enumerate(lines):
            # Calculate the position for this line of text
            text_size = cv2.getTextSize(line, font, font_scale, line_type)[0]
            text_position = ((width - text_size[0]) // 2, start_y + i * line_spacing)
            cv2.putText(img, line, text_position, font, font_scale, font_color, line_type, cv2.LINE_AA)

        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Apply the function to each frame
    video = video.fl_image(add_text)

    # Write the final video with text and sound
    video.write_videofile(output_path, codec="libx264")

    # Cleanup temporary files
    audio.close()
    video.close()
    # delete audio file
    # os.remove("text_audio_{}.wav".format(i))
    cv2.destroyAllWindows()


def concatenate_videos(video_files, output_file):
    # Load video files and create clips
    video_clips = [mp.VideoFileClip(video) for video in video_files]

    # Concatenate the clips
    final_clip = mp.concatenate_videoclips(video_clips)

    # Write the result to a file
    final_clip.write_videofile(output_file, codec='libx264')


def split_text_into_sentences(text, max_length=50):
    # Split the text at each period
    sentences = text.split('.')

    # Remove any empty strings from the list
    sentences = [sentence.strip() for sentence in sentences if sentence.strip() != '']

    # Further split each sentence into chunks of at most max_length characters
    chunks = []
    for sentence in sentences:
        while len(sentence) > max_length:
            # Find the last space within max_length characters
            split_index = sentence.rfind(' ', 0, max_length)
            if split_index == -1:
                # If no space was found, just split at max_length
                split_index = max_length
            chunks.append(sentence[:split_index].strip())
            sentence = sentence[split_index:].strip()
        chunks.append(sentence)

    return chunks



if __name__ == '__main__':
    print("Starting the script")

    in_path = r"my_video.mp4"
    out_path = r"video_{}.mp4"

    # Example usage
    text = "ChatGPT is an advanced language model developed by OpenAI. It is trained on 8 million web pages and is able to generate realistic and coherent continuations of text. It can also perform rudimentary reading comprehension."

    texts = split_text_into_sentences(text)

    for i, chunk in enumerate(texts):
        print(f"Chunk {i + 1}: {texts[i]}")

    start_time = 0
    for i in range(len(texts)):
        print(texts[i])
        add_text_and_sound_to_video(in_path, texts[i], out_path.format(i), i, start_time)
        start_time += len(texts[i]) / 10  # adjust this to match your TTS speed

    # Example usage:
    video_files = []
    for i in range(len(texts)):
        print(out_path.format(i))
        video_files.append(out_path.format(i))

    output_file = r"concatenation.mp4"
    print('concatenation')
    concatenate_videos(video_files, output_file)