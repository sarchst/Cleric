import pygame as pg
import os
import random

class Music:
    """
    For everything music related
    """
    def __init__(self):
        self._queue_all_and_play()

    def _queue_all_and_play(self):
        sound_track = os.listdir("music")
        random.shuffle(sound_track)
        pg.mixer.init()
        self._load("music/" + sound_track.pop())
        self._play()
        for track in sound_track:
            self._queue("music/" + track);

    def _load(self, track):
        pg.mixer.music.load(track)

    def _play(self):
        pg.mixer.music.play()

    def _queue(self, track):
        pg.mixer.music.queue(track)
