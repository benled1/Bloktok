import moviepy.editor as mpe
import os
import random

def createVideo(url: str) -> str:
    # Replace the next string with the output string from get audio
    # Get audio
        
    # Call getAudio
    
    # Delete next 2 lines once getAudio is implemented
    audio_background = mpe.AudioFileClip('template_videos/reddit_audio.mp3')
    audio_background = audio_background.subclip(0,180)
 
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
    # Create a new video with the name
    videos_created = len(os.listdir('output_video/'))
    file_output_path = f"output_video/newVideo{videos_created}.mp4"
    v_clip.write_videofile(file_output_path)
    return file_output_path