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
        self.cat_pixel_selected = user.cat_pixel_selected
        self.map_pixel_selected = user.map_pixel_selected
        self.page_number = catalog.page_number
        self.chapter = catalog.get_chapter()
        self.tile_offset = user.tile_offset
