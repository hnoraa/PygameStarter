import pygame
from globalVals import *
from scenes import *

class Main():
    def __init__(self):
        # initialize pygame
        pygame.init()
        pygame.font.init()

        # set up window
        self.surface = pygame.display.set_mode(constants.SSIZE)
        pygame.display.set_caption(constants.TITLE)

        # pygame specifics
        self.clock = pygame.time.Clock()

        # starter scene
        self.scene = title.Title()   

    def run(self):        
        # main game loop
        while not flags.done:
            # get pressed keys
            keys = pygame.key.get_pressed()

            # events
            filteredEvents = []
            for event in pygame.event.get():
                filteredEvents.append(event)

            self.scene.events(filteredEvents, keys)

            # logic
            self.scene.update()
            
            # rendering
            self.scene.render(self.surface)

            # set the next scene
            self.scene = self.scene.nextScene

            # update loop
            pygame.display.flip()
            self.clock.tick(constants.FPS)

    def quit(self):
        # terminate
        pygame.quit()

if __name__ == '__main__':
    m = Main()
    m.run()
    m.quit()