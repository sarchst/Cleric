import operator
import pygame as pg
import cPickle as pickle

class Video:
    """
    For everything renderering related
    """
    def __init__(self, pixel_res):
        self.font = pg.font.Font("fonts/SDS_8x8.ttf", 8)
        self.renders = 0
        self.pixel_font_size = self.font.size(".")
        # Rendering layers, one for each chapter, where each chapter
        # is a dictionary with the format:
        # (x, y) : Tile
        # (x, y) is in tile format, not pixel format, such that one unique
        # tile tile element can be used per entry
        self.layers = [ {}, {}, {}, {}, {}, {} ]
        self.tile_size = (32, 32)
        self.pixel_res = pixel_res
        self.tile_res = self.to_tile(pixel_res)
        self.screen = pg.display.set_mode(pixel_res)
        self.entries = []
        # Location
        self.top_left = (0, 0)
        self.bottom_right = tuple(map(operator.sub, self.pixel_res, self.pixel_font_size))
        # Colors
        self.black = (0x00, 0x00, 0x00)
        self.yellow = (0xFF, 0xFF, 0x00)

    def to_tile(self, pixel):
        """
        Transforms a pixel tuple coordinate to a tile tile coordinate
        """
        return tuple(map(operator.div, pixel, self.tile_size))

    def to_pixel(self, tile):
        """
        Transforms a tile tuple coordinate to a pixel tile coordinate
        """
        return tuple(map(operator.mul, tile, self.tile_size))

    def clear_log(self):
        del self.entries[:]

    def snap(self, pixel):
        """
        Snaps a pixel coordinate to the tile:
        """
        tile = self.to_tile(pixel)
        return self.to_pixel(tile)

    def place(self, link, user):
        """
        Places a tile link in a video layer
        """
        map_tile_selected = self.to_tile(link.map_pixel_selected)
        map_tile = tuple(map(operator.sub, map_tile_selected, link.tile_offset))
        for x in range(map_tile[0] - (user.brush_size - 1), map_tile[0] + user.brush_size):
            for y in range(map_tile[1] - (user.brush_size - 1), map_tile[1] + user.brush_size):
                self.layers[link.chapter][(x,y)] = link

    def log(self, message):
        """
        Adds a message to the log.
        Pops the head of the log if the log is longer than the display
        """
        self.entries.append(message)
        if len(self.entries) * self.pixel_font_size[1] > self.pixel_res[1]:
            self.entries.pop(0)

    def save(self):
        """
        Saves the video layers to a pickle file
        """
        pickle.dump(self.layers, open("map", "wb"), protocol = pickle.HIGHEST_PROTOCOL)
        self.log("Saved!")

    def erase(self):
        """
        Kills all video layers
        """
        self.layers = [ {}, {}, {}, {}, {}, {} ]

    def load(self):
        """
        Loads the video layers from a pickle file
        """
        try:
            self.layers = pickle.load(open("map", "rb"))
        except:
            self.log("No map file found...")

    def blit_title_screen(self):
        """
        Blits title screen to display
        """
        text = self.font.render("Loading one massive world...", 0, self.yellow)
        self.screen.blit(text, self.top_left)

    def blit_log(self):
        """
        Blits the log to the screen
        """
        for line, entry in enumerate(self.entries):
            text = self.font.render(entry, 0, self.yellow)
            self.screen.blit(text, (0, line * self.pixel_font_size[1]))

    def blit_selector(self, user, catalog):
        """
        Buffers the mouse selector tile in the screen backbuffer
        """
        # The GUI page is the very last page of the catalog and pixel of
        # the selctor tile is at (10, 0) of the GUI page
        gui_page = catalog.pages[catalog.page_count - 1]
        selector_pixel = self.to_pixel((10, 0))
        selector_pixel_rect = (selector_pixel, self.tile_size)
        # The selector tile is blitted to the position of the cursor
        cursor_pixel = self.snap(user.cursor_pixel)
        self.screen.blit(gui_page, cursor_pixel, selector_pixel_rect)

    def blit_catalog(self, catalog, user):
        """
        Buffers a catalog page in the screen backbuffer
        """
        animation = self.renders % 2
        page = catalog.pages[catalog.page_number + animation]
        page_pixel_rect = ((0, user.page_scroll * self.pixel_res[1]), self.pixel_res)
        self.screen.blit(page, self.top_left, page_pixel_rect)
        # Displays the page scroll at the bottom right hand of the screen
        text = self.font.render(str(user.page_scroll), 0, self.yellow)
        self.screen.blit(text, self.bottom_right)

    def blit_layer(self, coord, catalog, tile):
        """
        Buffers one layer at screen coordinates in the screen backbuffer
        """
        for layer in self.layers:
            try:
                link = layer[tile]
            except:
                continue
            else:
                animation = self.renders % 2
                page = catalog.pages[link.page_number + animation]
                map_pixel = self.to_pixel(coord)
                cat_pixel_scroll = (0, link.page_scroll * self.pixel_res[1])
                cat_pixel = tuple(map(operator.add, link.cat_pixel_selected, cat_pixel_scroll))
                cat_pixel_rect = (self.snap(cat_pixel), self.tile_size)
                self.screen.blit(page, map_pixel, cat_pixel_rect)

    def blit_map(self, catalog, user):
        """
        Buffers the map in the screen backbuffer with catalog tiles
        """
        for x in range(0, self.tile_res[0]):
            for y in range(0, self.tile_res[1]):
                coord = (x, y)
                tile = tuple(map(operator.sub, coord, user.tile_offset))
                self.blit_layer(coord, catalog, tile)

    def blit_clear(self):
        """
        Buffers blackness to the screen backbuffer
        """
        self.screen.fill(self.black)

    def flip(self):
        """
        Transfers the screen backbuffer to the display
        """
        pg.display.flip()
        self.renders += 1

    def off(self):
        """
        Kills pygame
        """
        pg.quit()
