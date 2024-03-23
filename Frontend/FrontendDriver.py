## Driver file

import pygame
from Display import Screen

pygame.init()

screen = Screen.StartDisplay(pygame)

# Main Runtime loop
running = True
while running :
    Screen.DisplayUi(pygame, screen)

    # Check events code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()