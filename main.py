import moviepy.editor as mp
import whisper


def mp4_to_wav(path):
    # Load the video
    video = mp.VideoFileClip(path)

    # Extract the audio from the video
    audio_file = video.audio
    audio_file.write_audiofile("C:\\Users\\kkrzak\\PycharmProjects\\read_text_from_video\\wav\\audio1-en.wav")


mp4_to_wav("C:\\Users\\kkrzak\\PycharmProjects\\read_text_from_video\\mp4\\video-en.mp4")


def read_video(path):
    # Load model (you can chose: tiny, base, small, medium, large)
    model = whisper.load_model("small") # Wybierz model odpowiedni dla twojego sprzętu

    # Transcript
    result = model.transcribe(path, language="en")

    # Results
    print(result["text"])


read_video("C:\\Users\\kkrzak\\Desktop\\audio1-en.wav")
