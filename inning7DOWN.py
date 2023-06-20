import pyautogui as pag
from set_button_and_game import *


def inning7DOWN():
    # 9
    ball()
    ball()
    ball()
    ball()

    # 1
    KStolenBase2()
    kstrike()
    ballStolenBase3()
    outon1base()
    pag.leftClick(xFIRSTBUTTON[1],yFIRSTBUTTON, 0, d)
    pag.leftClick(xnumbers[8], ynumbers, 0, d)
    moveTO_4()
    done()
    done()

    # 2
    kstrike()
    kstrike()
    ball()
    ball()
    onebasehit()
    pag.leftClick(xFIRSTBUTTON[1],yFIRSTBUTTON, 0, d)
    pag.leftClick(x2BTN[0], y2BTN,0,d)
    pag.leftClick(xnumbers[6],ynumbers,0,d)
    done()

    # 3
    ballStolenBase2()
    done()
    ballStolenBase3()
    done()
    kstrike()
    kstrike()
    ball()
    done()

    # 4
    foul()
    ball()
    ball()
    swing()
    ball()
    swing()
    done()

    # 5
    kstrike()
    ball()
    swing()
    swing()
    done()
