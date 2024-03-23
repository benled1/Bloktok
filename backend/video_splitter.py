import moviepy.editor as mpe
full_video = '../template_videos/minecraft_parkour.mp4'
current_duration = mpe.VideoFileClip(full_video).duration
divide_into_count = 5
single_duration = current_duration/divide_into_count
current_video = f"{current_duration}.mp4"

while current_duration > single_duration:
    clip = mpe.VideoFileClip(full_video).subclip(current_duration-single_duration, current_duration)
    current_duration -= single_duration
    current_video = f"{current_duration}.mp4"
    clip.to_videofile(current_video, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')