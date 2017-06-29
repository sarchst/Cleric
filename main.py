import os
import pygame

# The user - That's you!
class User:
    def __init__(self):
        # Scroll wheel index
        self.scroll_wheel = 0
        # Selected map pixel
        self.map_pixel = None
        # Selected catalog pixel
        self.cat_pixel = None
        # User is viewing the catalog
        self.catalogging = False
        # User wishes to quit
        self.done = False

    def serve_keyboard(self, event):
        # User pushes F1 wanting to quit
        if event.key == pygame.K_F1:
            self.done = True
        # An example of how to use key events for
        # future reference
        if event.key == pygame.K_a:
            pass

    def serve_mouse(self, event, catalog):
        cursor = pygame.mouse.get_pos()
        # The selected map pixel will always revert to None
        # and must be set with the left mouse
        # button when the user is not catalogging
        self.map_pixel = None
        # Left mouse button
        if event.button == 1:
            if self.catalogging:
                # Pick a catalog pixel and stop looking at the catalog
                self.cat_pixel = cursor
                self.catalogging = False
            else:
                # Pick a map pixel if the catalog is not being looked at
                self.map_pixel= cursor
        # Middle mouse buton press - a temporary place holder
        if event.button == 2:
            pass
        # Right mouse button press - user is now looking at the catalog
        if event.button == 3:
            self.catalogging = True
        # Scroll wheel up only when viewing catalog
        if event.button == 4:
            if self.catalogging:
                # Every catalog page is doubled up for animation
                # which we will add later
                self.scroll_wheel += 2
                # Upper clamp if user scrolls out of upper bounds
                if self.scroll_wheel >= catalog.page_count:
                    self.scroll_wheel = catalog.page_count - 2
        # Scroll wheel down only when viewing catalog
        if event.button == 5:
            if self.catalogging:
                self.scroll_wheel -= 2
                # Lower clamp if user scrolls out of lower bounds
                if self.scroll_wheel < 0:
                    self.scroll_wheel = 0

    def get_input(self, catalog):
        expected = [pygame.QUIT, pygame.MOUSEBUTTONUP, pygame.KEYUP]
        # Wait here for one of the expected events to occur
        event = pygame.event.wait()
        while event.type not in expected:
            event = pygame.event.wait()
        # User hits the 'X' button of a window wanting to quit
        if event.type == pygame.QUIT:
            self.done = False
        # Service user mouse event on the up stroke
        if event.type == pygame.MOUSEBUTTONUP:
            self.serve_mouse(event, catalog)
        # Service user keyboard event on the up stroke
        if event.type == pygame.KEYUP:
            self.serve_keyboard(event)

# The catalog - all sprite artwork is stored in the catalog
class Catalog:
    def __init__(self, root):
        # One sprite artwork image constitutes a page.
        # These pages are loaded into this list for the renderer
        self.pages = []
        # The overall page count is kept for future reference
        self.page_count = 0
        # Pages are segregated into chapters.
        # This list holds the number of pages per chapter
        self.chapter_size = []
        # This list keeps track of the available chapters
        self.chapters = [0, 1, 2, 3, 4, 5]
        # This object, when instantiated, will load itself
        # at creation with a chapters folder directory
        # containing all the sprite artwork.
        for chapter in self.chapters:
            parent = root + "/" + str(chapter)
            imgs = sorted(os.listdir(parent))
            for img in imgs:
                page = pygame.image.load(parent + "/" + img)
                self.pages.append(page)
            self.chapter_size.append(len(imgs))
            self.page_count = len(self.pages)

    # This function returns the chapter when given a page number.
    def get_chapter(self, page_number):
        for chapter in self.chapters:
            if page_number < sum(self.chapter_size[:chapter + 1]):
                return chapter
        return None

# Tiles hold a catalog pixel and a map pixel.
# Tiles also hold the page number and chapter of the catalog.
class Tile:
    def __init__(self, user, catalog):
        self.cat_pixel = user.cat_pixel
        self.map_pixel = user.map_pixel
        self.page_number = user.scroll_wheel
        self.chapter = catalog.get_chapter(self.page_number)

# The video class renders catalog artwork to the display.
class Video:
    def __init__(self, res):
        self.screen = pygame.display.set_mode(res)
        # Renders are done sequentially by layer.
        # Catalog sprites, by chapter, are moved to video layers prior to the render.
        # This allows for more intricate sprites, like door frames, to render
        # overtop of other sprites, like grass blades and kaitjies, without clipping.
        self.layers = [ {}, {}, {}, {}, {}, {} ]
        self.black = (0, 0, 0)
        # The sprite width is modified here
        self.sprite_width = 16
        # The sprite width dictates the sprite area
        self.sprite_area = (self.sprite_width, self.sprite_width)

    # Pixels can be translated to grid co-ordinates for dictionaries keys
    def to_grid(self, pixel):
        return tuple(int(i / self.sprite_width) for i in pixel)

    # Grid co-ordinates can be translated to pixels for rendering
    def to_pixel(self, grid):
        return tuple(int(i * self.sprite_width) for i in grid)

    # Mixing these two gives a snap function for rounding down a pixel co-ordinate
    def snap(self, pixel):
        return self.to_pixel(self.to_grid(pixel))

    # This function populates the layer dictionary with a tile
    def lay(self, tile):
        self.layers[tile.chapter][self.to_grid(tile.map_pixel)] = tile

    # For you to figure out, sarchy - use pickle again, and see if
    # you can figure out a way to have the user object command this save
    # method to save the layer information to the disk
    def save(self):
        pass

    # Same goes for load
    def load(self):
        pass

    # This method shows the catalog
    def show_catalog(self, user, catalog):
        self.screen.fill(self.black)
        page = catalog.pages[user.scroll_wheel]
        top_left = (0, 0)
        self.screen.blit(page, top_left)
        pygame.display.flip()

    # This method shows the game map
    def show_map(self, catalog):
        self.screen.fill(self.black)
        for layer in self.layers:
            for grid, tile in layer.iteritems():
                page = catalog.pages[tile.page_number]
                self.screen.blit(page,
                        (self.snap(tile.map_pixel), self.sprite_area),
                        (self.snap(tile.cat_pixel), self.sprite_area))
        pygame.display.flip()

# And here we go - we build all the objects here and have them
# communicate with one another
def main():
    pygame.init()
    pygame.display.set_caption("Cleric")
    video = Video((640, 480))
    catalog = Catalog("dawnlike")
    user = User()
    while not user.done:
        user.get_input(catalog)
        if user.map_pixel != None and user.cat_pixel != None:
            video.lay(Tile(user, catalog))
        if user.catalogging:
            video.show_catalog(user, catalog)
        else:
            video.show_map(catalog)
    pygame.quit()

main()
