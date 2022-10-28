import pyautogui 
import time 
import sys 
from datetime import datetime 
pyautogui.FAILSAFE = False 
numMin = 10
 
pyautogui.moveTo(600,1) 
print("Start") 
while(True): 
    x=0 
    while(x<numMin): 
        time.sleep(1) 
        x+=1 
    for i in range(0,45): 
        pyautogui.moveTo(600,i*15) 
    pyautogui.moveTo(600,1) 
    for i in range(0,3): 
        pyautogui.press("shift") 
    print("Movement made at {}".format(datetime.now().time()))

    