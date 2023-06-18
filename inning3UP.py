import pyautogui as pag
from set_button_and_game import *

d = 1

def inning3UP():
    # 5
    ball()
    foul()
    ball()
    ball()
    foul()
    
    outon1base()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xnumbers[2],ynumbers, duration=d)
    done()
    # 6
    ball()
    ball()
    kstrike()
    foul()
    swingpastball()
    done()
    # 7
    twobasehit()
    pag.leftClick(xFIRSTBUTTON[1],yFIRSTBUTTON,duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    pag.leftClick(xnumbers[7], ynumbers, duration=d)
    done()

    # 8
    foul()
    twobasehit()
    pag.leftClick(xFIRSTBUTTON[2],yFIRSTBUTTON,duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    pag.leftClick(xnumbers[7], ynumbers, duration=d)
    done()
    done()
    done()
    done()

    # 9
    ball()
    swing()
    kstrike()
    kstrike()
    done()

    # 1
    outon1base()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, duration=d)
    pag.leftClick(xnumbers[7],ynumbers, duration=d)
    done()
