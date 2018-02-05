import pygame as pg
import os
import random

class Music:
    """
    For everything music related
    """
    
    def __init__(self):
        soundTrack = os.listdir("music")
        random.shuffle(soundTrack)
        pg.mixer.init()
        self._load("music/" + soundTrack.pop())
        self._play()

       
    def _load(self, track):
        pg.mixer.music.load(track)

    def _play(self):
        pg.mixer.music.play()

    
    def _queue(self, track):
        pg.mixer.music.queue(track)
