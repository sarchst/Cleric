import pygame
import user
import zone
import tile

class private:
    """
    Private attributes.
    """
    frames = 0

def render(screen, font):
    x = private.frames % 2
    screen.fill((0, 0, 0))
    # Editing Menu
    if user.public.editing:
        screen.blit(tile.sheets[user.public.sheet][x], (0, 0))
    # Game Map
    elif not user.public.editing:
        # Terrain
        for coord, thing in zone.public.terrain.iteritems():
            screen.blit(tile.sheets[thing.sheet][x],\
                tile.rect(coord), tile.rect(thing.tile))
        # Sprites
        for coord, thing in zone.public.sprites.iteritems():
            screen.blit(tile.sheets[thing.sheet][x],\
                tile.rect(coord), tile.rect(thing.tile))
    if user.public.saved:
        screen.blit(font.render("Saved!", 0, (255, 255, 0)), (0,0))
    pygame.display.flip()
    private.frames += 1
