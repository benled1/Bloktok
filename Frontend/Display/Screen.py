## Main Display Functionality

import pygame

def StartDisplay() :
    pygame.init()

    background_colour = (255,255,255)
    (width, height) = (500, 700)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tiktok Garbage Generator')
    screen.fill(background_colour)

    return pygame