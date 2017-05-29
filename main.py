import pygame
import random

""" Setup """
# Window resolution
xres = 640
yres = 480
# Colors
black = (0x00, 0x00, 0x00)
green = (0x00, 0xFF, 0x00)
white = (0xFF, 0xFF, 0xFF)
yllow = (0xFF, 0xFF, 0x00)
# Screen and game font
pygame.init()
font = pygame.font.Font("Fonts/alterebro-pixel-font.ttf", 32)
screen = pygame.display.set_mode((xres, yres))
pygame.display.set_caption("Cleric")
screen.fill(black)
""" Loop """
done = False
while not done:
    """ Input """
    for event in pygame.event.get():
        # User pushed X to close window
        if event.type == pygame.QUIT:
            done = True
        # User pushed F1 to close window
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_F1:
                done = True
    """ Data """
    # Buffers a circle at a random point
    x = random.randint(0, xres)
    y = random.randint(0, yres)
    pygame.draw.circle(screen, green, (x, y), 8, 1)
    # Buffers a message at the top left
    label = font.render("Heya Sarch", True, yllow)
    x = 20
    y = 20
    screen.blit(label, (x, y))
    """ Output """
    # Renders buffer to display
    pygame.display.flip()
    # Locks the screen to a 60 Hz refresh rate
    fps = 60
    pygame.time.wait(1000 / fps)
# Done - Clean up
pygame.quit()
