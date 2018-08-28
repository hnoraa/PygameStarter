import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.vx = 0
        self.vy = 0