import pygame

# Our libraries.
import tile

# Tile map.
# Loads a tile map and doubles size from native 16x16 to 32x32.
floor = pygame.image.load("Objects/Floor.png")
floor = pygame.transform.scale2x(floor)

cats = pygame.transform.scale2x(pygame.image.load("Characters/Cat0.png"))
trees = pygame.transform.scale2x(pygame.image.load("Objects/Tree1.png"))

# World tiles are represented as a dictionary of tuples.
# The dictionary maps the screen coordinate to the tile map coordinate.
world = {
    (0,0):(8,7), (1,0):(8,7), (2,0):(3,4), (3,0):(8,7), (4,0):(8,7), (5,0):(8,7), (6,0):(8,7), (7,0):(9,7), (8,0):(14,19), (9,0):(15,19),
    (0,1):(8,7), (1,1):(8,7), (2,1):(3,4), (3,1):(8,7), (4,1):(8,7), (5,1):(8,7), (6,1):(8,7), (7,1):(9,7), (8,1):(14,20), (9,1):(15,20),
    (0,2):(8,7), (1,2):(8,7), (2,2):(3,4), (3,2):(8,7), (4,2):(8,7), (5,2):(8,7), (6,2):(8,7), (7,2):(8,7), (8,2):(8,6), (9,2):(8,6),
    (0,3):(8,7), (1,3):(8,7), (2,3):(3,4), (3,3):(8,7), (4,3):(8,7), (5,3):(8,7), (6,3):(8,7), (7,3):(8,7), (8,3):(8,7), (9,3):(8,7),
    (0,4):(8,7), (1,4):(8,7), (2,4):(3,4), (3,4):(8,7), (4,4):(8,7), (5,4):(8,7), (6,4):(8,7), (7,4):(8,7), (8,4):(8,7), (9,4):(8,7),
    (0,5):(8,7), (1,5):(8,7), (2,5):(3,4), (3,5):(8,7), (4,5):(8,7), (5,5):(8,7), (6,5):(7,15), (7,5):(8,15), (8,5):(8,15), (9,5):(9,15),
    (0,6):(8,7), (1,6):(8,7), (2,6):(3,4), (3,6):(8,7), (4,6):(8,7), (5,6):(10,15), (6,6):(7,16), (7,6):(8,16), (8,6):(8,16), (9,6):(9,16),
    (0,7):(8,7), (1,7):(8,7), (2,7):(0,5), (3,7):(5,4), (4,7):(5,4), (5,7):(9,16), (6,7):(7,16), (7,7):(8,16), (8,7):(8,16), (9,7):(9,16),
    (0,8):(8,7), (1,8):(8,7), (2,8):(8,7), (3,8):(8,7), (4,8):(8,7), (5,8):(10,17), (6,8):(7,16), (7,8):(8,16), (8,8):(8,16), (9,8):(9,16),
    (0,9):(8,7), (1,9):(8,7), (2,9):(8,7), (3,9):(8,7), (4,9):(8,7), (5,9):(8,7), (6,9):(7,17), (7,9):(8,17), (8,9):(8,17), (9,9):(9,17),
}
# Setup.
# The world is a 3x3 grid of tiles.
# The screen size must be the same.
pygame.init()
screen = pygame.display.set_mode(tile.size((10, 10)))
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print (mx/32), (my/32)

    # Data.
    for key, value in world.iteritems():
        screen.blit(floor, tile.rect(key), tile.rect(value))

    screen.blit(cats,tile.rect((9,6)), tile.rect((1,1)))
    screen.blit(cats,tile.rect((8,7)), tile.rect((1,2)))
    screen.blit(cats,tile.rect((6,6)), tile.rect((2,2)))
    screen.blit(cats,tile.rect((7,9)), tile.rect((2,1)))
    screen.blit(cats,tile.rect((8,9)), tile.rect((1,3)))
    screen.blit(cats,tile.rect((9,7)), tile.rect((2,3)))
    screen.blit(cats,tile.rect((9,9)), tile.rect((2,0)))

    screen.blit(trees, tile.rect((0,0)), tile.rect((0,3)))
    screen.blit(trees, tile.rect((1,0)), tile.rect((0,3)))
    screen.blit(trees, tile.rect((3,0)), tile.rect((0,3)))
    screen.blit(trees, tile.rect((4,0)), tile.rect((0,3)))
    screen.blit(trees, tile.rect((3,1)), tile.rect((0,3)))
    screen.blit(trees, tile.rect((1,1)), tile.rect((0,3)))
    screen.blit(trees, tile.rect((3,1)), tile.rect((0,3)))

    # Output.
    pygame.display.flip()
    pygame.time.wait(16)


# End.
pygame.quit()
