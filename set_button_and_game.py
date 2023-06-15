import pyautogui as pag
x = 515
y =349

# цифры аутов или хитов
xnumbers = [580, 605, 630, 655, 680, 705, 730, 755, 780] 
ynumbers = 430

# первый ряд кнопок
xFIRSTBUTTON = [50, 150, 250,350, 450, 550]
yFIRSTBUTTON = 480

# второвй ряд кнопок
x2BTN = [150, 250, 350, 450, 550]
y2BTN = 520


# координаты баз, БЕЗ ДОМА!!!!!
xBASE =[712, 509, 300, 427, 603]
yBASE = [260, 215, 267, 407, 411]

# координаты аутов 
xOUT =[667]
yOUT = [342]
def done():
    x1 = 95
    y1 =735
    pag.leftClick(x1, y1)
def onebasehit():
    pag.mouseDown(x, y, button='left')
    pag.moveTo(xBASE[0], yBASE[0], 2)
    pag.mouseUp()

def twobasehit():
    pag.mouseDown(x, y, button='left')
    pag.moveTo(xBASE[1], yBASE[1], 2)
    pag.mouseUp()
def threebasehit():
    pag.mouseDown(x, y, button='left')
    pag.moveTo(xBASE[2], yBASE[2], 2)
    pag.mouseUp()

def homerun():
    pag.mouseDown(x, y, button='left')
    pag.moveTo(xBASE[3], yBASE[3], 1)
    pag.mouseUp()

def outon1base():
    pag.mouseDown(x, y, button='left')
    pag.moveTo(xOUT[0], yOUT[0], 1)
    pag.mouseUp()

def ball():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=0.5)
    done()

def ballStolenBase2():
    pag.leftClick(xFIRSTBUTTON[0], yFIRSTBUTTON, duration=0.5)
    pag.mouseDown(xBASE[0], yBASE[0], button= "left")
    pag.moveTo(xBASE[1], yBASE[1], 2)
    pag.mouseUp()
    pag.leftClick(x2BTN[0], y2BTN, duration=1)
    done()

def swing():
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON, duration=1)
    done()

def kstrike():
    pag.leftClick(xFIRSTBUTTON[2], yFIRSTBUTTON, duration=1)
    done()

def KStolenBase3():
    pag.leftClick(xFIRSTBUTTON[2], yFIRSTBUTTON, duration=1)
    pag.mouseDown(xBASE[1], yBASE[1], button= "left")
    pag.moveTo(xBASE[2], yBASE[2], 2)
    pag.mouseUp()
    pag.leftClick(x2BTN[0], y2BTN, duration=1)
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