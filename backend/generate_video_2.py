import moviepy.editor as mpe
nextInt = 0
# Get video/audio
v_clip = mpe.VideoFileClip('../template_videos/minecraft_parkour.mp4')
v_clip = v_clip.subclip(0, 5) 
audio_background = mpe.AudioFileClip('../template_videos/reddit_audio.mp3')
audio_background = audio_background.subclip(0, 5) 
# clip together
final_audio = mpe.CompositeAudioClip([v_clip.audio, audio_background])
v_clip.audio = final_audio
v_clip.write_videofile(f"../output_video/newVideo{nextInt}.mp4")