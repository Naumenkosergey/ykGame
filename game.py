import pygame
import random
import os

namePict="1"

class Gui:
    def __init__(self):
        global namePict
        path = "picturies"
        spisok = ["picturies/" + i for i in os.listdir(path)]
        i = random.randint(0, len(spisok) - 1)
        self.img = pygame.image.load(spisok[i])
        self.img = pygame.transform.scale(self.img, (200, 200))

        namePict = spisok[i]
        namePict = namePict.split(".jpg")
        namePict.pop()
        namePict = ''.join(namePict)
        namePict = namePict.split("picturies/")
        namePict.pop(0)
        namePict = ''.join(namePict)


    def draw_img(self, window):
        window.blit(self.img, (130, 50))

    def next_picture(self):
        global namePict
        self.__init__()

