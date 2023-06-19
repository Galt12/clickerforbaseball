import pyautogui as pag
from set_button_and_game import *
from firstinningUP import firstinningUP
from firstinningDOWN import firstinningDOWN
from inning2UP import inning2UP
from inning2DOWN import inning2DOWN
from inning3UP import inning3UP
from inning3DOWN import inning3DOWN
from inning4UP  import inning4UP
from inning4DOWN import inning4DOWN
from inning5UP import inning5UP
from inning5DOWN import inning5DOWN
from inning6UP import inning6UP
from inning6DOWN import inning6DOWN
from inning7UP import inning7UP


if __name__ == '__main__':
    for func in [ 
                firstinningDOWN,
                inning2UP,
                inning2DOWN,
                inning3UP,
                inning3DOWN,
                inning4UP, 
                inning4DOWN, 
                inning5UP, 
                inning5DOWN, 
                inning6UP, 
                inning6DOWN,
                inning7UP]:
        func()
        print(f"Закончили {func.__name__}!")
