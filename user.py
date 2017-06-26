import pygame
import tile
import zone
import time

class public:
    """
    Public attributes.
    """
    done = False
    editing = False
    # The chosen tile of the editing screen
    choice = tile.pixel((0, 0))
    # The selected tile of the playing screen
    selected = None
    # The sprite sheet to use
    sheet = 0
    # Saved
    saved = False

def mouse(event):
    """
    Updates public attributes with mouse event.
    """
    global public
    class button:
        left = 1
        middle = 2
        right = 3
    class scroll:
        up = 4
        down = 5
    if event.type == pygame.MOUSEBUTTONDOWN:
        public.saved = False
        click = tile.tile(pygame.mouse.get_pos())
        # Mouse scroll up
        if public.editing and event.button == scroll.up:
            public.sheet += 1
            if public.sheet >= len(tile.sheets):
                public.sheet = len(tile.sheets) - 1
        # Mouse scroll down
        elif public.editing and event.button == scroll.down:
            public.sheet -= 1
            if public.sheet < 0:
                public.sheet = 0
        # Right mouse button was pushed
        elif event.button == button.right:
            public.editing = True
        # Left mouse button was pushed on the editing screen
        elif public.editing and event.button == button.left:
            public.choice = click
            public.editing = False
            public.selected = False
        # Left mouse button was pushed on game screen
        elif event.button == button.left:
            public.selected = click

def keyboard(event):
    """
    Updates public attributes with a keyboard event.
    """
    global public
    if event.type == pygame.QUIT:
        public.done = True
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
            public.done = True
        if event.key == pygame.K_F5 and not public.editing:
            zone.save("Zones/home")
            public.saved = True

def input(timeout):
    """
    Polls for a single keyboard / mouse action.
    Timeout in milliseconds.
    """
    waiting = True
    while waiting:
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN\
        or event.type == pygame.KEYDOWN:
            mouse(event)
            keyboard(event)
            timeout = 0
        if timeout <= 0:
            waiting = False
        timeout -= 1
        time.sleep(0.001)
