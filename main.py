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
    pygame.font.init()
    font = pygame.font.Font("Fonts/alterebro-pixel-font.ttf", 32)
    zone.load("Zones/home")
    """Game Loop"""
    frames = 0
    while not user.done:
        """Input"""
        user.input()
        """Data"""
        zone.update()
        """Video"""
        video.render(screen, frames, 60, font)
        frames = frames + 1
    """Cleanup"""
    pygame.quit()

"""Cleric"""
main()
