import pygame
from . import scene
from . import game
from globalVals import *
from util import *

class PauseMenuMain(scene.Scene):
    def __init__(self):
        super().__init__()

        # setup main title
        self.fontT = textUtil.setupFont(fonts.FMONO, fonts.FLRG)
        self.textT = textUtil.renderText('Main Menu', self.fontT, colors.BLUE)

        # setup menu options
        self.fontM = textUtil.setupFont(fonts.FMONO, fonts.FMED)
        self.menuItems = ['Items', 'Weapons', 'Save', 'Options']
        self.menuOffsetY = self.textT.get_height() + 10
        self.menuOffsetX = 10

        self.menuItemsText = []
        for i in range(len(self.menuItems)):
            self.menuItemsText.append(textUtil.renderText(self.menuItems[i], self.fontM, colors.BLACK))

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
        textUtil.drawText(surface, self.textT, constants.SSIZE[0]//2 - self.textT.get_width()//2, 0)

        # draw menu items
        self.drawMenuOptions(surface)

    def drawMenuOptions(self, surface):
        for i in range(len(self.menuItemsText)):
            textUtil.drawText(surface, self.menuItemsText[i], self.menuOffsetX, ((self.menuItemsText[i].get_height() * i) + self.menuOffsetY))