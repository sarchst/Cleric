import os
import pygame

class User:
    def __init__(self):
        # The scroll wheel value
        self.scroll_wheel = 0
        # The selected pixel of the game map
        self.map_pixel_selected = None
        # The selected pixel of the catalog
        self.cat_pixel_selected = None
        # The current pixel of the mouse
        self.cursor_pixel = None
        # The user is on the catalog page
        self.is_catalogging = False
        # The user is done playing the game
        self.is_done = False

    def serve_keyboard(self, event):
        # The user pushed 'X' to close the window
        if event.type == pygame.QUIT:
            self.is_done = True
        # The user pushed F1 wanting to quit.
        # Could use escape, but breaks pygame
        # if escape and caps lock are reversed
        if event.key == pygame.K_F1:
            self.is_done = True
        # Example key press for future reference
        if event.key == pygame.K_a:
            pass

    def serve_mouse(self, event):
        # The selected map pixel must stay None if no event
        # occured. The catalog selection must be persistent
        # and should be set to None
        self.map_pixel_selected = None
        # Left mouse button was pressed
        if event.button == 1:
            if self.is_catalogging:
                self.cat_pixel_selected = self.cursor_pixel
                self.is_catalogging = False
            else:
                self.map_pixel_selected = self.cursor_pixel
        # Middle mouse button was pressed
        if event.button == 2:
            pass
        # Right mouse button was pressed
        if event.button == 3:
            self.is_catalogging = True
        # Scroll wheel up was pressed
        if event.button == 4:
            if self.is_catalogging:
                self.scroll_wheel += 1
        # Scroll wheel down was pressed
        if event.button == 5:
            if self.is_catalogging:
                self.scroll_wheel -= 1

    def get_input(self):
        # Wait here until any event occurs
        event = pygame.event.wait()
        # A full screen render will occur everytime the
        # mouse is moved, and that will kill the poor little CPU,
        # so wait for a key press or mouse press event
        while event.type not in [pygame.MOUSEBUTTONUP, pygame.KEYUP]:
            event = pygame.event.wait()
        # Now service the mouse press event
        self.cursor_pixel = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            self.serve_mouse(event)
        # ...Or the key press event
        if event.type == pygame.KEYUP:
            self.serve_keyboard(event)

class Catalog:
    def __init__(self):
        self.page_number = 0
        self.pages = []
        self.page_count = 0
        self.chapter_size = []
        self.chapters = [0, 1, 2, 3, 4, 5]
        self.animations_per_tile = 2

    def load(self, root):
        for chapter in self.chapters:
            parent = root + "/" + str(chapter)
            imgs = sorted(os.listdir(parent))
            for img in imgs:
                page = pygame.image.load(parent + "/" + img)
                self.pages.append(page)
            self.chapter_size.append(len(imgs))
            self.page_count = len(self.pages)

    def get_chapter(self):
        for chapter in self.chapters:
            if self.page_number < sum(self.chapter_size[:chapter + 1]):
                return chapter
        return None

    def bound(self, user):
        self.page_number = self.animations_per_tile * user.scroll_wheel
        # Upper bound
        if self.page_number >= self.page_count:
            self.page_number = self.page_count - self.animations_per_tile
        # Lower bound
        if self.page_number < 0:
            self.page_number = 0
        # Force scroll wheel into place
        user.scroll_wheel = self.page_number / self.animations_per_tile


class Link:
    def __init__(self, user, catalog):
        self.cat_pixel_selected = user.cat_pixel_selected
        self.map_pixel_selected = user.map_pixel_selected
        self.page_number = catalog.page_number
        self.chapter = catalog.get_chapter()

class Video:
    def __init__(self, res):
        self.screen = pygame.display.set_mode(res)
        self.layers = [ {}, {}, {}, {}, {}, {} ]
        self.tile_width = 16
        self.tile_size = (self.tile_width, self.tile_width)
        # Margins
        self.top_left = (0, 0)
        # Colors
        self.black = (0, 0, 0)

    def to_tile(self, pixel):
        return tuple(int(i / self.tile_width) for i in pixel)

    def to_pixel(self, tile):
        return tuple(int(i * self.tile_width) for i in tile)

    def snap(self, pixel):
        tile = self.to_tile(pixel)
        return self.to_pixel(tile)

    def create(self, link):
        map_tile = self.to_tile(link.map_pixel_selected)
        self.layers[link.chapter][map_tile] = link

    def save(self):
        pass

    def load(self):
        pass

    def flip(self):
        pygame.display.flip()

    def wipe(self):
        self.screen.fill(self.black)

    def blit_selector(self, user, catalog):
        # The GUI page is the very last page of the catalog
        gui_page = catalog.pages[catalog.page_count - 1]
        # The pixel of the selctor tile is at (10, 0) of the GUI page
        selector_pixel = self.to_pixel((10, 0))
        selector_pixel_rect = (selector_pixel, self.tile_size)
        # The selector tile is blitted to the position of the cursor
        cursor_pixel = self.snap(user.cursor_pixel)
        self.screen.blit(gui_page, cursor_pixel, selector_pixel_rect)

    def blit_catalog(self, catalog):
        page = catalog.pages[catalog.page_number]
        self.screen.blit(page, self.top_left)

    def blit_map(self, catalog):
        for layer in self.layers:
            for tile in layer:
                link = layer[tile]
                page = catalog.pages[link.page_number]
                map_pixel_rect = (self.snap(link.map_pixel_selected), self.tile_size)
                cat_pixel_rect = (self.snap(link.cat_pixel_selected), self.tile_size)
                self.screen.blit(page, map_pixel_rect, cat_pixel_rect)

def main():
    pygame.init()
    pygame.display.set_caption("Cleric")
    video = Video((640, 480))
    catalog = Catalog()
    catalog.load("dawnlike")
    user = User()
    while not user.is_done:
        user.get_input()
        catalog.bound(user)
        video.wipe()
        if user.map_pixel_selected and user.cat_pixel_selected:
            video.create(Link(user, catalog))
        if user.is_catalogging:
            video.blit_catalog(catalog)
        else:
            video.blit_map(catalog)
        video.blit_selector(user, catalog)
        video.flip()
    pygame.quit()

main()
