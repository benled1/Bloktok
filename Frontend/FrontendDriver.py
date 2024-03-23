## Driver file

import tkinter as tk 
from Display import Screen

# Scale values
sizeX = 500
sizeY = 700

urlString = ""

def SaveInput() : 
    url = textBox.get(1.0, "end-1c") 
    urlString = url
    print(urlString)
  
frame = tk.Tk() 
frame.title("TikTok Garbage Generator") 
frame.geometry("% sx% s" % (sizeX, sizeY)) 

Screen.CreateLabel("TikTok Garbage Generator", 0, frame, tk).pack(pady=100, side=tk.TOP)
Screen.CreateButton("Test button", 0, SaveInput, frame, tk).pack(pady=100, side = tk.BOTTOM)
textBox = Screen.CreateTextInput(12, int(sizeX/2), frame, tk)
textBox.pack(side=tk.BOTTOM)

frame.mainloop() 