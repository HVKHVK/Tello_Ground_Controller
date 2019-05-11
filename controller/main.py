# Tello Ground Control

# Imports
import controller.config as config
import pygame

from controller.tello import Tello

class TelloControl(object):
    """
    Controls the Tello. All commands on the SDK Documentation applies(Eventually). Display locates here.
    Control parameters will define here:

    All control parameters will be given inside the Ground Station as well.
    """
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Tello Ground Station")

        if config.SCREEN_SETTINGS is "WINDOWED":
            self.screen = pygame.display.set_mode([config.SCREEN_HEIGHT, config.SCREEN_WIDTH])
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.tello = Tello()

        pygame.time.set_timer(pygame.USEREVENT + 1, 50)

    def run(self):



def main():
    tellocontrol = TelloControl()
    tellocontrol.run()


if __name__ == "__main__":
    main()