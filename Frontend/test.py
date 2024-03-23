import tkinter as tk
import vlc
from PIL import Image, ImageTk

class StateApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.state = False  # Initial state is starting screen
        self.title("Block Talk")
        self.configure(bg="white")
        self.geometry("500x700")
        self.MakeInitialScreen()

    def MakeInitialScreen(self):
        self.titleImagePath = "Frontend/Graphics/BlokTokLogo.png"
        self.titleImage = Image.open(self.titleImagePath)
        self.titleImage = self.titleImage.resize((500, 100))
        self.tkTitleImage = ImageTk.PhotoImage(self.titleImage)

        self.titleLabel = tk.Label(self, image=self.tkTitleImage, bg="white")
        self.titleLabel.pack()

        self.descriptionLabel = tk.Label(self, text="Enter a Reddit URL")
        self.descriptionLabel.pack(pady=10)

        self.urlInput = tk.Text(self)
        self.urlInput.pack(pady=10)

        self.toggle_button = tk.Button(self, text="Generate Brainrot Video", command=self.PlayVideo)
        self.toggle_button.pack()

    def PlayVideo(self):
        # Get url
        url = self.urlInput.get(1.0, "end-1c") 
        print(url)

        # Send url to backend for processing

        # Get returned video
        videoPath = "Frontend/Graphics/testClip.mp4"

        # Reset the screen
        self.urlInput.destroy()
        self.titleLabel.destroy()
        self.descriptionLabel.destroy()
        self.toggle_button.destroy()
        self.state = not self.state

        # add the video player
        # Create a frame to hold the video player
        self.video_frame = tk.Frame(self)
        self.video_frame.pack(fill=tk.BOTH, expand=True)

        # Initialize the VLC player
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.player.set_fullscreen(True)  # Uncomment this line for fullscreen playback

        # Load the video file
        self.media = self.instance.media_new(videoPath)
        self.player.set_media(self.media)

        # Embed the video player in the Tkinter window
        self.player.set_hwnd(self.video_frame.winfo_id())

        # Play the video
        self.player.play()

if __name__ == "__main__":
    app = StateApp()
    app.mainloop()