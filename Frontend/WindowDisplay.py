import tkinter as tk
import vlc
from PIL import Image, ImageTk
from backend.createVideo import createVideo

# Colours
red = "#FF4500"
lightRed = "#f08760"
black = "#000000"
blue = "#CEE3F8"
white = "#FFFFFF"

# Font
gillLarge = ("Gill Sans", 18)
gillMed = ("Gill Sans", 12)

# Padding intervals
bigPadding = 100
smallPadding = 8

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

        self.titleLabel = tk.Label(self, 
                                   image=self.tkTitleImage, 
                                   bg=white)
        self.titleLabel.grid(row=1, 
                             column=0, 
                             padx=smallPadding, 
                             pady=bigPadding)

        self.urlInput = tk.Text(self, 
                                height=1, 
                                width=50, 
                                bg=lightRed, 
                                font=gillMed)
        self.urlInput.grid(row=2, 
                           column=0, 
                           padx=smallPadding, 
                           pady=smallPadding)
        
        self.descriptionLabel = tk.Label(self, 
                                         text="ENTER A REDDIT URL", 
                                         bg=white, 
                                         fg=red, 
                                         font=gillMed)
        self.descriptionLabel.grid(row=3, 
                                   column=0, 
                                   padx=smallPadding, 
                                   pady=smallPadding)

        self.toggleButton = tk.Button(self, 
                                      text="GENERATE BRAINROT", 
                                      command=self.PlayVideo, 
                                      bg=black, 
                                      fg=white, 
                                      borderwidth=0, 
                                      font=gillLarge)
        self.toggleButton.grid(row=4, 
                               column=0, 
                               padx=smallPadding, 
                               pady=bigPadding)

    def PlayVideo(self):
        # Get url
        url = self.urlInput.get(1.0, "end-1c") 
        print(url)

        # Send url to backend for processing
        videoPath = createVideo(url)

        # Reset the screen
        self.urlInput.destroy()
        self.titleLabel.destroy()
        self.descriptionLabel.destroy()
        self.toggleButton.destroy()
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