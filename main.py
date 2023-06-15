import pyautogui as pag
# pag.dragTo(50, 200, 2, button='left')
print(pag.position())
# x = 515
# y =349

# x1 = 712
# y1 = 260

# pag.mouseDown(x, y, button='left')
# pag.moveTo(x1, y1, 2)
# pag.mouseUp()
def done():
    x1 = 95
    y1 =735
    pag.leftClick(x1, y1)

def ball():
    x = 40
    y = 475
    pag.leftClick(x, y, duration=1)
    done()

def swing():
    x = 145
    y = 475
    pag.leftClick(x, y, duration=1)
    done()

def kstrike():
    x = 245
    y = 475
    pag.leftClick(x, y, duration=1)
    done()

def foul():
    x = 345
    y = 475
    pag.leftClick(x, y, duration=1)
    done()

def hp():
    x = 445
    y = 475
    pag.leftClick(x, y, duration=1)
    done()

def firstinningUP():
    # 1 бьющий
    kstrike()
    ball()
    # координаты дома
    x = 510
    y =348
    # координаты аута на 1 базе
    x1out = 667
    y1out = 342

    pag.mouseDown(x, y, button='left')
    pag.moveTo(x1out, y1out, 2)
    pag.mouseUp()
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
    x2base = 509
    y2base = 215

    pag.mouseDown(x, y, button='left')
    pag.moveTo(x2base, y2base, 2)
    pag.mouseUp()
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
    x1 = 712
    y1 = 260

    pag.mouseDown(x, y, button='left')
    pag.moveTo(x1, y1, 2)
    pag.mouseUp()
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
    x1 = 712
    y1 = 260

    pag.mouseDown(x, y, button='left')
    pag.moveTo(x1, y1, 2)
    pag.mouseUp()
    xsingle= 135
    ysingle = 520
    pag.leftClick(xsingle, ysingle, duration=1)
    pag.leftClick(755, 426, duration=1)
    done()
    done()
    # 8 (аут бегуну в дом)
    pag.mouseDown(x, y, button='left')
    pag.moveTo(x1, y1, 2)
    pag.mouseUp()
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
    pag.leftClick(580,422,duration=1)
    pag.leftClick(600, 422, duration=1)
    done()
    pag.leftClick(xsingle, ysingle, duration=1)
    done()
    pag.leftClick(xsingle, ysingle, duration=1)
    done()
    pag.leftClick(xsingle, ysingle, duration=1)
    done()
    done()  

def firstinningDOWN():
    ball()
    ball()
    kstrike()
    ball()
    swing()
    
if __name__=='__main__':
    firstinningUP()