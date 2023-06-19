import pyautogui as pag
from set_button_and_game import *


def inning5DOWN():
    # # 8
    kstrike()
    ball()
    kstrike()
    foul()
    foul()
    swing()

    # 9
    kstrike()
    ball()
    ball()
    swing()
    done()
    onebasehit()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xnumbers[3], ynumbers, duration=d)
    done()

    # 1
    KStolenBase2()
    swing()
    foul()
    swing()
    done()
    done()

    # 2
    homerun()
    pag.leftClick(x2BTN[1], y2BTN, duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    pag.leftClick(xnumbers[7], ynumbers, duration=d)
    pag.leftClick(x3BTN[3], y3BTN, duration=d)
    pag.leftClick(x4BTN[3], y4BTN, duration=d)
    pag.leftClick(x5BTN[3], y5BTN, duration=d)
    done()
    done()

    # 3
    ball()
    done()
    outon1base()
    pag.leftClick(x2BTN[1], y2BTN, duration=d)
    pag.leftClick(xnumbers[4], ynumbers, duration=d)
    done()


