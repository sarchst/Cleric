import pygame
import tile

# Tile maps.
floor = pygame.transform.scale2x(pygame.image.load("Objects/Floor.png"))
cats  = pygame.transform.scale2x(pygame.image.load("Characters/Cat0.png"))
cats1 = pygame.transform.scale2x(pygame.image.load("Characters/Cat1.png"))
trees = pygame.transform.scale2x(pygame.image.load("Objects/Tree1.png"))

# Screen coordinates to tile map coordinates.
terrain = {
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

sprites = {
    (9,6):(1,1), (8,7):(1,2), (6,6):(2,2), (7,9):(2,1), (8,9):(1,3), (9,7):(2,3), (9,9):(2,0)
}

# Setup.
pygame.init()
screen = pygame.display.set_mode(tile.size((10, 10)))
pygame.display.set_caption("Cleric")

x = True

done = False
while not done:
    # Input.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print coordinates to terminal
            mx, my = pygame.mouse.get_pos()
            print "(" + str((mx/tile.width)) + "," + str((my/tile.width)) + ")"
            #place grass tile
            terrain[((mx/tile.width), (my/tile.width))] = (8,7)

    # Data.
    for key, value in terrain.iteritems():
        screen.blit(floor, tile.rect(key), tile.rect(value))

    if x:
        for key, value in sprites.iteritems():
            screen.blit(cats, tile.rect(key), tile.rect(value))
    else:
        for key, value in sprites.iteritems():
            screen.blit(cats1, tile.rect(key), tile.rect(value))
    x = not x

    # Output.
    pygame.display.flip()
    pygame.time.wait(16)

# Cleanup.
pygame.quit()
