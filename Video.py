import operator
import pygame
import cPickle as pickle # So much faster!

class Video:
    def __init__(self, pixel_res):
        pygame.init()
        pygame.display.set_caption("Cleric")
        self.renders = 0
        # Rendering layers, one for each chapter, where each chapter
        # is a dictionary with the format:
        # (x, y) : Tile
        # (x, y) is in tile format, not pixel format, such that one unique
        # tile tile element can be used per entry
        self.layers = [ {}, {}, {}, {}, {}, {} ]
        self.tile_width = 16
        self.tile_size = (self.tile_width, self.tile_width)
        self.top_left = (0, 0)
        self.black = (0x00, 0x00, 0x00)
        self.pixel_res = pixel_res
        self.tile_res = self.to_tile(pixel_res)
        self.screen = pygame.display.set_mode(pixel_res)

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
        # Sarch Step:
        # Condense this by removing all if statements
        # and using a single x and y for loop
        # 1x1
        if user.brush_size == 1:
            self.layers[link.chapter][map_tile] = link
        # 3x3
        if user.brush_size == 2:
            for x in range(map_tile[0] - 1, map_tile[0] + 2):
	            for y in range(map_tile[1] - 1, map_tile[1] + 2):
	                self.layers[link.chapter][(x,y)] = link
        # 5x5
        if user.brush_size == 3:
            for x in range(map_tile[0] - 2, map_tile[0] + 3):
	            for y in range(map_tile[1] - 2, map_tile[1] + 3):
	                self.layers[link.chapter][(x,y)] = link
        # 7x7 
        if user.brush_size == 4:
            for x in range(map_tile[0] - 3, map_tile[0] + 4):
	            for y in range(map_tile[1] - 3, map_tile[1] + 4):
	                self.layers[link.chapter][(x,y)] = link
        # 9x9
        if user.brush_size == 5:
            for x in range(map_tile[0] - 4, map_tile[0] + 5):
	            for y in range(map_tile[1] - 4, map_tile[1] + 5):
	                self.layers[link.chapter][(x,y)] = link
        # 11x11
        if user.brush_size == 6:
            for x in range(map_tile[0] - 5, map_tile[0] + 6):
	            for y in range(map_tile[1] - 5, map_tile[1] + 6):
	                self.layers[link.chapter][(x,y)] = link

    def save(self):
        """
        Saves the video layers to a pickle file
        """
        pickle.dump(self.layers, open("map", "wb"))

    def load(self):
        """
        Loads the video layers from a pickle file
        """
        return pickle.load(open("map", "rb"))

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

    def blit_catalog(self, catalog):
        """
        Buffers a catalog page in the screen backbuffer
        """
        page = catalog.pages[catalog.page_number]
        self.screen.blit(page, self.top_left)

    def blit_map(self, catalog, user):
        """
        Buffers the map in the screen backbuffer with catalog tiles
        NOTE:
        Highly inneffecient! Blits off screen tiles. If map is huge
        this will really kill performance!
        """
        animation = self.renders % 2
        for layer in self.layers:
            for tile in layer:
                link = layer[tile]
                camera = tuple(map(operator.add, tile, user.tile_offset))
                page = catalog.pages[link.page_number + animation]
                map_pixel_rect = self.to_pixel(camera)
                cat_pixel_rect = (self.snap(link.cat_pixel_selected), self.tile_size)
                self.screen.blit(page, map_pixel_rect, cat_pixel_rect)

    def blit_clear(self):
        """
        Buffers blackness to the screen backbuffer
        """
        self.screen.fill(self.black)

    def flip(self):
        """
        Transfers the screen backbuffer to the display
        """
        pygame.display.flip()
        self.renders += 1

    def off(self):
        pygame.quit()