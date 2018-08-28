import pygame
from . import scene
from globalVals import *

class GameOver(scene.Scene):
    def __init__(self):
        super().__init__()

    def events(self, events, keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    flags.done = True
            elif event.type == pygame.QUIT:
                flags.done = True

    def update(self):
        pass

    def render(self, surface):
        # background
        surface.fill(colors.MOCCASIN)

        # show title
        font = textUtil.setupFont(fonts.FMONO, fonts.FXXL)
        text = textUtil.renderText(constants.GAMEOVERMSG, font, colors.RED)
        textUtil.drawText(surface, text, constants.SSIZE[0]//2 - text.get_width()//2, constants.SSIZE[1]//2 - text.get_height()//2)
