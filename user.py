import pygame
import tile
import zone

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
    global choice, editing, selected, sheet, saved
    if event.type == pygame.MOUSEBUTTONDOWN:
        saved = False
        click = tile.tile(pygame.mouse.get_pos())
        # Mouse buttons
        left = 1; middle = 2; right = 3; up = 4; down = 5
        # Right mouse button was pushed
        if event.button == right:
            editing = True
        # Mouse scroll down
        if editing and event.button == down:
            sheet -= 1
            if sheet < 0: sheet = 0
        # Mouse scroll up
        if editing and event.button == up:
            sheet += 1
            if sheet >= len(tile.sheets): sheet = len(tile.sheets) - 1
        # Left mouse button was pushed on the editing screen
        elif event.button == left and editing:
            choice = click
            editing = False
        elif event.button == left:
            selected = click
    else:
        selected = None

def keyboard(event):
    global done, saved
    if event.type == pygame.QUIT:
        done = True
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
            done = True
        if event.key == pygame.K_F5:
            zone.save("Zones/home")
            saved = True

def input():
    for event in pygame.event.get():
        mouse(event)
        keyboard(event)
