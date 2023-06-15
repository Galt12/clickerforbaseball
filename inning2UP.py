import pyautogui as pag
from set_button_and_game import *

def inning2UP():
    # 9
    kstrike()
    foul()
    onebasehit()
    pag.leftClick(x2BTN[0], y2BTN, duration=1)
    pag.leftClick(xnumbers[7], ynumbers, duration=1)
    done()
    # 1
    ballStolenBase2()
    swing()
    kstrike()
    outon1base()
    pag.leftClick(x2BTN[1], y2BTN, duration=1)
    pag.leftClick(xnumbers[0], ynumbers)
    done()
    # 2
    outon1base()
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=1)
    pag.leftClick(xnumbers[6],ynumbers, duration=1)
    done()
    # 3
    foul()
    ball()
    foul()
    onebasehit()
    pag.leftClick(x2BTN[0], y2BTN, duration=1)
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, duration=1)
    pag.leftClick(xnumbers[6], ynumbers, duration=1)
    pag.mouseDown(xBASE[2], yBASE[2], button="left")
    pag.moveTo(xBASE[3], yBASE[3], duration=1)
    pag.mouseUp()
    done()
    done()
    # 4
    swing()
    outon1base()
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=1)
    pag.leftClick(xnumbers[4], ynumbers, duration=1)
    done()
