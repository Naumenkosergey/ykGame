import pygame

menuhka = True
playgame = False


class ButtonImage:

    def __init__(self, x, y, width, height, img):
        self.x = x
        self.y = y
        self.img = img
        self.width = width
        self.height = height

    def showButtonImg(self, window):
        self.buttonimg = pygame.image.load(self.img)
        # pygame.draw.rect(window, (x, y, self.width, self.height))
        window.blit(self.buttonimg, (self.x, self.y))

    def clickStart(self):
        global menuhka, playgame
        if menuhka ==True:
            playgame=True
            menuhka=False
        else:
            playgame = False
            menuhka = True


    def drawButtonImg(self, window, action1=None):
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
                action1()
                print (menuhka)
                print("click" + self.img)
                pygame.time.delay(200)  # 200мс ожидание
