import pyautogui as pag
from set_button_and_game import *

def inning6UP():
    # 6
    kstrike()
    done()
    outon1base()
    pag.leftClick(x2BTN[1],y2BTN, duration=d)
    pag.leftClick(xnumbers[3],ynumbers, duration=d)    
    done()
    # 7
    foul()
    done()
    outon1base()
    pag.leftClick(x2BTN[1],y2BTN, duration=d)
    pag.leftClick(xnumbers[5],ynumbers, duration=d)    
    done()
    # 8
    ball()
    ball()
    ball()
    done()
    onebasehit()
    pag.leftClick(x2BTN[0],y2BTN, duration=d)
    pag.leftClick(xnumbers[3],ynumbers, duration=d)   
    done()
    # 9
    done()
    onebasehit()
    pag.mouseDown(xBASE[1], yBASE[1], duration=d)
    pag.moveTo(xOUT[1], yOUT[1], duration=d)
    pag.mouseUp()
    pag.leftClick(xnumbers[3],ynumbers, duration=d)   
    pag.leftClick(xnumbers[5],ynumbers, duration=d)   
    done()
    done()