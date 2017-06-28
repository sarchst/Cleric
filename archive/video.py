import pygame
import user
import zone
import tile

class private:
    renders = 0

def render(screen, font):
    x = private.renders % 2
    screen.fill((0, 0, 0))
    # Editing Menu
    if user.public.editing:
        frame = tile.sheets[user.public.sheet][x]
        screen.blit(frame, (0, 0))
    # Game Map
    elif not user.public.editing:
        # Layers
        for index in range(zone.public.thickness):
            layer = zone.public.layers[index]
            for coord, thing in layer.iteritems():
                frame = tile.sheets[thing.sheet][x]
                screen.blit(frame, tile.rect(coord), tile.rect(thing.tile))
    # Saved text
    if user.public.saved:
        screen.blit(font.render("Saved!",\
            0, (255, 255, 0)), (0,0))
    # Editing screen sheet text
    if user.public.editing:
        screen.blit(font.render(str(user.public.sheet),\
            0, (255, 255, 0)), tile.pixel((21, 0)))
    pygame.display.flip()
    private.renders += 1
