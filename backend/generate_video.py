from moviepy.editor import *

input_file = '/Users/anneboltwood/Documents/Code/jungle.mp4'
output_file = '/Users/anneboltwood/Documents/Code/out.mp4'
audio_file = '/Users/anneboltwood/Documents/Code/aud1.mp3'


audioclip = AudioFileClip(audio_file)
audio_duration = audioclip.duration

clip = VideoFileClip(input_file).subclip(0, audio_duration+1)
clip = clip.set_audio(audioclip)


# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip("Minecraft",fontsize=70,color='white')

# Say that you want it to appear 10s at the center of the screen
txt_clip = txt_clip.set_pos('center').set_duration(10)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip, txt_clip])

# Write the result to a file (many options available !)
video.write_videofile(output_file)