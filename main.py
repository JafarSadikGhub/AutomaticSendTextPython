import pyautogui
import time
times = 300
while times>0:
    time.sleep(0.5)
    pyautogui.write('Message text')
    time.sleep(0.5)
    pyautogui.press('enter')
    
