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
        self.textSOffsetY = (self.textT.get_height())

        self.gameSaveRect = pygame.Rect((self.midX//2) - 50, (self.midY//2), self.midX + 100, self.midY)

        # game saves
        self.selectedGame = 0
        self.gameSaves = ['save1', 'save2', 'save3']

        self.fontG = textUtil.setupFont(fonts.FMONO, fonts.FLRG)
        self.gameSavesOffsetY = self.gameSaveRect.top
        self.renderGameSaves()

        # options
        self.selectedIndex = 0  # current item
        self.options = ['Load', 'New Game', 'Quit']
        self.fontO = textUtil.setupFont(fonts.FMONO, fonts.FLRG)
        self.optionsOffsetY = self.midY + (self.gameSaveRect.bottom//2)
        self.renderOptions()

    def renderOptions(self):
        self.optionsText = []

        for i in range(len(self.options)):
            if not self.selectedIndex == i:
                color = colors.BLACK
            else:
                color = colors.WHITE
            self.optionsText.append(textUtil.renderText(self.options[i], self.fontO, color))

    def renderGameSaves(self):
        self.gameSavesText = []
        
        for i in range(len(self.gameSaves)):
            if not self.selectedGame == i:
                textColor = colors.DIMGRAY
            else:
                textColor = colors.WHITE
            #self.gameSavesText.append(textUtil.renderText(self.gameSaves[i]['name'], self.fontG, textColor))
            self.gameSavesText.append(textUtil.renderText(self.gameSaves[i], self.fontG, textColor))

    def events(self, events, keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    flags.done = True
                elif event.key == pygame.K_UP:
                    # navigate up through game saves
                    if self.selectedGame > 0:
                        self.selectedGame -= 1
                    else:
                        self.selectedGame = len(self.options) - 1
                elif event.key == pygame.K_DOWN:
                    # navigate down through game saves
                    if self.selectedGame < len(self.options) - 1:
                        self.selectedGame += 1
                    else:
                        self.selectedGame = 0
                elif event.key == pygame.K_RIGHT:
                    # navigate right through game options
                    if self.selectedIndex < len(self.options) - 1:
                        self.selectedIndex += 1
                    else:
                        self.selectedIndex = 0
                elif event.key == pygame.K_LEFT:
                    # navigate left through game options
                    if self.selectedIndex > 0:
                        self.selectedIndex -= 1
                    else:
                        self.selectedIndex = len(self.options) - 1
                elif event.key == pygame.K_RETURN:
                    # actions
                    if self.selectedIndex == 0:
                        # load selected game save
                        print('Loading...')
                        print(self.gameSaves[self.selectedGame])
                    elif self.selectedIndex == 1:
                        # overwrite selected game save
                        print('New/Delete game save')
                    else:
                        flags.done = True
            elif event.type == pygame.QUIT:
                flags.done = True

    def update(self):
       # highlight the correct option and game save
       self.renderOptions()
       self.renderGameSaves()

    def render(self, surface):
        # background
        surface.fill(colors.PERU)

        # show title
        textUtil.drawText(surface, self.textT, self.midX - self.titleMidX, 0)
        
        # show subtitle
        textUtil.drawText(surface, self.textS, self.midX - (self.textS.get_width()//2), self.textSOffsetY)

        # show game saves background
        pygame.draw.rect(surface, colors.BLACK, self.gameSaveRect, 0)

        # show game saves
        x = self.gameSaveRect.left + 20
        textUtil.drawText(surface, self.gameSavesText[0], x, self.gameSaveRect.top + self.gameSavesText[0].get_height())
        textUtil.drawText(surface, self.gameSavesText[1], x, self.gameSaveRect.centery - (self.gameSavesText[1].get_height()//2))
        textUtil.drawText(surface, self.gameSavesText[2], x, self.gameSaveRect.bottom - self.gameSavesText[2].get_height() * 2)

        # show options
        y = self.optionsText[0].get_height() + self.optionsOffsetY
        textUtil.drawText(surface, self.optionsText[0], self.gameSaveRect.left, y)
        textUtil.drawText(surface, self.optionsText[1], self.midX - (self.optionsText[1].get_width()//2), y)
        textUtil.drawText(surface, self.optionsText[2], self.gameSaveRect.right - self.optionsText[2].get_width(), y)