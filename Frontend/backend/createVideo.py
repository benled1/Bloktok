import moviepy.editor as mpe
from moviepy.video.fx.all import crop
from moviepy.video.tools.subtitles import SubtitlesClip
import os
import random
import math
from .text_parsing import client
from faster_whisper import WhisperModel

def createVideo(url: str) -> str:
    # Replace the next string with the output string from get audio
    # Get audio
        
    audio_path = client.get_audio(url)["audio_filepath"]
    audio_background = mpe.AudioFileClip(audio_path)
 
    # Subclip a random part of it 
    # Get video
    audio_duration = audio_background.duration
    videos = []
    for i in range(0,4):
        videos.append(mpe.VideoFileClip(f'template_videos/minecraft_parkour_{i}.mp4'))
    v_clip = mpe.concatenate_videoclips(videos)
    video_start = random.randint(0, ((int)(v_clip.duration - audio_duration)) + 1)
    video_end = video_start + audio_duration + 1
    v_clip = v_clip.subclip(video_start, video_end)
    v_clip = v_clip.set_audio(audio_background)
    v_clip = crop(v_clip, x1=300, y1=10, x2=552, y2=470)
    # Create a new video with the name
    videos_created = len(os.listdir('output_video/'))
    #Create subtitles
    subtitle_file = transcribeAudio(audio_path, videos_created)
    generator = lambda txt: mpe.TextClip(txt, font='Impact', fontsize=50, color="white", stroke_color="black", stroke_width=2,  size=v_clip.size)
    subtitles = SubtitlesClip(subtitle_file, generator)
    # Create a new video with the name
    file_output_path = f"output_video/newVideo{videos_created}.mp4"
    final = mpe.CompositeVideoClip([v_clip, subtitles])
    final.write_videofile(file_output_path)

    return file_output_path

def transcribeAudio(audioFilePath: str, videoNum: int):
    model = WhisperModel("small")
    segments, info = model.transcribe(audioFilePath, word_timestamps=True)
    language = info[0]
    segments = list(segments)
    # Delete old file if it exists
    if os.path.exists(f"output_video/sub-subtitle.{language}.srt"):
        os.remove(f"output_video/sub-subtitle.{language}.srt")
    subtitle_file = f"output_video/sub-subtitle.{language}.srt"
    text = ""
    index = 0
    for segment in segments:
        for word in segment.words:
            word_start = format_time(word.start)
            word_end = format_time(word.end)
            text += f"{str(index+1)} \n"
            text += f"{word_start} --> {word_end} \n"
            new_word = word.word.replace(" ", "")
            text += f"{new_word} \n"
            text += "\n"
            index += 1
        
    f = open(subtitle_file, "w")
    f.write(text)
    f.close()

    return subtitle_file

def format_time(seconds):

    hours = math.floor(seconds / 3600)
    seconds %= 3600
    minutes = math.floor(seconds / 60)
    seconds %= 60
    milliseconds = round((seconds - math.floor(seconds)) * 1000)
    seconds = math.floor(seconds)
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"

    return formatted_time
