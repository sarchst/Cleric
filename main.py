import pygame
import os

def tile((x, y)):
    """Returns a tile tuple from a pixel tuple"""
    return (x / 16, y / 16)

def pixel((x, y)):
    """Returns a pixel tuple from a tile tuple"""
    return (x * 16, y * 16)

def square((x, y)):
    """ """
    return (pixel((x, y)), (16, 16))

class Catalog:
    """Holds all tile art sheets by chapter"""
    def __init__(self):
        # All tile art sheets
        self.sheets = []
        # Number of sheets per chapter
        self.chapters = []
        # Load self on creation
        self.load()

    def load(self):
        """Populates catalog"""
        for dir in ["0", "1", "2", "3", "4", "5"]:
            for root, dirs, files in os.walk(dir):
                for file in sorted(files):
                    name = dir + "/" + file
                    sheet = pygame.image.load(name)
                    self.sheets.append(sheet)
            self.chapters.append(len(files))

    def bookmark(self, user):
        """Returns the chapter of the provided page"""
        if user.page < sum(self.chapters[:1]):
            return 0
        if user.page < sum(self.chapters[:2]):
            return 1
        if user.page < sum(self.chapters[:3]):
            return 2
        if user.page < sum(self.chapters[:4]):
            return 3
        if user.page < sum(self.chapters[:5]):
            return 4
        if user.page < sum(self.chapters[:6]):
            return 5


class World:
    """Holds all tile art placements"""
    def __init__(self):
        self.layers = [ {}, {}, {}, {}, {}, {} ]

    def place(self, user, catalog):
        if user.select is None:
            return
        chapter = catalog.bookmark(user)
        self.layers[chapter][user.select] = user.pick
        print self.layers

class User:
    """Handles keyboard and mouse input"""
    def __init__(self):
        # User is looking at tile art catalog
        self.catalogging = False
        # Art catalog page user is looking at
        self.page = 0
        # Tile art that user picked when looking at art catalog
        self.pick = (0, 0)
        # Location user clicked on the game map
        self.select = None
        # The user wants to stop playing
        self.done = False

    def mouse(self, event, catalog):
        """Handles all mouse events for the user"""
        if event.type == pygame.MOUSEBUTTONUP:
            click = pygame.mouse.get_pos()
            # Left mouse button
            if event.button == 1:
                if self.catalogging:
                    self.pick = tile(click)
                else:
                    self.select = tile(click)
                self.catalogging = False
            # Middle mouse button
            elif event.button == 2:
                pass
            # Right mouse button
            elif event.button == 3:
                self.catalogging = True
            # Scroll wheel up
            elif event.button == 4 and self.catalogging:
                self.page += 2
                if self.page >= len(catalog.sheets):
                    self.page = len(catalog.sheets) - 2
            # Scroll wheel down
            elif event.button == 5 and self.catalogging:
                self.page -= 2
                if self.page < 0:
                    self.page = 0
        else:
            self.select = None

    def keyboard(self, event):
        """Handles all keyboard events for the user"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_F1:
                self.done = True

    def input(self, catalog):
        """User did something with either the keyboard or mouse"""
        event = pygame.event.wait() # Waits here until user does something
        self.mouse(event, catalog)
        self.keyboard(event)

class Video:
    """Handles display updates"""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Cleric")
        pygame.font.init()
        self.screen = pygame.display.set_mode(pixel((40, 30)))
        self.font = pygame.font.Font("fonts/SDS_8x8.ttf", 16)

    def show_catalog(self, catalog, user):
        sheet = catalog.sheets[user.page]
        self.screen.blit(sheet, (0, 0))

    def show_game(self, catalog, user, world):
        for chapter in range(len(catalog.chapters)):
            layer = world.layers[chapter]
            for game_tile, catalog_tile in layer.iteritems():
                sheet = catalog.sheets[user.page]
                self.screen.blit(sheet, square(game_tile), square(catalog_tile))

    def render(self):
        pygame.display.flip()

    def wipe(self):
        self.screen.fill((0, 0, 0))

def main():
    # Setup
    video = Video()
    user = User()
    world = World()
    catalog = Catalog()
    # Loop
    while not user.done:
        video.wipe()
        user.input(catalog)
        world.place(user, catalog)
        if user.catalogging:
            video.show_catalog(catalog, user)
        else:
            video.show_game(catalog, user, world)

        video.render()
    # Cleanup
    pygame.quit()

"""Cleric"""
main()
