import pygame
from . import scene
from . import game
from . import loadGame
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
        self.selectedIndex = 0  # current item
        self.options = ['New', 'Load', 'Quit']
        self.fontO = textUtil.setupFont(fonts.FMONO, fonts.FLRG)
        self.optionsOffsetY = self.midY + self.textT.get_height()
        self.renderOptions()

    def renderOptions(self):
        self.optionsText = []

        for i in range(len(self.options)):
            if not self.selectedIndex == i:
                color = colors.BLACK
            else:
                color = colors.WHITE
            self.optionsText.append(textUtil.renderText(self.options[i], self.fontO, color))

    def events(self, events, keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    flags.done = True
                elif event.key == pygame.K_UP:
                    # navigate up through menu options
                    if self.selectedIndex > 0:
                        self.selectedIndex -= 1
                    else:
                        self.selectedIndex = len(self.options) - 1
                elif event.key == pygame.K_DOWN:
                    # navigate down through menu options
                    if self.selectedIndex < len(self.options) - 1:
                        self.selectedIndex += 1
                    else:
                        self.selectedIndex = 0
                elif event.key == pygame.K_RETURN:
                    # menu item 'press'
                    if self.selectedIndex == 0:
                        self.transition(game.Game())
                    elif self.selectedIndex == 1:
                        self.transition(loadGame.LoadGame())
                    else:
                        flags.done = True
            elif event.type == pygame.QUIT:
                flags.done = True

    def update(self):
       # highlight the correct option
       self.renderOptions()

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
