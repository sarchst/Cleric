import operator
import time
import pygame as pg

class User:
    """
    For everything user input related
    """
    def __init__(self):
        self.scroll_wheel = 0
        self.map_pixel_selected = None
        self.cat_pixel_selected = None
        self.cursor_pixel = None
        self.is_catalogging = False
        self.is_clearing_log = False
        self.is_done = False
        self.tile_offset = (0, 0)
        self.tile_pan = 5
        self.brush_size = 1
        self.is_saving = False
        self.is_erasing = False
        self.page_scroll = 0
        self.is_querying = False

    def serve_keyboard(self, event):
        # User quits (END or X button on screen)
        if event.type == pg.QUIT:
            self.is_done = True
        if event.key == pg.K_END:
            self.is_done = True
        # (q)
        if event.key == pg.K_q:
            # Query
            self.is_querying = True;
        # (w)
        if event.key == pg.K_w:
            # Catalog page scroll up
            if self.is_catalogging:
                self.page_scroll -= 1
            else:
                # Pan up
                self.tile_offset = tuple(map(operator.add,\
                    self.tile_offset, (0, self.tile_pan)))
        # (s)
        if event.key == pg.K_s:
            # Catalog page scroll down
            if self.is_catalogging:
                self.page_scroll += 1
            # Pan down
            else:
                self.tile_offset = tuple(map(operator.sub,\
                    self.tile_offset, (0, self.tile_pan)))
        # Locks the page scroll
        if self.page_scroll < 0:
            self.page_scroll = 0
        # (a)
        if event.key == pg.K_a:
            # Pan left
            self.tile_offset = tuple(map(operator.add,\
                self.tile_offset, (self.tile_pan, 0)))
        # (d)
        if event.key == pg.K_d:
            # Pan right
            self.tile_offset = tuple(map(operator.sub,\
                self.tile_offset, (self.tile_pan, 0)))
        # (1) 1x1 brush size
        if event.key == pg.K_1:
            self.brush_size = 1
        # (2) 3x3 brush size
        if event.key == pg.K_2:
            self.brush_size = 2
        # (3) 5x5 brush size
        if event.key == pg.K_3:
            self.brush_size = 3
        # (4) 7x7 brush size
        if event.key == pg.K_4:
            self.brush_size = 4
        # (5) 9x9 brush size
        if event.key == pg.K_5:
            self.brush_size = 5
        # (6) 11x11 brush size
        if event.key == pg.K_6:
            self.brush_size = 6
        # (F5) Saving
        if event.key == pg.K_F5:
            self.is_saving = True
        # (F9) Screen clearing
        if event.key == pg.K_F9:
            self.is_erasing = True

    def serve_mouse(self, event, pixel_res):
        # Left mouse button
        if event.button == 1:
            if self.is_catalogging:
                self.cat_pixel_selected = tuple(map(operator.add,\
                    self.cursor_pixel, (0, self.page_scroll * pixel_res[1])))
                self.is_catalogging = False
            else:
                self.map_pixel_selected = self.cursor_pixel
        # Middle mouse button
        if event.button == 2:
            # Clears the event log
            self.is_clearing_log = True
        # Right mouse button
        if event.button == 3:
            self.is_catalogging = True
        # Scroll wheel up
        if event.button == 4:
            if self.is_catalogging:
                self.scroll_wheel += 1
            # Resets catalog page scroll
            self.page_scroll = 0
        # Scroll wheel down
        if event.button == 5:
            if self.is_catalogging:
                self.scroll_wheel -= 1
            # Resets catalog page scroll
            self.page_scroll = 0

    def get_input(self, pixel_res):
        """
        Waits here for a mouse or key event or for 0.25 seconds to elapse
        """
        start = time.time()
        event = pg.event.poll()
        while event.type not in [pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.KEYDOWN]:
            if time.time() - start > 0.25:
                break
            event = pg.event.poll()
        # The selected map pixel must stay None if no event
        # occured. The catalog selection must be persistent
        self.map_pixel_selected = None
        # Mouse service
        self.cursor_pixel = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONUP:
            self.serve_mouse(event, pixel_res)
        # Keyboard service
        if event.type == pg.KEYDOWN:
            self.serve_keyboard(event)
