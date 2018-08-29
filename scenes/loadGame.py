import pygame
from . import scene
from . import game
from . import title
from globalVals import *
from util import *

class LoadGame(scene.Scene):
    def __init__(self):
        super().__init__()

        # setip main title
        self.fontT = textUtil.setupFont(fonts.FMONO, fonts.FLRG)
        self.textT = textUtil.renderText('Load Game', self.fontT, colors.BLUE)

    def events(self, events, keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.transition(title.Title())
                elif event.key == pygame.K_q:
                    flags.done = True
            elif event.type == pygame.QUIT:
                flags.done = True

    def update(self):
        pass

    def render(self, surface):
        surface.fill(colors.PLUM)

        # menu title
        textUtil.drawText(surface, self.textT, constants.SSIZE[0]//2 - self.textT.get_width()//2, 0)
