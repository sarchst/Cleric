import pygame

floor = [
    pygame.transform.scale2x(pygame.image.load("Objects/Floor.png")),
    pygame.transform.scale2x(pygame.image.load("Objects/Floor.png"))
]

cats = [
    pygame.transform.scale2x(pygame.image.load("Characters/Cat0.png")),
    pygame.transform.scale2x(pygame.image.load("Characters/Cat1.png"))
]

width = 32

def tile((x, y)):
    """
    Returns a tie tuple of a pixel tuple
    """
    return (x / width, y / width)

def pixel((x, y)):
    """
    Returns a pixel tuple of a tile tuple.
    """
    return (x * width, y * width)

def rect((x, y)):
    """
    Returns a rectangular tile tuple of a tile tuple.
    """
    return (pixel((x, y)), (width, width))
