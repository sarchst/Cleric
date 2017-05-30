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
