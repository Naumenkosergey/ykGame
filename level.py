import pygame
from button import Button, currentLableButton
import button
from game import Gui
from control import Control
from buttonImage import ButtonImage


pygame.init()
widtWindow = 1333
heigWindow = 750
window = pygame.display.set_mode((widtWindow, heigWindow))
pygame.display.set_caption("Угадай детальку")

widthButt = 200
heightBut = 40


widthButt = 200
heightBut = 40

controler = Control()
images = Gui()
score = Button(widthButt, heightBut)


def showLevel():
    path = "image/"
    but1 = path + "but1.png"
    but2 = path + "but2.png"
    back = path + "Back.png"
    levelscreen = pygame.image.load("image/level.png")
    levelscreen = pygame.transform.scale(levelscreen, (1300, 750))

    window.blit(levelscreen, (0, 0))
    firstButton=ButtonImage(750, 300, 300, 100, but1)
    secondbutton=ButtonImage(750, 400, 300, 100, but2)
    threeBotton=ButtonImage(750, 500, 300, 100, but1)
    fourButton=ButtonImage(750, 600, 300, 100, but2)
    backBut = ButtonImage(50, 100, 150, 98, back)
    firstButton.drawButtonImg(window,action1=None)
    secondbutton.drawButtonImg(window, action1=None)
    threeBotton.drawButtonImg(window, action1=None)
    fourButton.drawButtonImg(window,action1=None)
    backBut.drawButtonImg(window,action1=backBut.clickStart)
    images.draw_img(window,150,350)



    # BLabel1 = currentLableButton[0]
    # BLabel2 = currentLableButton[1]
    # BLabel3 = currentLableButton[2]
    # BLabel4 = currentLableButton[3]
    # nextPicture = "Не знаю, дальше("
    #
    # images.draw_img(window)
    # rightUpButtons.drawButton(window, message=BLabel1, x=widtWindow - (widtWindow - 250),
    #                           y=heigWindow - 200,
    #                           action1=images.next_picture, action2=labelButton.labelButtons,
    #                           action3=rightUpButtons.proverka, font_size=22)
    # leftUpButtons.drawButton(window, message=BLabel2, x=widtWindow - (widtWindow - 30),
    #                          y=heigWindow - 200, action1=images.next_picture, action2=labelButton.labelButtons,
    #                          action3=leftUpButtons.proverka, font_size=22)
    # rightDownButtons.drawButton(window, message=BLabel3, x=widtWindow - (widtWindow - 250),
    #                             y=heigWindow - 150, action1=images.next_picture, action2=labelButton.labelButtons,
    #                             action3=rightDownButtons.proverka, font_size=22)
    # leftDownButtons.drawButton(window, message=BLabel4, x=widtWindow - (widtWindow - 30),
    #                            y=heigWindow - 150, action1=images.next_picture, action2=labelButton.labelButtons,
    #                            action3=leftDownButtons.proverka, font_size=22)
    # centerDownButtons.drawButton(window, message=nextPicture, x=widtWindow - (widtWindow - 30),
    #                              y=heigWindow - 100, action1=images.next_picture, action2=labelButton.labelButtons,
    #                              action3=centerDownButtons.proverka, font_size=22)
    #
    # score.print_text(window, message=f'Баллы:{button.ball}', x=310, y=10, font_color=(0, 255, 255), font_size=35)
