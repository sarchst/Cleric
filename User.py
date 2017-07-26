import pygame
import operator
import time
start = time.time()
class User:
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

    def serve_keyboard(self, event):
        # Quitting
        if event.type == pygame.QUIT:
            self.is_done = True
        if event.key == pygame.K_F1:
            self.is_done = True
        """
        Camera tile movement controls
        """
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
        """
        Brush size selection
        """
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
        # 5 key press: 9x9 brush size
        if event.key == pygame.K_5:
            self.brush_size = 5
        # 6 key press: 11x11 brush size
        if event.key == pygame.K_6:
            self.brush_size = 6
        """
        Misc
        """
        # Saving
        if event.key == pygame.K_F5:
            self.is_saving = True
        # Log clearing
        if event.key == pygame.K_l and pygame.key.get_mods() == pygame.KMOD_LCTRL:
            self.is_clearing_log = True

    def serve_mouse(self, event):
        # Left mouse button
        if event.button == 1:
            if self.is_catalogging:
                self.cat_pixel_selected = self.cursor_pixel
                self.is_catalogging = False
            else:
                self.map_pixel_selected = self.cursor_pixel
        # Middle mouse button
        if event.button == 2:
            pass
        # Right mouse button
        if event.button == 3:
            self.is_catalogging = True
        # Scroll wheel up
        if event.button == 4:
            if self.is_catalogging:
                self.scroll_wheel += 1
        # Scroll wheel down
        if event.button == 5:
            if self.is_catalogging:
                self.scroll_wheel -= 1

    def get_input(self):
        """
        Waits here for a mouse or key event
        """
        events = [
            pygame.MOUSEBUTTONDOWN,
            pygame.MOUSEBUTTONUP,
            pygame.KEYDOWN
        ]
        event = pygame.event.wait()
        while event.type not in events:
            if time.time() - start > 0.25:
                break
            event = pygame.event.wait()
        # The selected map pixel must stay None if no event
        # occured. The catalog selection must be persistent
        self.map_pixel_selected = None
        # Mouse service
        self.cursor_pixel = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            self.serve_mouse(event)
        # Keyboard service
        if event.type == pygame.KEYDOWN:
            self.serve_keyboard(event)
