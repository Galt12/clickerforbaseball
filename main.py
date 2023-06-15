import pyautogui as pag
from set_button_and_game import *
from firstinningUP import firstinningUP
from firstinningDOWN import firstinningDOWN
from inning2UP import inning2UP
# pag.dragTo(50, 200, 2, button='left')
print(pag.position())
# ДОМ
x = 515
y = 349

if __name__=='__main__':
    firstinningUP()
    firstinningDOWN()
    inning2UP()


