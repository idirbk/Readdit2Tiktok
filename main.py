import os
import time
from readit.reddit import get_story
from editing.edit import split_text_into_sentences, add_text_and_sound_to_video, concatenate_videos
from videos.requests_videos import generate_video


file_path = "video.mp4"
output_path = "tik_tok_{}.mp4"
final_video = "tik_tok.mp4"
theme = 'minecraft'

# Specify the directory path where you want to delete the files
directory_path = "./"

# Specify the file extensions you want to delete
extensions_to_delete = [".mp4", ".wav"]

# Specify the file name that you want to keep
file_to_keep_video = "video.mp4"

def delete_files_with_extensions(directory, extensions, file_to_keep_video):
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions) and file != file_to_keep_video and  file != final_video:
                file_path = os.path.join(root, file)

                try:
                    os.remove(file_path)

                except Exception as err:
                    print(f"Unexpected {err=}, {type(err)=}")

                print(f"Deleted file: {file_path}")


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


    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


    finally:
        time.sleep(60)
        # Call the function to delete the files
        delete_files_with_extensions(directory_path, extensions_to_delete, file_to_keep_video)
