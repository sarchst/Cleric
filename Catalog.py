import pygame as pg
import os

class Catalog:
    def __init__(self):
        self.page_number = 0
        self.pages = []
        self.page_count = 0
        self.pages_per_chapter = []
        self.chapters = [0, 1, 2, 3, 4, 5]
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
                page = pg.transform.scale2x(pg.image.load(parent + "/" + img))
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
