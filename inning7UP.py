import pyautogui as pag
from set_button_and_game import *

def inning7UP():
    # 1
    kstrike()
    ball()
    done()
    twobasehit()
    pag.leftClick(x2BTN[1], y2BTN,0,d)
    pag.leftClick(x3BTN[0], y3BTN, 0,d)
    pag.leftClick(xnumbers[0], ynumbers, 0,d)
    pag.leftClick(x3BTN[3], y3BTN,0,d)
    done()

    # 2
    kstrike()
    B_e2T_3()
    done()
    ball()
    ball()
    ball()
    done()

    # 3
    done()
    K_SB2_full_is_3()
    
    done()
    ball()
    ball()
    foul()
    done()
    outon1base()
    pag.leftClick(x2BTN[0], y2BTN,0,d)
    pag.leftClick(xnumbers[0], ynumbers,0,d)
    pag.leftClick(xnumbers[2], ynumbers,0,d)
    moveTO_3()
    done()
    done()

    # 4
    ball()
    ball()
    kstrike()
    ball()
    foul()
    done()

    onebasehit()
    pag.leftClick(x2BTN[1], y2BTN,0,d)
    pag.leftClick(x3BTN[0], y3BTN, 0,d)
    pag.leftClick(xnumbers[3], ynumbers, 0,d)
    moveTO_4()
    done()
    done()

    # 5
    pickoff1()
    ballStolenBase2()
    kstrike()
    foul()
    done()
    onebasehit()
    pag.leftClick(x2BTN[0], y2BTN,0,d)
    pag.leftClick(xnumbers[3], ynumbers, 0,d)  
    pag.mouseDown(xBASE[2], yBASE[2],'left',d)
    pag.moveTo(xBASE[1], yBASE[1],0,d)
    pag.mouseUp()
    done()  
    done()

    # 6
    done()
    onebasehit()
    pag.leftClick(xFIRSTBUTTON[2], yFIRSTBUTTON,0,d)
    pag.leftClick(x2BTN[0], y2BTN,0,d)
    pag.leftClick(xFIRSTBUTTON[4], yFIRSTBUTTON,0,d)
    pag.leftClick(xnumbers[6], ynumbers, 0,d)  
    done()
    done()
    # 7
    swing()
    ball()
    ball()
    ball()
    swing()
    done()
    onebasehit()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON,0,d)
    pag.leftClick(x2BTN[0], y2BTN,0,d)
    pag.leftClick(xFIRSTBUTTON[4], yFIRSTBUTTON,0,d) 
    pag.leftClick(xnumbers[8], ynumbers, 0,d)  

    done()
    done()

    8
    foul()
    swing()
    ball()
    done()
    onebasehit()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON,0,d)
    pag.leftClick(x2BTN[0], y2BTN,0,d)    
    pag.leftClick(xFIRSTBUTTON[4], yFIRSTBUTTON,0,d)

    pag.leftClick(xnumbers[7], ynumbers, 0,d)  

    done()
    done()

    # 9 
    swing()
    ball()
    ball()
    ball()
    ball()
    done()
    done()

    # 1
    kstrike()
    done()
    onebasehit()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON,0,d)
    pag.leftClick(x2BTN[0], y2BTN,0,d)
    pag.leftClick(xFIRSTBUTTON[4], yFIRSTBUTTON,0,d)

    pag.leftClick(xnumbers[8], ynumbers, 0,d)  
    moveTO_3()
    pag.leftClick(xFIRSTBUTTON[4], yFIRSTBUTTON,0,d)    
    done()
    done()
    done()
    done()

    # 2
    kstrike()
    ball()
    foul()
    done()

    onebasehit()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON,0,d)
    pag.leftClick(x2BTN[0], y2BTN,0,d)
    pag.leftClick(xFIRSTBUTTON[4], yFIRSTBUTTON,0,d)

    pag.leftClick(xnumbers[4], ynumbers, 0,d)

    done()
    done()

    # 3
    foul()
    ball()
    swing()
    ball()
    done()
    onebasehit()
    pag.leftClick(x2BTN[0], y2BTN,0,d)
    pag.leftClick(xnumbers[5], ynumbers, 0,d)   
    moveTO_3()
    done()
    done()
    done()

    # 4
    pickoff1()
    B_SB2_full_is_3()
    done()
    twobasehit()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON,0,d)
    pag.leftClick(x3BTN[0], y3BTN,0,d)
    pag.leftClick(xFIRSTBUTTON[4], yFIRSTBUTTON,0,d)

    pag.leftClick(xnumbers[6], ynumbers, 0,d)
    done()
    done()
    done()

    # 5
    kstrike()
    ball()
    done()
    onebasehit()
    pag.leftClick(x2BTN[0], y2BTN,0,d)
    pag.leftClick(xnumbers[8], ynumbers, 0,d)
    done()

    # 6
    S_SB2_full_is_3()
    swing()
    foul()
    pickoff2()
    done()
    onebasehit()
    pag.leftClick(x2BTN[0], y2BTN,0,d)
    pag.leftClick(xnumbers[8], ynumbers, 0,d)
    done()
    done()
    done()

    # 7

    twobasehit()
    pag.leftClick(xFIRSTBUTTON[1], yFIRSTBUTTON,0,d)
    pag.leftClick(x3BTN[0], y3BTN,0,d)
    pag.leftClick(xFIRSTBUTTON[4], yFIRSTBUTTON,0,d)
    pag.leftClick(xnumbers[6], ynumbers, 0,d)
    pag.leftClick(xnumbers[7], ynumbers,0,d)
    moveTO_4()
    done()
    done()
    done()

    # 8
    done()
    outon1base()
    pag.leftClick(x2BTN[0], y2BTN,0,d)
    pag.leftClick(xnumbers[0], ynumbers, 0,d)
    pag.leftClick(xnumbers[2], ynumbers, 0,d)
    moveTO_3()
    pag.mouseDown(xBASE[2],yBASE[2],button='primary', duration=d)
    pag.moveTo(xOUT[3],yOUT[3], d)
    pag.mouseUp()

    done()
    done()
    done()




