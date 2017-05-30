import pygame

# Our libraries.
import tile

# Tile map.
# Loads a tile map and doubles size from native 16x16 to 32x32.
floor = pygame.image.load("Objects/Floor.png")
floor = pygame.transform.scale2x(floor)
# World tiles are represented as a dictionary of tuples.
# The dictionary maps the screen coordinate to the tile map coordinate.
world = {
    (0,0):(0,3), (1,0):(1,3), (2,0):(2,3),
    (0,1):(0,4), (1,1):(1,4), (2,1):(2,4),
    (0,2):(0,5), (1,2):(1,5), (2,2):(2,5),
}
# Setup.
# The world is a 3x3 grid of tiles.
# The screen size must be the same.
pygame.init()
screen = pygame.display.set_mode(tile.size((3, 3)))
pygame.display.set_caption("Cleric")
# Game loop.
# Consists of three stages: Input, Data, and Output.
# Input, from the keyboard or mouse, manipulates game Data.
# Game Data manipulates the display and/or audio - the Output.
# The entire game loop is done in 60 frames per second.
# 60 FPS is fairly appealing to the human senses, and also CPU friendly.
done = False
while not done:
    # Input.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # Data.
    for key, value in world.iteritems():
        screen.blit(floor, tile.rect(key), tile.rect(value))
    # Output.
    pygame.display.flip()
    pygame.time.wait(16)
# End.
pygame.quit()
