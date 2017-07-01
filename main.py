import os
import pygame

class User:
    def __init__(self):
        self.scroll_wheel = 0
        self.map_pixel = None
        self.cat_pixel = None
        self.cursor_pixel = None
        self.catalogging = False
        self.done = False

    def clamp(self, catalog):
        # Upper bounds
        if self.scroll_wheel >= catalog.page_count:
            self.scroll_wheel = catalog.page_count - catalog.animations_per_tile
        # Lower bounds
        if self.scroll_wheel < 0:
            self.scroll_wheel = 0

    def serve_keyboard(self, event):
        if event.key == pygame.K_F1:
            self.done = True
        # Example key press
        if event.key == pygame.K_a:
            pass

    def serve_mouse_buttons(self, event, catalog):
        self.map_pixel = None
        # Left mouse button
        if event.button == 1:
            if self.catalogging:
                self.cat_pixel = self.cursor_pixel
                self.catalogging = False
            else:
                self.map_pixel= self.cursor_pixel
        # Middle mouse button
        if event.button == 2:
            pass
        # Right mouse button
        if event.button == 3:
            self.catalogging = True
        # Scroll wheel up
        if event.button == 4:
            if self.catalogging:
                self.scroll_wheel += catalog.animations_per_tile
                self.clamp(catalog)
        # Scroll wheel down
        if event.button == 5:
            if self.catalogging:
                self.scroll_wheel -= catalog.animations_per_tile
                self.clamp(catalog)

    def get_input(self, catalog):
        # Wait here until any keyboard or mouse event occurs
        event = pygame.event.wait()
        # Try again if the event was a mouse move event
        # otherwise a full screen render will occur everytime the
        # mouse is moved, and that will kill the poor little CPU
        while event.type == pygame.MOUSEMOTION:
            event = pygame.event.wait()
        self.cursor_pixel = pygame.mouse.get_pos()
        # Now service the mouse and keyboard
        if event.type == pygame.QUIT:
            self.done = False
        if event.type == pygame.MOUSEBUTTONUP:
            self.serve_mouse_buttons(event, catalog)
        if event.type == pygame.KEYUP:
            self.serve_keyboard(event)

class Catalog:
    def __init__(self):
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

    def get_chapter(self, page_number):
        for chapter in self.chapters:
            if page_number < sum(self.chapter_size[:chapter + 1]):
                return chapter
        return None

class Link:
    def __init__(self, user, catalog):
        self.cat_pixel = user.cat_pixel
        self.map_pixel = user.map_pixel
        self.page_number = user.scroll_wheel
        self.chapter = catalog.get_chapter(self.page_number)

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
        map_tile = self.to_tile(link.map_pixel)
        self.layers[link.chapter][map_tile] = link

    def save(self):
        pass

    def load(self):
        pass

    def update(self):
        pygame.display.flip()

    def wipe(self):
        self.screen.fill(self.black)

    def buffer_highlighter(self, user, catalog):
        gui_page = catalog.pages[catalog.page_count - 1]
        highlighter_pixel = self.to_pixel((10, 0))
        highlighter_pixel_rect = (highlighter_pixel, self.tile_size)
        cursor_pixel_rect = self.snap(user.cursor_pixel)
        self.screen.blit(gui_page, cursor_pixel_rect, highlighter_pixel_rect)

    def buffer_catalog(self, user, catalog):
        page = catalog.pages[user.scroll_wheel]
        self.screen.blit(page, self.top_left)

    def buffer_map(self, catalog):
        for layer in self.layers:
            for tile in layer:
                link = layer[tile]
                page = catalog.pages[link.page_number]
                map_pixel_rect = (self.snap(link.map_pixel), self.tile_size)
                cat_pixel_rect = (self.snap(link.cat_pixel), self.tile_size)
                self.screen.blit(page, map_pixel_rect, cat_pixel_rect)

def main():
    pygame.init()
    pygame.display.set_caption("Cleric")
    video = Video((640, 480))
    catalog = Catalog()
    catalog.load("dawnlike")
    user = User()
    while not user.done:
        user.get_input(catalog)
        video.wipe()
        if user.map_pixel and user.cat_pixel:
            video.create(Link(user, catalog))
        if user.catalogging:
            video.buffer_catalog(user, catalog)
        else:
            video.buffer_map(catalog)
        video.buffer_highlighter(user, catalog)
        video.update()
    pygame.quit()

main()
