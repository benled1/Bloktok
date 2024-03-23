## Driver file

from Display import Screen

display = Screen.StartDisplay()

# Main Runtime loop
running = True
while running:
    # Check events code
    for event in display.event.get():
        if event.type == display.QUIT:
            running = False

    display.display.update()