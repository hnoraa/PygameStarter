import pygame
from . import scene
from globalVals import *

class GameOver(scene.Scene):
    def __init__(self):
        super().__init__()

    def events(self, events, keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                flags.done = True

    def update(self):
        pass

    def render(self, surface):
        pass
