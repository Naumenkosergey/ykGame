import pygame
import random
import os

namePict="1"

class Gui:
    def __init__(self):
        global namePict
        path = "picturies" #Папка где хранятся картинки
        spisok = ["picturies/" + i for i in os.listdir(path)]#Список из имен картинок с указанием пути
        i = random.randint(0, len(spisok) - 1)
        self.img = pygame.image.load(spisok[i])#Вынрузка картинки в окно
        self.img = pygame.transform.scale(self.img, (200, 200)) #чтобы все картинки были одного размера

        namePict = spisok[i]
        namePict = namePict.split(".jpg")
        namePict.pop()
        namePict = ''.join(namePict)
        namePict = namePict.split("picturies/")
        namePict.pop(0)
        namePict = ''.join(namePict) #имя картинки но без указания папки и расширения, только имя


    def draw_img(self, window):
        window.blit(self.img, (130, 50))

    def next_picture(self):
        global namePict
        self.__init__()

