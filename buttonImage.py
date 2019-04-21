import pygame
import random
import os
import game

menuhka = True
playgame = False

currentLableButton = ["1", "2", "3", "4"]  # список для вариантов ответов на кнопки
labelButtons = []  # Список со всеми возможными вариантами ответов
ball = 0  # перемменная, считает правильные ответы
answer = ""  # Переменная, которая содержит правильный ответ


class ButtonImage:

    def __init__(self, x, y, width, height, img):
        self.x = x
        self.y = y
        self.img = img
        self.width = width
        self.height = height

    def showButtonImg(self, window):
        self.buttonimg = pygame.image.load(self.img)
        # self.buttonimg = pygame.transform.scale(self.img, (self.width, self.height))

        # pygame.draw.rect(window, (x, y, self.width, self.height))
        window.blit(self.buttonimg, (self.x, self.y))

    def clickStart(self):
        global menuhka, playgame
        if menuhka == True:
            playgame = True
            menuhka = False
        else:
            playgame = False
            menuhka = True

    def labelButtons(self):  # Метод(функция) смены вариантов ответа
        global nextLabelFlag, currentLableButton, labelButtons, namePict, answer

        # Создание списка. со всеми возможными вариантами ответа, по названию деталей из папки
        path = "picturies"
        labelButtons = [i for i in os.listdir(path)]  # создаем список файлов из полных имен картинки с расширенниями
        labelButtons = ''.join(labelButtons)  # Преобразование списка в строчку
        labelButtons = labelButtons.split(".jpg")  # разделяем строку на элементы, относительно .jpg, т.е убираем .jpg
        labelButtons.pop()  # Удаляем последний элемент, иак как он пустой

        a = labelButtons.copy()  # Переносим копию нашего списка в новый список a
        answer = game.namePict  # Ответ равен имени картинки
        while answer not in currentLableButton:  # наполняем список для кнопок, пока не будет в нем правильного ответа
            for i in range(4):
                currentLableButton[i] = a.pop(
                    random.randint(0, len(a) - 1))  # Наполнение списка надписей на кнопки аозможными вариантами

    def proverka(self, labBut):  # Функция проверки на правильность ответа
        global ball, answer
        if labBut == answer:  # если нажата кнопка у которой надпись совбадает с именем картинки, то верно и + балл
            ball += 1

    def drawButtonImg(self, window, text=None, action1=None, action2=None, action3=None, font_size=None):
        global menuhka, playgame
        # global currentLableButton, nextLabelFlag, ball, answer
        mouse = pygame.mouse.get_pos()  # позиция мышки
        click = pygame.mouse.get_pressed()  # Щелчок ЛКМ
        self.showButtonImg(window)
        # self.imgBut=pygame.image.load("butimg.png")
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[
            1] < self.y + self.height:  # Проверка находится ли укзатель в поределах кнопкиесли находится, то прорисовываем новый прямоугольник, только другим цвето
            # self.rec
            # если н1ажать на кнопку, когда указатель мыши входит в кнопку, то проверится на правильность и перегрузит картинки и варианты
            if click[0] == 1:
                if action1 != None and action2 != None and action3 != None:
                    action3(text)
                    action1()
                    action2()
                elif action1 != None and action2 != None and action3 == None:
                    action1()
                    action2()
                elif action1 != None and action2 == None and action3 == None:
                    action1()
                    # print (menuhka)
                # print(currentLableButton)
                pygame.time.delay(200)  # 200мс ожидание
        if text != None:
            self.print_text(window=window, message=text, x=self.x + 30, y=self.y + 20, font_size=font_size)

    def print_text(self, window, message, x, y, font_color=(255, 255, 255), font_type="impact.ttf", font_size=20):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        window.blit(text, (x, y - 5))
