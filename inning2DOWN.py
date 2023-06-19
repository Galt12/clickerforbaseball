import pyautogui as pag
from set_button_and_game import *

def inning2DOWN():
    # 6
    kstrike()
    ball()
    outon1base()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(xnumbers[3], ynumbers, duration=d)
    pag.leftClick(xnumbers[2], ynumbers, duration=d)

    done()
    # 7
    ball()
    ball()
    ball()
    ball()
    # 8
    foul()
    ballStolenBase2()
    foul()
    ball()
    kstrike()
    # 9
    swing()
    swing()
    swing()
