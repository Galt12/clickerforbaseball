import pyautogui as pag
from set_button_and_game import *

def firstinningDOWN():
    # 1
    ball()
    ball()
    kstrike()
    ball()
    swing()
    onebasehit()

    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xnumbers[4], ynumbers, duration=d) 
    done()
    # 2
    ballStolenBase2()
    KStolenBase3()
    outon1base()
    pag.leftClick(x2BTN[1], y2BTN, duration=d)
    pag.leftClick(xnumbers[4], ynumbers, duration=d)
    done()
    # 3
    swing()
    kstrike()
    outon1base()
    pag.leftClick(x2BTN[1], y2BTN, duration=d)
    pag.leftClick(xnumbers[7], ynumbers, duration=d)
    moveTO_3()
    done()
    done()
    done()
    # 4
    foul()
    ball()
    ball()
    ball()
    foul()
    ball()
    5
    pickoff1()
    ballStolenBase2()
    outon1base()
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    pag.leftClick(xnumbers[4], ynumbers)
    done()