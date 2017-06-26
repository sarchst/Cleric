import pygame
import tile
import zone

class public:
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
    global public
    if event.type == pygame.MOUSEBUTTONDOWN:
        public.saved = False
        click = tile.tile(pygame.mouse.get_pos())
        # Mouse buttons
        left = 1; middle = 2; right = 3; up = 4; down = 5
        # Right mouse button was pushed
        if event.button == right:
            public.editing = True
        # Mouse scroll down
        if public.editing and event.button == down:
            public.sheet -= 1
            if public.sheet < 0: public.sheet = 0
        # Mouse scroll up
        if public.editing and event.button == up:
            public.sheet += 1
            if public.sheet >= len(tile.sheets): public.sheet = len(tile.sheets) - 1
        # Left mouse button was pushed on the editing screen
        elif event.button == left and public.editing:
            public.choice = click
            public.editing = False
        elif event.button == left:
            public.selected = click
    else:
        public.selected = None

def keyboard(event):
    global public
    if event.type == pygame.QUIT:
        public.done = True
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
            public.done = True
        if event.key == pygame.K_F5:
            zone.save("Zones/home")
            public.saved = True

def input():
    for event in pygame.event.get():
        mouse(event)
        keyboard(event)
