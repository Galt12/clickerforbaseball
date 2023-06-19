import pyautogui as pag
from set_button_and_game import *

def inning6DOWN():
    # 4
    done()
    threebasehit()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, 0, d)
    pag.leftClick(x4BTN[0], y4BTN, duration=d)
    pag.leftClick(xnumbers[7],ynumbers, duration=d)
    pag.leftClick(xnumbers[8], ynumbers, duration=d)
    done()

    # 5
    onebasehit()
    pag.leftClick(x2BTN[1], y2BTN, duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    pag.leftClick(xnumbers[5],ynumbers, duration=d)
    moveTO_4()
    done()
    # 6
    KStolenBase2()
    ball()
    ball()
    foul()
    done()
    outon1base()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xnumbers[0], ynumbers, duration=d)
    pag.leftClick(xnumbers[2], ynumbers, duration=d)
    done()

    # 7
    onebasehit()
    pag.leftClick(x2BTN[1], y2BTN, duration=d)
    pag.leftClick(x3BTN[1], y3BTN, duration=d)
    pag.leftClick(xnumbers[5],ynumbers, duration=d)
    moveTO_3()
    moveTO_4()
    done()
    done()

    # 8
    hp()
    done()

    # 9
    onebasehit()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, 0, d)
    pag.leftClick(x2BTN[0], y2BTN, 0, d)
    pag.leftClick(xnumbers[7], ynumbers, 0,d)
    moveTO_3()
    done()
    done()

    # 1
    foul()
    ball()
    ball()
    ball()
    swing()
    threebasehit()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, 0, d)
    pag.leftClick(xFIRSTBUTTON[4], yFIRSTBUTTON, 0 ,d)
    pag.leftClick(x4BTN[0], y4BTN, 0, d)
    pag.leftClick(xnumbers[7], ynumbers, 0,d)
    pag.leftClick(xnumbers[8], ynumbers, 0,d)
    done()
    done()
    done()

    # 2
    ball()
    ball()
    done()
    twobasehit()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, 0, d)
    pag.leftClick(x3BTN[0], y3BTN, 0, d)
    pag.leftClick(xnumbers[6], ynumbers, 0,d) 
    done()
    done()

    # 3
    ball()
    ballStolenBase3()
    ball()
    ball()

    # 4
    ballWildPitch_2_4()
    done()
    done()
    twobasehit()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, 0, d)
    pag.leftClick(x3BTN[0], y3BTN, 0, d)
    pag.leftClick(xnumbers[6], ynumbers, 0,d) 
    done()
    done()

    # 5
    kstrike()
    ball()
    done()

    onebasehit()
    pag.leftClick(x2BTN[1], y2BTN, 0, d)
    pag.leftClick(x3BTN[0], y3BTN, 0,d)

    pag.leftClick(xnumbers[6], ynumbers, 0,d)     
    moveTO_3()
    done()
    done()

    # 6
    ballStolenBase2()
    done()
    K_PB_3()
    done()
    done()
    ball()
    ball()
    ball()

    # 7
    foul()
    done()

    outon1base()
    pag.leftClick(x2BTN[0], y2BTN, 0, d)
    pag.leftClick(xnumbers[0], ynumbers, 0,d)
    pag.leftClick(xnumbers[2], ynumbers, 0,d)   
    moveTO_4()
    done()
    done()

    # 8
    ball()
    ballStolenBase3()
    done()
    outon1base()
    pag.leftClick(x2BTN[0], y2BTN, 0, d)
    pag.leftClick(xnumbers[0], ynumbers, 0,d)
    pag.leftClick(xnumbers[2], ynumbers, 0,d) 
    done()
