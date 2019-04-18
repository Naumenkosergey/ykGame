import pygame
import random

from game import Gui
from control import Control
from button import Button, currentLableButton
import button

# global currentLableButton
pygame.init()
widtWindow = 480
heigWindow = 500
window = pygame.display.set_mode((widtWindow, heigWindow))
pygame.display.set_caption("Угадай детальку")

widthButt = 200
heightBut = 40

controler = Control()
images = Gui()
score = Button(widthButt, heightBut)
labelButton = Button(10, 20)
rightUpButtons = Button(widthButt, heightBut)
leftUpButtons = Button(widthButt, heightBut)
rightDownButtons = Button(widthButt, heightBut)
leftDownButtons = Button(widthButt, heightBut)
centerDownButtons = Button(widthButt * 2 + 20, heightBut)
labelButton.labelButtons()

while controler.flag_game:
    BLabel1 = currentLableButton[0]
    BLabel2 = currentLableButton[1]
    BLabel3 = currentLableButton[2]
    BLabel4 = currentLableButton[3]
    nextPicture = "Не знаю, дальше("

    controler.control()
    window.fill(pygame.Color("Black"))
    images.draw_img(window)
    rightUpButtons.drawButton(window, message=BLabel1, x=widtWindow - (widtWindow - 250),
                              y=heigWindow - 200,
                              action1=images.next_picture, action2=labelButton.labelButtons,
                              action3=rightUpButtons.proverka, font_size=22)
    leftUpButtons.drawButton(window, message=BLabel2, x=widtWindow - (widtWindow - 30),
                             y=heigWindow - 200, action1=images.next_picture, action2=labelButton.labelButtons,
                             action3=leftUpButtons.proverka, font_size=22)
    rightDownButtons.drawButton(window, message=BLabel3, x=widtWindow - (widtWindow - 250),
                                y=heigWindow - 150, action1=images.next_picture, action2=labelButton.labelButtons,
                                action3=rightDownButtons.proverka, font_size=22)
    leftDownButtons.drawButton(window, message=BLabel4, x=widtWindow - (widtWindow - 30),
                               y=heigWindow - 150, action1=images.next_picture, action2=labelButton.labelButtons,
                               action3=leftDownButtons.proverka, font_size=22)
    centerDownButtons.drawButton(window, message=nextPicture, x=widtWindow - (widtWindow - 30),
                                 y=heigWindow - 100, action1=images.next_picture, action2=labelButton.labelButtons,
                                 action3=centerDownButtons.proverka, font_size=22)

    score.printScore(window, message=f'Баллы:{button.ball}', x=310, y=10, font_color=(0, 255, 255), font_size=35)
    pygame.display.flip()
pygame.quit()
