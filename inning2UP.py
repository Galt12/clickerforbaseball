import pyautogui as pag
from set_button_and_game import *

def inning2UP():
    # 9
    kstrike()
    foul()
    onebasehit()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xnumbers[7], ynumbers, duration=d)
    done()
    # 1
    ballStolenBase2()
    swing()
    kstrike()
    outon1base()
    pag.leftClick(x2BTN[1], y2BTN, duration=d)
    pag.leftClick(xnumbers[0], ynumbers)
    done()
    # 2
    outon1base()
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    pag.leftClick(xnumbers[6],ynumbers, duration=d)
    done()
    # 3
    foul()
    ball()
    foul()
    onebasehit()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, duration=d)
    pag.leftClick(xnumbers[6], ynumbers, duration=d)
    moveTO_4()
    done()
    done()
    # 4
    swing()
    outon1base()
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    pag.leftClick(xnumbers[4], ynumbers, duration=d)
    done()
