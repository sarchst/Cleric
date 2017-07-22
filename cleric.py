import os, pygame, operator, pickle


class User:
    def __init__(self):
        # The scroll wheel value
        self.scroll_wheel = 0
        # The selected (x, y) pixel of the game map
        self.map_pixel_selected = None
        # The selected (x, y) pixel of the catalog
        self.cat_pixel_selected = None
        # The current (x, y) pixel of the mouse
        self.cursor_pixel = None
        # The user is on the catalog page
        self.is_catalogging = False
        # The user is done playing the game
        self.is_done = False
        # The current camera (x, y) tile position
        self.tile_offset = (0, 0)
        # The tile offset pan with WASD
        self.tile_pan = 5

        self.brush_size = 1

        self.is_saving = False 

    def serve_keyboard(self, event):
        # The user pushed 'X' to close the window
        if event.type == pygame.QUIT:
            self.is_done = True
        # The user pushed F1 wanting to quit.
        # Could use escape, but breaks pygame
        # if escape and caps lock are reversed
        if event.key == pygame.K_F1:
            self.is_done = True
        # Camera tile movement controls
        # Up
        if event.key == pygame.K_w:
            self.tile_offset = tuple(map(operator.add,
                self.tile_offset, (0, self.tile_pan)))
        # Left
        if event.key == pygame.K_a:
            self.tile_offset = tuple(map(operator.add,
                self.tile_offset, (self.tile_pan, 0)))
        # Right
        if event.key == pygame.K_d:
            self.tile_offset = tuple(map(operator.sub,
                self.tile_offset, (self.tile_pan, 0)))
        # Down
        if event.key == pygame.K_s:
            self.tile_offset = tuple(map(operator.sub,
                self.tile_offset, (0, self.tile_pan)))

        # 1 key press: 1x1 brush size
        if event.key == pygame.K_1:
            self.brush_size = 1
        # 2 key press: 3x3 brush size
        if event.key == pygame.K_2:
            self.brush_size = 2
        # 3 key press: 5x5 brush size
        if event.key == pygame.K_3:
            self.brush_size = 3
        # 4 key press: 7x7 brush size
        if event.key == pygame.K_4:
            self.brush_size = 4

        if event.key == pygame.K_F5:
            self.is_saving = True 

    def serve_mouse(self, event):
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
        """
        Waits here until any mouse button (on the upstroke)
        or the keyboard button event occurs (on the downstroke)
        """
        # A full screen render will occur everytime the
        # mouse is moved, and that will kill the poor little CPU,
        # so wait for a key press or mouse press event
        events = [
            pygame.MOUSEBUTTONDOWN,
            pygame.MOUSEBUTTONUP,
            pygame.KEYDOWN
        ]
        event = pygame.event.wait()
        while event.type not in events:
            event = pygame.event.wait()
        # The selected map pixel must stay None if no event
        # occured. The catalog selection must be persistent
        # and should be set to None
        self.map_pixel_selected = None
        # Now service the mouse press event only on the upstroke
        self.cursor_pixel = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            self.serve_mouse(event)
        # ...Or the key press event only on a down stroke
        if event.type == pygame.KEYDOWN:
            self.serve_keyboard(event)

class Catalog:
    def __init__(self):
        # The current page number of the catalog
        self.page_number = 0
        # All images loaded into a list
        self.pages = []
        # The number of pages in the catalog
        self.page_count = 0
        # The number of pages in each chapter
        self.pages_per_chapter = []
        # Available chapters
        self.chapters = [0, 1, 2, 3, 4, 5]
        # The number of pages needed to animate a tile
        self.pages_per_animation = 2

    def load(self, root):
        """
        Loads the catalog from file. The catalog is divided into chapters.
        The higher the chapter, the higher the importance of render.
        For instance:
        Chapter 0: Terrain
        Chatper 1: Rocks / Leaves
        Chapter 2: Characters
        ...
        Chapter 5: GUI
        Rocks will always be rendered over terrain, characters always
        over rocks, and the GUI always over everything.
        """
        for chapter in self.chapters:
            parent = root + "/" + str(chapter)
            imgs = sorted(os.listdir(parent))
            for img in imgs:
                page = pygame.image.load(parent + "/" + img)
                self.pages.append(page)
            self.pages_per_chapter.append(len(imgs))
        self.page_count = len(self.pages)

    def get_chapter(self):
        """
        Returns the chapter of the current catalog page
        """
        for chapter in self.chapters:
            if self.page_number < sum(self.pages_per_chapter[:chapter + 1]):
                return chapter
        return None

    def bound(self, user):
        """
        Sets the catalog page to that of the mouse scroll index.
        Forces the mouse scroll index back into place if it
        exceeds the number of pages of the catalog, or if it less than 0
        """
        self.page_number = self.pages_per_animation * user.scroll_wheel
        # Upper bound
        if self.page_number >= self.page_count:
            self.page_number = self.page_count - self.pages_per_animation
        # Lower bound
        if self.page_number < 0:
            self.page_number = 0
        # Force scroll wheel into place
        user.scroll_wheel = self.page_number / self.pages_per_animation


class Link:
    """
    Contains the relevant information needed to link a catalog
    tile to a video layer. Chapter to video layer links are one to one,
    that is:
    Chapter 0 == Layer 0
    Chapter 1 == Layer 1
    Chapter 2 == Layer 2
    ...
    Chapter 5 == Layer 5 
    """
    def __init__(self, user, catalog):
        # The selected catalog pixel
        self.cat_pixel_selected = user.cat_pixel_selected
        # The selected map pixel
        self.map_pixel_selected = user.map_pixel_selected
        # The page number of the catalog
        self.page_number = catalog.page_number
        # The chapter of the catalog
        self.chapter = catalog.get_chapter()
        # The tile offset of the camera at placement
        self.tile_offset = user.tile_offset

        self.brush_size = user.brush_size

class Video:
    def __init__(self, pixel_res):
        # Number of frame renders since game start
        self.renders = 0
        # Rendering layers, one for each chapter, where each chapter
        # is a dictionary with the format:
        # (x, y) : Tile
        # (x, y) is in tile format, not pixel format, such that one unique
        # tile tile element can be used per entry
        self.layers = [ {}, {}, {}, {}, {}, {} ]
        # Tile width and size - required for pixel to tile transformations
        self.tile_width = 16
        self.tile_size = (self.tile_width, self.tile_width)
        # Screen margins
        self.top_left = (0, 0)
        # Screen colors
        self.black = (0x00, 0x00, 0x00)
        # Screen pixel resolution
        self.pixel_res = pixel_res
        # Screen tile resolution
        self.tile_res = self.to_tile(pixel_res)
        # Screen init
        self.screen = pygame.display.set_mode(pixel_res)


    def to_tile(self, pixel):
        """
        Transforms a pixel tuple coordinate to a tile tile coordinate
        eg: (70, 33) -> (4, 2)
        """
        return tuple(map(operator.div, pixel, self.tile_size))

    def to_pixel(self, tile):
        """
        Transforms a tile tuple coordinate to a pixel tile coordinate
        eg: (4, 2) -> (64, 32)
        """
        return tuple(map(operator.mul, tile, self.tile_size))

    def snap(self, pixel):
        """
        Snaps a pixel coordinate to the tile:
        eg: (70, 33) -> (4, 2) -> (64, 32)
        """
        tile = self.to_tile(pixel)
        return self.to_pixel(tile)

    def place(self, link, user):
        """
        Places a tile link in a video layer
        """
        map_tile_selected = self.to_tile(link.map_pixel_selected)
        map_tile = tuple(map(operator.sub, map_tile_selected, link.tile_offset))

        #1x1 
        if user.brush_size == 1:
            self.layers[link.chapter][map_tile] = link
        #3x3
        if user.brush_size == 2:
            for x in range(map_tile[0] - 1, map_tile[0] + 2):
	            for y in range(map_tile[1] - 1, map_tile[1] + 2):
	                self.layers[link.chapter][(x,y)] = link
        #5x5
        if user.brush_size == 3:
            for x in range(map_tile[0] - 2, map_tile[0] + 3):
	            for y in range(map_tile[1] - 2, map_tile[1] + 3):
	                self.layers[link.chapter][(x,y)] = link
        #7x7 
        if user.brush_size == 4:
            for x in range(map_tile[0] - 3, map_tile[0] + 4):
	            for y in range(map_tile[1] - 3, map_tile[1] + 4):
	                self.layers[link.chapter][(x,y)] = link

    def save(self, user):
        """
        Saves the video layers to a pickle file
        """
        if user.is_saving:
            pickle.dump(self.layers, open("map", "w")) 
            user.is_saving = False           

    def load(self):
        """
        Loads the video layers from a pickle file
        """
        return pickle.load(open("map", "r")) 

    def blit_selector(self, user, catalog):
        """
        Buffers the mouse selector tile in the screen backbuffer
        """
        # The GUI page is the very last page of the catalog
        gui_page = catalog.pages[catalog.page_count - 1]
        # The pixel of the selctor tile is at (10, 0) of the GUI page
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

def cleric():
    """
    Copyright (c) Sarchen Starke, Gustav Louw
    """
    # Game setup
    pygame.init()
    pygame.display.set_caption("Cleric")
    video = Video((640, 480))
    video.layers = video.load()
    catalog = Catalog()
    catalog.load("dawnlike")
    user = User()
    # Game loop
    while not user.is_done:
        # Input
        user.get_input()
        video.save(user)
        catalog.bound(user)
        # Render
        video.blit_clear()
        if user.map_pixel_selected and user.cat_pixel_selected:
            video.place(Link(user, catalog), user)
        if user.is_catalogging:
            video.blit_catalog(catalog)
        else:
            video.blit_map(catalog, user)
        video.blit_selector(user, catalog)
        video.flip()
    # Game done
    pygame.quit()

# Rock and roll
cleric()
