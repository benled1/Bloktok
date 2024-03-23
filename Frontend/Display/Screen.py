## Main Display Functionality

def CreateLabel(message, size, frame, tk) :
    return tk.Label(frame, text = message)

def CreateButton(message, size, callback, frame, tk) :
    return tk.Button(frame, text = message, command = callback)

def CreateTextInput(height, width, frame, tk) :
    return tk.Text(frame)