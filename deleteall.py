import pyautogui as pag
def deleteall():
    count = 0
    x1 = 295
    y1 =777
    while count <40:
        pag.leftClick(x1, y1, duration=0.5)
        count += 1
        print(count)
        
deleteall()