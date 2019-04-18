import pygame
from pygame.locals import *

class Control:
    
    def __init__(self):
        self.flag_game = True


    def control(self):
        for event in pygame.event.get():
            if event.type == QUIT:#выход при нажатии на крестик
                self.flag_game=False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:#выход при нажатии на клавишу ESC
                    self.flag_game=False

                    
                    
