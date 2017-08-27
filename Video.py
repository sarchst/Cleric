import operator
import pygame as pg
import cPickle as pickle
import copy

class Video:
    """
    For everything renderering related
    """
    def __init__(self, pixel_res):
        self.font = pg.font.Font("fonts/SDS_8x8.ttf", 8)
        self.renders = 0
        self.layers = [ {}, {}, {}, {}, {}, {} ]
        # Tile size must remain constant - No other tile sizes are supported
        self.pixel_tile_size = (32, 32)
        self.pixel_res = pixel_res
        self.tile_res = self.to_tile(pixel_res)
        self.screen = pg.display.set_mode(pixel_res)
        self.entries = []
        # Location
        self.top_left = (0, 0)
        # Colors
        self.black = (0x00, 0x00, 0x00)
        self.yellow = (0xFF, 0xFF, 0x00)

    def to_tile(self, pixel):
        """
        Transforms a pixel tuple coordinate to a tile tile coordinate
        """
        return tuple(map(operator.div, pixel, self.pixel_tile_size))

    def to_pixel(self, tile):
        """
        Transforms a tile tuple coordinate to a pixel tile coordinate
        """
        return tuple(map(operator.mul, tile, self.pixel_tile_size))

    def clear_log(self):
        """
        Clears the display log history
        """
        del self.entries[:]

    def snap(self, pixel):
        """
        Snaps a pixel coordinate to the tile:
        """
        return self.to_pixel(self.to_tile(pixel))

    def place(self, link, user):
        """
        Places a tile link in a video layer
        """
        map_tile_selected = self.to_tile(link.map_pixel_selected)
        map_tile = tuple(map(operator.sub, map_tile_selected, link.tile_offset))
        for x in range(map_tile[0] - (user.brush_size - 1), map_tile[0] + user.brush_size):
            for y in range(map_tile[1] - (user.brush_size - 1), map_tile[1] + user.brush_size):
                self.layers[link.chapter][x, y] = link

    def is_black_tile(self, link, catalog):
        """
        Returns true if a link to the catalog is a black square
        """
        pixel_start = self.snap(link.cat_pixel_selected)
        x_max = self.pixel_tile_size[0]
        y_max = self.pixel_tile_size[1]
        for x in range(x_max):
            for y in range(y_max):
                pixel = tuple(map(operator.add, pixel_start, (x, y)))
                color = catalog.pages[link.page_number].get_at(pixel)
                if color[0] != 0x00 and color[1] != 0x00 and color[2] != 0x00:
                    return False
        return True

    def collect_garbage(self, catalog):
        """
        Black tile links can be placed to erase tiles,
        but will still affect collision detection during gameplay.
        This method removes all black tiles links
        """
        garbage_tiles = 0
        for layer in self.layers:
            mirror = copy.deepcopy(layer)
            for coord, link in mirror.iteritems():
                # Out of bounds black tile
                try:
                    pixel = catalog.pages[link.page_number].get_at(link.cat_pixel_selected)
                except:
                    garbage_tiles += 1
                    del layer[coord]
                # In bounds black tile
                else:
                    if self.is_black_tile(link, catalog):
                        garbage_tiles += 1
                        del layer[coord]
        self.log("%r garbage tiles removed" % garbage_tiles)

    def log(self, message):
        """
        Adds a message to the log.
        Pops the head of the log if the log is longer than the display.
        """
        self.entries.append(message)
        if len(self.entries) * self.font.size(".")[1] > self.pixel_res[1]:
            self.entries.pop(0)

    def query(self, user, catalog):
        """
        Logs catalog or game map tile attributes
        """
        if user.is_catalogging:
            pixel = tuple(map(operator.add,\
                user.cursor_pixel, (0, user.page_scroll * self.pixel_res[1])))
            self.log("tile %r" % (self.to_tile(pixel),))
        else:
            tile = tuple(map(operator.sub,\
                self.to_tile(user.cursor_pixel),\
                user.tile_offset))
            for layer in self.layers:
                try:
                    link = layer[tile]
                except:
                    pass
                else:
                    self.log("tile %r: page %3r: chapter %r" %
                        (self.to_tile(link.cat_pixel_selected), link.page_number, link.chapter))
            self.log("")

    def save(self, catalog):
        """
        Saves the video layers to a pickle file
        """
        self.collect_garbage(catalog);
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

    def blit_log(self):
        """
        Blits the log to the screen
        """
        for line, entry in enumerate(self.entries):
            text = self.font.render(entry, 0, self.yellow)
            self.screen.blit(text, (0, line * self.font.size(entry)[1]))

    def blit_selector(self, user, catalog):
        """
        Buffers the mouse selector tile in the screen backbuffer
        """
        # The GUI page is the very last page of the catalog and pixel of
        # the selctor tile is at (10, 0)
        gui_page = catalog.pages[catalog.page_count - 1]
        selector_pixel = self.to_pixel((10, 0))
        selector_pixel_rect = (selector_pixel, self.pixel_tile_size)
        # The selector tile is blitted to the position of the cursor.
        # A dragging effect will occur with selector as it technically is a sprte
        cursor_pixel = self.snap(user.cursor_pixel)
        self.screen.blit(gui_page, cursor_pixel, selector_pixel_rect)

    def blit_catalog(self, catalog, user):
        """
        Buffers a catalog page in the screen backbuffer
        """
        # Tile map portion
        animation = self.renders % 2
        page = catalog.pages[catalog.page_number + animation]
        pixel_offset = (0, user.page_scroll * self.pixel_res[1])
        page_pixel_rect = (pixel_offset, self.pixel_res)
        self.screen.blit(page, self.top_left, page_pixel_rect)
        # Page number and chapter
        message = "page %r: chapter %r" % (catalog.page_number, catalog.get_chapter())
        text = self.font.render(message, 0, self.yellow)
        bottom_right = tuple(map(operator.sub, self.pixel_res, self.font.size(message)))
        self.screen.blit(text, bottom_right)

    def blit_layers(self, coord, catalog, user):
        """
        Buffers one layer at screen coordinates in the screen backbuffer
        """
        tile = tuple(map(operator.sub, coord, user.tile_offset))
        for layer in self.layers:
            try:
                link = layer[tile]
            except:
                continue
            else:
                animation = self.renders % 2
                page = catalog.pages[link.page_number + animation]
                map_pixel = self.to_pixel(coord)
                cat_pixel_rect = (self.snap(link.cat_pixel_selected), self.pixel_tile_size)
                self.screen.blit(page, map_pixel, cat_pixel_rect)

    def blit_map(self, catalog, user):
        """
        Buffers the map in the screen backbuffer with catalog tiles
        """
        for x in range(0, self.tile_res[0]):
            for y in range(0, self.tile_res[1]):
                self.blit_layers((x, y), catalog, user)

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
