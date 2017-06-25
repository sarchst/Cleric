import pygame
import tile
import zone
import user
import video

def main():
    """Setup"""
    pygame.init()
    screen = pygame.display.set_mode(tile.pixel((40, 30)))
    pygame.display.set_caption("Cleric")
    zone.load("Zones/home")
    """Game Loop"""
    frames = 0
    while not user.done:
        """Input"""
        user.input()
        """Data"""
        zone.update()
        """Video"""
        video.render(screen, frames, 60)
        frames = frames + 1
    """Cleanup"""
    pygame.quit()

"""Cleric"""
main()
