import moviepy.editor as mpe
from moviepy.video.fx.all import crop
import os
import random
import math
from .text_parsing import client

def createVideo(url: str) -> str:
    # Replace the next string with the output string from get audio
    # Get audio
        
    # Call getAudio
    
    # Delete next 2 lines once getAudio is implemented
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
    file_output_path = f"output_video/newVideo{videos_created}.mp4"
    v_clip.write_videofile(file_output_path)
    return file_output_path