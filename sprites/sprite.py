import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.x = x
        self.y = y