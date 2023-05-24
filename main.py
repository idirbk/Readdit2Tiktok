import os
from readit.reddit import get_story
from editing.edit import split_text_into_sentences, add_text_and_sound_to_video, concatenate_videos
from videos.requests_videos import generate_video

# delete video.mp4
file_path = "video.mp4"
output_path = "tik_tok_{}.mp4"
final_video = "tik_tok.mp4"
theme = 'fortnite'

if __name__ == '__main__':
    try:
        generate_video(theme)
        stories = get_story(1)
        text = ''

        for story in stories:
            text = story.selftext

        texts = split_text_into_sentences(text)

        start_time = 0

        for i in range(len(texts)):
            print(texts[i])
            add_text_and_sound_to_video(file_path, texts[i], output_path.format(i), i, start_time)
            start_time += len(texts[i]) / 10  # adjust this to match your TTS speed

        # Example usage:
        video_files = []
        for i in range(len(texts)):
            print(output_path.format(i))
            video_files.append(output_path.format(i))

        concatenate_videos(video_files, final_video)

    except :
        pass

