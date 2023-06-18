import pyautogui as pag
from set_button_and_game import *

def inning4DOWN():
    # 7
    hp()
    
    # 8
    KStolenBase2()
    swing()
    ball()
    ball()
    ballWildPitch3()
    swing()
    done()

    # 9
    ball()
    ball()
    foul()
    swing()
    ball()
    twobasehit()
    pag.leftClick(x2BTN[1], y2BTN, duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    pag.leftClick(xnumbers[3], ynumbers, duration=d)
    pag.leftClick(x3BTN[3], y3BTN, duration=d)
    moveTO_4()
    done()

    # 1
    foul()
    kstrike()
    hp()

    # 2
    onebasehit()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xnumbers[7], ynumbers, duration=d)
    
    # 3
    onebasehit()

    pag.leftClick(xBASE[1], yBASE[1], duration=d)
    pag.leftClick(x2BTN[3], y2BTN, duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    pag.leftClick(xnumbers[5], ynumbers, duration=d)
    done()
    done()
    done()
    done()

    # 4
    ball()
    ball()
    onebasehit()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, duration=d)
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xFIRSTBUTTON[4], yFIRSTBUTTON, duration=d)

    pag.leftClick(xnumbers[7], ynumbers, duration=d)
    done()
    done()

    # 5
    ball()
    foul()
    ball()
    foul()
    threebasehit()
    pag.leftClick(x2BTN[1], y2BTN, duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    pag.leftClick(xnumbers[5], ynumbers, duration=d)
    pag.leftClick(x3BTN[3], y3BTN, duration=d)
    pag.leftClick(x4BTN[3], y4BTN, duration=d)
    done()
    pag.leftClick(x4BTN[0], y4BTN, duration=d)
    done()
    done()
    done()

    # 6
    foul()
    kstrike()
    outon1base()
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    pag.leftClick(xnumbers[2], ynumbers, duration=d)
    done()

    # # 7
    swing()
    outon1base()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xnumbers[2], ynumbers, duration=d)
    done()
    
    print("закончили низ 4")