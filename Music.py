import pygame as pg

class Music:
    def __init__(self, track):
        pg.mixer.init()
        self.load(track)
        self.play()

    def load(self, track):
        pg.mixer.music.load(track)

    def play(self):
        pg.mixer.music.play()
