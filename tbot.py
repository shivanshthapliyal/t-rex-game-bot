
from PIL import ImageOps
import pyscreenshot as ImageGrab
import pyautogui, time
from numpy import *


class Coordinates():
    replayBtn = (517,517)
    dino = (215,530)
    #coordinate for point where dino should jump if obstacle appears
    x=282
    #coordinate to check for lowest obstacle
    y=561



def restartGame():
    pyautogui.click(Coordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')

def imageGrab():
    box = (Coordinates.dino[0]+240,Coordinates.dino[1],Coordinates.dino[0]+240+40,Coordinates.dino[1]+30)
    # box = (dinoCOrd.X + distance, dinoCord.Y, dinoCOrd.X + distance + 40, dinoCord.Y + 30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())

    return a.sum()

# while True:
#     imageGrab()


def main():
    restartGame()
    while True:
        if(imageGrab()!=1447):
            pressSpace()
            time.sleep(0.1)

main()

# restartGame()
# time.sleep(1)
# pressSpace()