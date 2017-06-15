import pygame
# Tiles are 32 pixels by 32 pixels wide.
width = 32

def size((x, y)):
    """
    Returns a pixel tuple of a tile tuple.
    """
    return (x * width, y * width)

def rect((x, y)):
    """
    Returns a rectangular tile tuple of a tile tuple.
    """
    return ((x * width, y * width), (width, width))

floor = [
    pygame.transform.scale2x(pygame.image.load("Objects/Floor.png")),
    pygame.transform.scale2x(pygame.image.load("Objects/Floor.png"))
]
cats = [
    pygame.transform.scale2x(pygame.image.load("Characters/Cat0.png")),
    pygame.transform.scale2x(pygame.image.load("Characters/Cat1.png"))
]
