import pygame
import user
import zone
import tile

def render(screen, frames, fps, font):
    x = (frames / (fps / 2)) % 2
    screen.fill((0, 0, 0))
    # Editing Menu
    if user.public.editing:
        screen.blit(tile.sheets[user.public.sheet][x], (0, 0))
    # Game Map
    elif not user.public.editing:
        # Terrain
        for coord, thing in zone.terrain.iteritems():
            screen.blit(tile.sheets[thing.sheet][x], tile.rect(coord), tile.rect(thing.tile))
        # Sprites
        for coord, thing in zone.sprites.iteritems():
            screen.blit(tile.sheets[thing.sheet][x], tile.rect(coord), tile.rect(thing.tile))
    if user.public.saved:
        screen.blit(font.render("Saved!", 0, (255, 255, 0)), (0,0))
    pygame.display.flip()
    pygame.time.wait(1000 / fps)
