import pygame
from . import scene
from . import game
from globalVals import *
from util import *

class Title(scene.Scene):
    def __init__(self):
        super().__init__()

    def events(self, events, keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    flags.done = True
                self.transition(game.Game())
            elif event.type == pygame.QUIT:
                flags.done = True

    def update(self):
        pass

    def render(self, surface):
        # background
        surface.fill(colors.PERU)

        # show title
        fontT = textUtil.setupFont(fonts.FMONO, fonts.FXXL)
        textT = textUtil.renderText(constants.TITLE, fontT, colors.DARKGREEN)
        textUtil.drawText(surface, textT, constants.SSIZE[0]//2 - textT.get_width()//2, constants.SSIZE[1]//2 - textT.get_height()//2)
        
        # show subtitle
        fontS = textUtil.setupFont(fonts.FMONO, fonts.FXLG)
        textS = textUtil.renderText(constants.SUBTITLE, fontS, colors.LIMEGREEN)
        textUtil.drawText(surface, textS, constants.SSIZE[0]//2 - textS.get_width()//2, (constants.SSIZE[1]//2) + 20)
