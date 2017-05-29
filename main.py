import pygame
import random

class Circle:
    def __init__(self, point):
        self.point = point
        self.size = 5
        self.color = (0, 255, 0)
        self.thickness = 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.point, self.size, self.thickness)


def main():
    xres = 640
    yres = 480
    # Game init
    screen = pygame.display.set_mode((xres, yres))
    pygame.display.set_caption("Cleric")
    screen.fill((0, 0, 0))
    # Game loop
    done = False
    while not done:
        # Game data
        x = random.randint(0, xres)
        y = random.randint(0, yres)
        point = (x, y)
        circle = Circle(point)
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
        circle.draw(screen)
        pygame.display.flip()
        pygame.time.wait(15)
    # Done
    pygame.quit()

# Run cleric
main()
