# Tiles are 16 pixels by 16 pixels wide.
width = 16

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
