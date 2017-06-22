import pygame
import tile
import zone

done = False
editingScreen = False
# The chosen tile of the editing screen
choice = tile.pixel((0, 0))
# The selected tile of the playing screen
select = None

def mouse(event):
    global choice, editingScreen, select
    if event.type == pygame.MOUSEBUTTONDOWN:
        click = tile.tile(pygame.mouse.get_pos())
        # Mouse buttons.
        left = 1; middle = 2; right = 3
        # Right mouse button was pushed.
        if event.button == right:
            editingScreen = True
        # Left mouse button was pushed on the editing screen.
        elif event.button == left and editingScreen:
            choice = click
            editingScreen = False
        elif event.button == left:
            select = click
    else:
        select = None

def keyboard(event):
    global done
    if event.type == pygame.QUIT:
        done = True
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F5:
            zone.save(zone.terrain, zone.sprites)
def getInput():
    for event in pygame.event.get():
        mouse(event)
        keyboard(event)
