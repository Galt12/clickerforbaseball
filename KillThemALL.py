import pyautogui as pag
def deleteall():
    
    x1 = 295
    y1 =777
    for count in range (1, 15):
        pag.leftClick(x1, y1, duration=0.5)
        if count % 10 == 0:
            print(count)
        
deleteall()

# 150