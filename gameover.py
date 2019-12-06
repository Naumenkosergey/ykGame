import pygame

from game import Gui
from control import Control

from text import Text

pygame.init()
widtWindow = 768
heigWindow = 512
window = pygame.display.set_mode((widtWindow, heigWindow))
pygame.display.set_caption("ПОБЕДА")

controler = Control()
images = Gui()
score = Text((0, 255, 255),"impact.ttf",50)

def showVictory():
    victoryWindow = pygame.image.load("image/victory.png")
    victoryWindow = pygame.transform.scale(victoryWindow, (1280, 720))

    window.blit(victoryWindow, (0, 0))
