import pyautogui as pag
from set_button_and_game import *

def firstinningUP():
    # 1 бьющий
    kstrike()
    ball()
    # координаты дома
    x = 510
    y =348
    # координаты аута на 1 базе
    outon1base()
    xfoul = 239
    yfoul = 521
    pag.leftClick(xfoul, yfoul, duration=1)
    pag.leftClick(755, 426, duration=1)
    done()

    # # 2 бьющий
    ball()
    ball()
    kstrike()
    ball()
    ball()

    # # 3 бьющий (удар с первого, однобазовый хит с продвижением до 2 по ошибке 7)
    twobasehit()
    xsingle= 135
    ysingle = 520
    pag.leftClick(xsingle, ysingle, duration=1)
    pag.leftClick(727, 425)
    x2error = 245
    y2error = 565
    pag.leftClick(x2error, y2error, duration=1)
    x3error = 330
    y3error = 600
    pag.leftClick(x3error, y3error, duration=1)
    done()
    done()
    # 4 бьющий
    onebasehit()
    xsingle= 135
    ysingle = 520
    pag.leftClick(xsingle, ysingle, duration=1)
    pag.leftClick(655, 430, duration=1)
    done()
    done()
    # # 5 
    kstrike()
    ball()
    ball()
    ball()
    foul()
    ball()
    done()
    # # 6
    kstrike()
    swing()
    swing()
    done()
    # 7 
    ball()
    foul()
    onebasehit()
    pag.leftClick(x2BTN[0], y2BTN, duration=1)
    pag.leftClick(xnumbers[7], ynumbers, duration=1)
    done()
    done()
    # 8 (аут бегуну в дом)
    onebasehit()
    x3out = 333
    y3out = 357
    x4scored = 435
    y4scored = 393   
    x1 = 712
    y1 = 260

    pag.mouseDown(x, y, button='left')
    pag.moveTo(x1, y1, 2)
    pag.mouseUp()
   
    pag.mouseDown(x4scored, y4scored, button='left')
    pag.moveTo(x3out, y3out, 2)
    pag.mouseUp()
    pag.leftClick(xnumbers[0],ynumbers,duration=1)
    pag.leftClick(xnumbers[1],ynumbers, duration=1)
    done()
    pag.leftClick(xsingle, ysingle, duration=1)
    done()
    pag.leftClick(xsingle, ysingle, duration=1)
    done()
    pag.leftClick(xsingle, ysingle, duration=1)
    done()
    done()  