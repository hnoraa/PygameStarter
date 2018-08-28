import pygame
import sys
import os
from globalVals import *

def setupFont(family, size):
    if flags.useCustomFont:
        return pygame.font.Font(os.path.join('assets', 'fonts', fonts.FCUST), size)
    else:
        return pygame.font.SysFont(family, size)

def renderText(msg, font, color):
    return font.render(msg, True, color)

def drawText(surface, textObj, x, y):
    surface.blit(textObj, (x, y))
