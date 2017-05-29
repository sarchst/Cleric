import pygame
import random

def main():
    xres = 640
    yres = 480
    black = (0x00, 0x00, 0x00)
    green = (0x00, 0xFF, 0x00)
    # Game init
    screen = pygame.display.set_mode((xres, yres))
    pygame.display.set_caption("Cleric")
    screen.fill(black)
    # Game loop
    done = False
    while not done:
        # Key input
        for event in pygame.event.get():
            # User pushed window X
            if event.type == pygame.QUIT:
                done = True
            # User pushed F1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_F1:
                    done = True
        # Renderer
        x = random.randint(0, xres)
        y = random.randint(0, yres)
        point = (x, y)
        pygame.draw.circle(screen, green, point, 5, 1)
        pygame.display.flip()
        pygame.time.wait(15)
    # Done
    pygame.quit()

# Run cleric
main()
