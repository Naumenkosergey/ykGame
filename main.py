import pygame
import random

from game import Gui
from control import Control
from button import Button, currentLableButton
import button
from menu import Menu
import level
from buttonImage import ButtonImage, menuhka, victory
import buttonImage
import victory

pygame.init()
widtWindow = 1280
heigWindow = 720
window = pygame.display.set_mode((widtWindow, heigWindow))
pygame.display.set_caption("Угадай детальки")

# widthButt = 200
# heightBut = 40

controler = Control()
meny=Menu()
while controler.flag_game:

    controler.control()
    meny.show_menu(window)
    if buttonImage.menuhka==False:
        level.showLevel()
        if buttonImage.victory==True:
            victory.showVictory()
        if buttonImage.queshion==10 and buttonImage.victory==False:
            victory.showOver()


    pygame.display.flip()
pygame.quit()
