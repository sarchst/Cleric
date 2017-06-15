import pygame
import tile
import zone

"""
Setup
"""
pygame.init()
screen = pygame.display.set_mode(tile.size((10, 10)))
pygame.display.set_caption("Cleric")

def getUserInput(editingScreen, done):
    global choice

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
	    done = True 
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Print coordinates to terminal.
            mx, my = pygame.mouse.get_pos()
            click = mx / tile.width, my / tile.width 
            print click
            if event.button == right:
                editingScreen = True
            elif event.button == left and editingScreen:
                choice = click
                editingScreen = False
            elif "choice" in globals() and not editingScreen:
                zone.sprites[click] = choice
            else:
                zone.terrain[click] = (8,7)
    return done, editingScreen

"""
Game loop
"""
# Frame rendered since game start.
frames = 0
# Frames per second to run the game loop.
fps = 60
# Renders one frame every loop.

done = False
left = 1
right = 3
editingScreen = False

while not done:

    done, editingScreen = getUserInput(editingScreen, done)

    """
    Data
    """

    # The frame animation to select - will be either 0 or 1. Changes every half second.
    x = (frames / fps) % 2

    # Cat Menu
    if editingScreen:
        screen.fill((0,0,0))
        screen.blit(tile.cats[x], (0,0))
    # Terrain.
    elif not editingScreen:
        for key, value in zone.terrain.iteritems():
            screen.blit(tile.floor[x], tile.rect(key), tile.rect(value))
    # Sprites.
        for key, value in zone.sprites.iteritems():
            screen.blit(tile.cats[x], tile.rect(key), tile.rect(value))

    """
    Output
    """
    pygame.display.flip()
    pygame.time.wait(1000 / fps)

    # Onto the next frame.
    frames = frames + 1

"""
Cleanup
"""
pygame.quit()
