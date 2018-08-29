import pygame
from . import scene
from . import game
from globalVals import *
from util import *

class PauseMenuMain(scene.Scene):
    def __init__(self):
        super().__init__()

    def events(self, events, keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.transition(game.Game())
            elif event.type == pygame.QUIT:
                flags.done = True

    def update(self):
        pass

    def render(self, surface):
        surface.fill(colors.PLUM)

        # menu title
        fontT = textUtil.setupFont(fonts.FMONO, fonts.FLRG)
        textT = textUtil.renderText('Paused', fontT, colors.BLUE)
        textUtil.drawText(surface, textT, constants.SSIZE[0]//2 - textT.get_width()//2, 10)
