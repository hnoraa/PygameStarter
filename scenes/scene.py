import pygame

class Scene():
    def __init__(self):
        self.nextScene = self

    def events(self, events, keys):
        pass

    def update(self):
        pass

    def render(self, surface):
        pass

    def transition(self, scene):
        self.nextScene = scene

    def end(self):
        self.nextScene = None
