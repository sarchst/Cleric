import pygame
import tile
import zone
import user

def render(screen, frames, fps):
    x = (frames / (fps / 2)) % 2
    # Cat Menu.
    if user.editingScreen:
        screen.fill((0, 0, 0))
        screen.blit(tile.cats[x], (0, 0))
    # Game Map.
    elif not user.editingScreen:
        # Terrain.
        for key, value in zone.terrain.iteritems():
            screen.blit(tile.floor[x], tile.rect(key), tile.rect(value))
        # Sprites.
        for key, value in zone.sprites.iteritems():
            screen.blit(tile.cats[x], tile.rect(key), tile.rect(value))
    pygame.display.flip()
    pygame.time.wait(1000 / fps)

def main():
    """
    Setup
    """
    pygame.init()
    screen = pygame.display.set_mode(tile.pixel((10, 10)))
    pygame.display.set_caption("Cleric")
    """
    Game loop
    """
    frames = 0
    while not user.done:
        """
        Input
        """
        user.getInput()
        """
        Data
        """
        if not user.editingScreen and user.select:
            zone.sprites[user.select] = user.choice
        """
        Output
        """
        render(screen, frames, 60)
        frames = frames + 1
    """
    Cleanup
    """
    pygame.quit()

"""
Cleric
  A game about... nothing yet, really. We're still deciding that.
"""
main()
