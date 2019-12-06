import pygame
from control import Control
from button import Button
from buttonImage import ButtonImage
import buttonImage
from victory import *



class Menu:
    images = Gui()

    def __init__(self):
        self.backgraund = pygame.image.load("image/screen.png")
        self.img = pygame.transform.scale(self.backgraund, (1300, 750))  # чтобы все картинки были одного размера

    def draw_menu(self, window):
        path = "image/"
        play = path + "Play.png"
        stor = path + "Stories.png"
        startgame = ButtonImage(850, 150, 300, 103, play)
        storBut = ButtonImage(850, 250, 300, 103, stor)
        window.blit(self.backgraund, (0, 0))
        startgame.drawButtonImg(window,action1=startgame.clickStart,action2=startgame.labelButtons)
        # storBut.drawButtonImg(window,action1=showVictory)

    def show_menu(self, window):
        if buttonImage.menuhka==True:
            self.draw_menu(window)
        else:
            window.fill(pygame.Color("Black"))
