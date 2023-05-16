import cv2

def add_text_to_video(video_path, texts, output_path):
    # Open the video
    video = cv2.VideoCapture(video_path)

    # Get the video properties
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    # Create a VideoWriter object to write the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Variables for tracking time and text index
    elapsed_time = 0
    text_index = 0

    # Loop through each frame of the video
    while True:
        ret, frame = video.read()

        if not ret:
            break

        # Add the white text in the center of the frame with a custom font
        font = cv2.FONT_HERSHEY_SIMPLEX  # Change the font type or use a font file
        font_scale = 1  # Font scale factor
        font_color = (255, 255, 255)  # White color
        line_type = 2  # Line thickness and type
        text_size, _ = cv2.getTextSize(texts[text_index], font, font_scale, line_type)
        text_position = (int((width - text_size[0]) / 2), int((height + text_size[1]) / 2))
        cv2.putText(frame, texts[text_index], text_position, font, font_scale, font_color, line_type, cv2.LINE_AA)

        # Write the frame with the text to the output video
        out.write(frame)

        # Increment elapsed time
        elapsed_time += 1

        # Check if 5 seconds have passed
        if elapsed_time == int(fps) * 5:
            # Increment the text index
            text_index = (text_index + 1) % len(texts)
            elapsed_time = 0

    # Release resources
    video.release()
    out.release()
