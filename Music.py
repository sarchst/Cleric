import pygame

class Music:
    def __init__(self, track):
        pygame.mixer.init()
        self.load(track)
        self.play()

    def load(self, track):
        pygame.mixer.music.load(track)

    def play(self):
        pygame.mixer.music.play()
