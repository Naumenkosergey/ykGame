import pygame
from button import Button, currentLableButton
import button
from game import Gui
from control import Control
from buttonImage import ButtonImage, currentLableButton
import buttonImage
from text import Text

pygame.init()
widtWindow = 1333
heigWindow = 750
window = pygame.display.set_mode((widtWindow, heigWindow))
pygame.display.set_caption("Угадай детальку")

widthButt = 200
heightBut = 40

controler = Control()
images = Gui()
score = Text((0, 255, 255),"impact.ttf",50)

def showLevel():
    print(currentLableButton)
    # while buttonImage.menuhka==False:
    path = "image/"
    but1 = path + "but1.png"
    but2 = path + "but2.png"
    back = path + "Back.png"
    almaz = path + "almaz.png"
    levelscreen = pygame.image.load("image/level.png")
    almaz = pygame.image.load(almaz)
    levelscreen = pygame.transform.scale(levelscreen, (1300, 750))


    BLabel1 = currentLableButton[0]
    BLabel2 = currentLableButton[1]
    BLabel3 = currentLableButton[2]
    BLabel4 = currentLableButton[3]
    nextPicture = "Не знаю, дальше("

    window.blit(levelscreen, (0, 0))
    window.blit(almaz,(875,25))

    firstButton = ButtonImage(750, 300, 300, 100, but1)
    secondbutton = ButtonImage(750, 400, 300, 100, but2)
    threeBotton = ButtonImage(750, 500, 300, 100, but1)
    fourButton = ButtonImage(750, 600, 300, 100, but2)
    backBut = ButtonImage(50, 100, 150, 98, back)
    nextPic=ButtonImage(100,660,600,100, but1)

    firstButton.drawButtonImg(window, text=BLabel1, font_size=50, action1=images.next_picture,
                              action2=firstButton.labelButtons,action3=firstButton.proverka)
    secondbutton.drawButtonImg(window, text=BLabel2, font_size=50, action1=images.next_picture,
                               action2=secondbutton.labelButtons,action3=secondbutton.proverka)
    threeBotton.drawButtonImg(window, text=BLabel3, font_size=50, action1=images.next_picture,
                              action2=threeBotton.labelButtons,action3=threeBotton.proverka)
    fourButton.drawButtonImg(window, text=BLabel4, font_size=50, action1=images.next_picture,
                             action2=fourButton.labelButtons,action3=fourButton.proverka)
    backBut.drawButtonImg(window, action1=backBut.clickStart)
    nextPic.drawButtonImg(window, text=nextPicture, font_size=30, action1=images.next_picture,
                             action2=nextPic.labelButtons)
    images.draw_img(window, 150, 350)
    score.print_text(window,str(buttonImage.ball),1000,45)
