import pyautogui as pag
# ДОМ
xhome = 511
yhome = 352

# Длительность движений мыши. Зависит от возможностей системы.
# НЕ СТАВИТЬ РАВНЫМ 0. Программа не успеет!!!!
d = 2
# цифры аутов или хитов
xnumbers = [580, 605, 630, 655, 680, 705, 730, 755, 780] 
ynumbers = 430

# первый ряд кнопок
xFIRSTBUTTON = [50, 150, 250,350, 450, 550]
yFIRSTBUTTON = 480

# второвй ряд кнопок
x2BTN = [150, 250, 350, 450, 550]
y2BTN = 520

single = pag.leftClick(x2BTN[0], y2BTN, duration=d)
# третий ряд кнопок
x3BTN = [150, 250, 350, 450, 550]
y3BTN = 570

# четверный ряд кнопок
x4BTN = [150, 250, 350, 450, 550]
y4BTN = 610

# пятый ряд кнопок
x5BTN = [150, 250, 350, 450, 550]
y5BTN = 650

# шестой ряд кнопок
x6BTN = [150, 250, 350, 450, 550]
y6BTN = 610

# координаты баз, БЕЗ ДОМА!!!!!
xBASE =[712, 509, 292, 430, 603]
yBASE = [260, 215, 259, 389, 411]

# координаты аутов 
xOUT =[667,630, 373, 327]
yOUT = [342,238, 276, 361]
def done():
    x1 = 95
    y1 =735
    pag.leftClick(x1, y1, duration=d)
def onebasehit():
    pag.mouseDown(xhome, yhome, button='left')
    pag.moveTo(xBASE[0], yBASE[0], d)
    pag.mouseUp()

def twobasehit():
    pag.mouseDown(xhome, yhome, button='left')
    pag.moveTo(xBASE[1], yBASE[1], d)
    pag.mouseUp()

def threebasehit():
    pag.mouseDown(xhome, yhome, button='left')
    pag.moveTo(xBASE[2], yBASE[2], d)
    pag.mouseUp()

def homerun():
    pag.mouseDown(xhome, yhome, button='left')
    pag.moveTo(xBASE[3], yBASE[3], d)
    pag.mouseUp()

def outon1base():
    pag.mouseDown(xhome, yhome, button='left')
    pag.moveTo(xOUT[0], yOUT[0], d)
    pag.mouseUp()

def ball():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    done()

def ballStolenBase2():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    moveTO_2()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    done()

def ballStolenBase3():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    moveTO_3()
    pag.leftClick(x2BTN[0], y2BTN, duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    done()

def ballWildPitch2():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    moveTO_2()
    pag.leftClick(x2BTN[3], y2BTN, duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    done()

def ballWildPitch3():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    moveTO_3()
    pag.leftClick(x2BTN[3], y2BTN, duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    done()

def ballWildPitch4():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    moveTO_4()
    pag.leftClick(x2BTN[3], y2BTN, duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    done()

def ballWildPitch_2_4():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    moveTO_2()
    pag.leftClick(x2BTN[3], y2BTN, duration=d)
    pag.leftClick(x3BTN[0], y3BTN, duration=d)
    moveTO_4()
    done()

def B_e2T_3():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    moveTO_3()
    pag.leftClick(x2BTN[2], y2BTN, duration=d)
    pag.leftClick(x3BTN[3], y3BTN, duration=d)
    pag.leftClick(xnumbers[1], ynumbers,0,d)
    done()

def B_SB2_full_is_3():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=1)
    moveTO_2()
    pag.leftClick(x2BTN[0], y2BTN, duration=1)
    pag.leftClick(x3BTN[0], y3BTN, duration=1)
    done()

def swing():
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, duration=d)
    done()

def S_SB_2():
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, duration=1)
    moveTO_2()
    pag.leftClick(x2BTN[0], y2BTN, duration=1)
    done()

def S_SB2_full_is_3():
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, duration=1)
    moveTO_2()
    pag.leftClick(x2BTN[0], y2BTN, duration=1)
    pag.leftClick(x3BTN[0], y3BTN, duration=1)
    done()

def swingpastball():
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, duration=d)
    pag.mouseDown(xOUT[0],yOUT[0], button = 'left')
    pag.moveTo(xBASE[0], yBASE[0], duration=d)
    pag.mouseUp()
    pag.leftClick(x2BTN[3], y2BTN, duration=d)

def kstrike():
    pag.leftClick(xFIRSTBUTTON[2], yFIRSTBUTTON, duration=1)
    done()

def KStolenBase2():
    pag.leftClick(xFIRSTBUTTON[2], yFIRSTBUTTON, duration=1)
    moveTO_2()
    pag.leftClick(x2BTN[0], y2BTN, duration=1)
    done()

def K_SB_2_e2T():
    pag.leftClick(xFIRSTBUTTON[2], yFIRSTBUTTON, duration=1)
    moveTO_2()
    moveTO_3()
    pag.leftClick(x2BTN[0], y2BTN, duration=1)
    pag.leftClick(x3BTN[2],y3BTN, duration=d)
    pag.leftClick(x4BTN[2], y4BTN, duration=d )
    done()

def K_SB2_full_is_3():
    pag.leftClick(xFIRSTBUTTON[2], yFIRSTBUTTON, duration=1)
    moveTO_2()
    pag.leftClick(x2BTN[0], y2BTN, duration=1)
    pag.leftClick(x3BTN[0], y3BTN, duration=1)
    done()

def KStolenBase3():
    pag.leftClick(xFIRSTBUTTON[2], yFIRSTBUTTON, duration=1)
    moveTO_3()
    pag.leftClick(x2BTN[0], y2BTN, duration=1)
    done()

def K_PB_3():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    moveTO_3()
    pag.leftClick(x2BTN[3], y2BTN, duration=d)
    pag.leftClick(x3BTN[1], y3BTN, duration=d)
    done()

def ballPastBall2():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    moveTO_2()
    pag.leftClick(x2BTN[3], y2BTN, duration=d)
    pag.leftClick(x3BTN[1], y3BTN, duration=d)
    done()

def ballPastBall3():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    moveTO_3()
    pag.leftClick(x2BTN[3], y2BTN, duration=d)
    pag.leftClick(x3BTN[1], y3BTN, duration=d)
    done()

def ballPastBall4():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=d)
    moveTO_4()
    pag.leftClick(x2BTN[3], y2BTN, duration=d)
    pag.leftClick(x3BTN[1], y3BTN, duration=d)
    done()

def foul():
    pag.leftClick(xFIRSTBUTTON[3], yFIRSTBUTTON, duration=1)
    done()

def hp():
    pag.leftClick(xFIRSTBUTTON[4], yFIRSTBUTTON, duration=1)
    done()

def pickoff1():
    pag.leftClick(xBASE[0], yBASE[0], duration=1)
    pag.leftClick(x2BTN[0], y2BTN)
    done()

def pickoff2():
    pag.leftClick(xBASE[1], yBASE[1], duration=1)
    pag.leftClick(x2BTN[0], y2BTN)
    done()


def pickoff3():
    pag.leftClick(xBASE[2], yBASE[2], duration=1)
    pag.leftClick(x2BTN[0], y2BTN)
    done()

def moveTO_2():
    pag.mouseDown(xBASE[0], yBASE[0], button= "left")
    pag.moveTo(xBASE[1], yBASE[1], d)
    pag.mouseUp()

def moveTO_3():
    pag.mouseDown(xBASE[1], yBASE[1], button= "left")
    pag.moveTo(xBASE[2], yBASE[2], d)
    pag.mouseUp(duration=d)

def moveTO_4():
    pag.mouseDown(xBASE[2], yBASE[2], button= "left")
    pag.moveTo(xBASE[3], yBASE[3], d)
    pag.mouseUp()