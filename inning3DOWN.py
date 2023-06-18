import pyautogui as pag
from set_button_and_game import *

def inning3DOWN():
    # 1
    kstrike()
    ball()
    ball()
    swing()
    ball()
    ball()

    # 2
    ballStolenBase2()
    KStolenBase3()
    ball()
    ball()
    twobasehit()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xnumbers[7], ynumbers, duration=d)
    pag.leftClick(x3BTN[1], y3BTN, duration=d)
    pag.leftClick(x4BTN[2], y4BTN, duration=d)
    done()
    done()

    # 3
    outon1base()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, duration=d)
    pag.leftClick(xnumbers[0], ynumbers, duration=d)
    pag.leftClick(xnumbers[2], ynumbers, duration=d)
    done()

    # 4
    ball()
    ball()
    foul()
    swing()
    swing()
    done()

    # 5
    ballStolenBase3()
    ball()
    onebasehit()
    pag.leftClick(x2BTN[1], y2BTN, duration=d)
    pag.leftClick(x3BTN[2], y3BTN, duration=d)
    pag.leftClick(xnumbers[5], ynumbers, duration=d)
    pag.mouseDown(xBASE[2], yBASE[2], duration=d)
    pag.moveTo(xBASE[3],yBASE[3], duration=d)
    pag.mouseUp()
    done()

    # # 6
    KStolenBase2()
    kstrike()
    ball()
    foul()
    outon1base()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xnumbers[5], ynumbers, duration=d )
    pag.leftClick(xnumbers[2],ynumbers, duration=d)
    done()