import pygame
from . import scene
from . import game
from globalVals import *
from util import *

class Title(scene.Scene):
    def __init__(self):
        super().__init__()

        # dimensions
        self.midX = (constants.SSIZE[0]//2)
        self.midY = (constants.SSIZE[1]//2)

        # title
        self.fontT = textUtil.setupFont(fonts.FMONO, fonts.FXXL)
        self.textT = textUtil.renderText(constants.TITLE, self.fontT, colors.DARKGREEN)
        self.titleMidX = (self.textT.get_width()//2)
        self.titleMidY = (self.textT.get_height()//2)

        # subtitle
        self.fontS = textUtil.setupFont(fonts.FMONO, fonts.FXLG)
        self.textS = textUtil.renderText(constants.SUBTITLE, self.fontS, colors.LIMEGREEN)
        self.textSOffsetY = (self.textT.get_height() - 30)

        # options
        self.options = ['New', 'Load', 'Quit']
        self.fontO = textUtil.setupFont(fonts.FMONO, fonts.FLRG)
        self.optionsText = []
        self.optionsOffsetY = self.midY + self.textT.get_height()
        for i in range(len(self.options)):
            self.optionsText.append(textUtil.renderText(self.options[i], self.fontO, colors.BLACK))

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
        textUtil.drawText(surface, self.textT, self.midX - self.titleMidX, self.midY - self.titleMidY)
        
        # show subtitle
        textUtil.drawText(surface, self.textS, self.midX - (self.textS.get_width()//2), self.midY + self.textSOffsetY)

        # show options
        for i in range(len(self.optionsText)):
            x = (self.midX - (self.optionsText[i].get_width()//2))
            y = (self.optionsText[i].get_height() * i) + self.optionsOffsetY
            textUtil.drawText(surface, self.optionsText[i], x, y)
