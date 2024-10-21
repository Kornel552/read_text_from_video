import moviepy.editor as mp
import whisper


def mp4_to_wav(path):
    # Load the video
    video = mp.VideoFileClip(path)

    # Extract the audio from the video
    audio_file = video.audio
    audio_file.write_audiofile("wav\\robak.wav")


mp4_to_wav("mp4\\robak.mp4")


def read_video_to_txt(path):
    # Load model (you can choose: tiny, base, small, medium, large)
    model = whisper.load_model("small") # choose

    # Transcript
    result = model.transcribe(path, language="pl")

    # Results
    print(result["text"])
    txt = result["text"]
    txt_file = open("text\\robak.txt", "a", encoding='utf8')
    txt_file.write(txt)
    txt_file.close()


read_video_to_txt("wav\\robak.wav")
