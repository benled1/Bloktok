## Driver file

import tkinter as tk 
from Display import Screen

# State of app
state = 0

# Scale values
sizeX = 500
sizeY = 700

# URL Capture
urlString = ""

def SaveInput(textBox) : 
    url = textBox.get(1.0, "end-1c") 
    urlString = url
    print(urlString)
    DrawEndingScreen()
  
frame = tk.Tk() 
frame.title("TikTok Garbage Generator") 
frame.geometry("% sx% s" % (sizeX, sizeY)) 

def DrawStartingScreen() :
    Screen.CreateLabel("TikTok Garbage Generator", 0, frame, tk).pack(pady=100, side=tk.TOP)
    textBox = Screen.CreateTextInput(12, int(sizeX/2), frame, tk)
    Screen.CreateButton("Test button", 0, SaveInput(textBox), frame, tk).pack(pady=100, side = tk.BOTTOM)
    textBox.pack(side=tk.BOTTOM)

def DrawEndingScreen():
    Screen.CreateLabel("TikTok Garbage Generator 2", 0, frame, tk).pack(pady=100, side=tk.TOP)

DrawStartingScreen()

frame.mainloop() 