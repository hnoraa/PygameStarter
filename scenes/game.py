import pygame
from . import scene
from globalVals import *

class Game(scene.Scene):
    def __init__(self):
        super().__init__()

    def events(self, events, keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                pass

    def update(self):
        pass

    def render(self, surface):
        surface.fill(colors.MAGENTA)
