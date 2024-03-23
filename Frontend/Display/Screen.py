## Main Display Functionality

# Scale values
sizeX = 500
sizeY = 700
fontSizeLarge = 56
fontSizeMed = 36
fontSizeSmall = 24

# Colours
black = (0,0,0)
white = (255,255,255)
grey = (177,177,177)

def StartDisplay(pygame) :
    background_colour = (255,255,255)
    (width, height) = (sizeX, sizeY)
    icon = pygame.image.load('Frontend/Graphics/hackathonLogo1.png')

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tiktok Garbage Generator')
    pygame.display.set_icon(icon)
    screen.fill(background_colour)

    return screen

def DisplayUi(pygame, screen) :
    # Fonts
    largeFont = pygame.font.SysFont("Open Sans", fontSizeLarge)
    medFont = pygame.font.SysFont("Open Sans", fontSizeMed)
    smallFont = pygame.font.SysFont("Open Sans", fontSizeSmall)

    DisplayText("TikTok Garbage", sizeX/2, sizeY/4 - fontSizeLarge + 10, largeFont, black, screen)
    DisplayText("Generator", sizeX/2, sizeY/4, largeFont, black, screen)

    DisplayText("Enter a Reddit post URL", sizeX/2, 3*sizeY/4, smallFont, grey, screen)

def DisplayText(message, x, y, font, colour, screen) :
    text = font.render( message, True, colour, white)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)