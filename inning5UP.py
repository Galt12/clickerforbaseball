import pyautogui as pag
from set_button_and_game import *

def inning5UP():
    # sub attack
    pag.leftClick(887, 389, duration=d)
    pag.leftClick(974, 392, duration=d)
    pag.leftClick(923,221,duration=d)

    # sub deffense
    pag.leftClick(955, 47, duration=d)
    pag.leftClick(922, 251,duration=d)
    pag.leftClick(974, 241,duration=d)
    pag.leftClick(894,365,duration=d)

    done()

    # 9 
    kstrike()
    ball()
    ball()
    ball()
    kstrike()
    outon1base()
    pag.leftClick(xFIRSTBUTTON[2], yFIRSTBUTTON, duration=d)
    pag.leftClick(x2BTN[1],y2BTN, duration=d)
    pag.leftClick(xnumbers[3],ynumbers,duration=d)
    done()

    # 1
    ball()
    kstrike()
    swing()
    done()
    homerun()
    pag.leftClick(x2BTN[0],y2BTN, duration=d)
    pag.leftClick(xnumbers[4], ynumbers, duration=d)
    pag.leftClick(x3BTN[1],y3BTN, duration=d)
    pag.leftClick(x4BTN[1],y4BTN, duration=d)
    pag.leftClick(x4BTN[3],y4BTN, duration=d)
    pag.leftClick(x5BTN[3],y5BTN, duration=d)
    pag.leftClick(x6BTN[1],y6BTN, duration=d)
    done()

    # 2
    onebasehit()
    pag.leftClick(x2BTN[0],y2BTN, duration=d)
    pag.leftClick(xnumbers[6], ynumbers, duration=d)
    done()

    # 3
    ball()
    ballStolenBase2()
    onebasehit()


    pag.leftClick(xFIRSTBUTTON[1],yFIRSTBUTTON, duration=d)
    pag.leftClick(x2BTN[0],y2BTN, duration=d)
    pag.leftClick(xnumbers[7], ynumbers, duration=d)
    pag.leftClick(xnumbers[8], ynumbers, duration=d)
    done()
    done()

    # 3
    pickoff1()
    ball()
    swing()
    swing()
    ball()
    ball()
    kstrike()
    done()

    # 4
    ball()
    ball()
    foul()
    kstrike()
    kstrike()
    done()
