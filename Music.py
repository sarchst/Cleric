import pygame as pg

class Music:
    """
    For everything music related
    """
    # SARCHER:
    # Today you will build a shuffle music player like what you see in windows media player or itunes:
    #   Step 1:
    #     Go to youtube and rip a bunch of ambient tracks. Try searching:
    #         ambient wind rustling through trees
    #         ambient medieval market sounds
    #         ambient medieval overworld
    #         medieval tavern music
    #     Place them as mp3s in the music folder
    #   Step 2:
    #     Import the os module and determine the number of files in the music dir.
    #     For each file name in the dir append it to a string list.
    #   Step 3:
    #     Randomly shuffle the string list
    #   Step 4:
    #     Init() the pg mixer
    #   Step 5:
    #     Load() the first track of the string list and then pop the top of the string list.
    #   Step 6:
    #     For each of the remaining strings in the string list, queue (hint: pg.mixer.music.queue(string))
    #   Step 7:
    #     Play()
    #
    # All of this must take place in the constructor, but you may write extra methods in this class
    # to help you along.
    # As an added challenge, we will adopt the (_) underscore prefx notation for all method names
    # which we deem private. That is, the current load() and play() functions are
    # private to this class. Their functionalities are used internally by the constructor.
    # As our rule of thumb:
    #   A good class has more than 50% of its methods private.
    #   A great class has more than 75% of its methods private.
    def __init__(self, track):
        pg.mixer.init()
        self._load(track)
        self._play()

    def _load(self, track):
        pg.mixer.music.load(track)

    def _play(self):
        pg.mixer.music.play()
