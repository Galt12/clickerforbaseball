import pyautogui as pag
from set_button_and_game import *

def inning4UP():
    # 2
    kstrike()
    kstrike()
    outon1base()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xnumbers[5], ynumbers, duration=d)
    pag.leftClick(xnumbers[2], ynumbers, duration=d)
    done()

    # # 3
    onebasehit()
    pag.leftClick(x2BTN[1], y2BTN, duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    pag.leftClick(xnumbers[4], ynumbers, duration=d)
    done()

    # # 4
    outon1base()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xnumbers[2], ynumbers, duration=d)
    done()
    done()
    done()

    # # 5
    pickoff2()
    ball()
    ball()
    ball()
    KStolenBase3()
    ball()
    

    # 6
    twobasehit()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    pag.leftClick(xnumbers[6], ynumbers, duration=d)
    pag.leftClick(xnumbers[7], ynumbers, duration=d)
    done()
    done()
    done()

    # 7
    ballWildPitch3()
    done()
    onebasehit()
    pag.leftClick(x2BTN[1], y2BTN, duration=d)
    pag.leftClick(x3BTN[1], y3BTN, duration=d)
    pag.leftClick(xnumbers[4], ynumbers, duration=d)
    moveTO_4()
    done()
    done()

    # # 8
    K_SB_2_e2T()
    ball()
    outon1base()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, duration=d )
    pag.leftClick(xnumbers[7], ynumbers, duration=d)
    done()
    done()