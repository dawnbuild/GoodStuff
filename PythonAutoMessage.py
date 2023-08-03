import pyautogui
import time as t
import keyboard
import random

owo_text = "wh"
def anjay():
    rnum= random.randint(0,3)
    rtime= random.randint(15,16)
    print("random number:",rnum)
    print("random time:",rtime)
    if (rnum==0):
        t.sleep(rtime)
        pyautogui.typewrite("wh")
        keyboard.press_and_release('enter')
    elif (rnum==1):
        t.sleep(rtime)
        pyautogui.typewrite("w h")
        keyboard.press_and_release('enter')
    elif (rnum==2):
        t.sleep(rtime)
        pyautogui.typewrite("w battle")
        keyboard.press_and_release('enter')
    elif (rnum==3):
        t.sleep(rtime)
        pyautogui.typewrite("w hunt")
        keyboard.press_and_release('enter')

t.sleep(5)
pyautogui.typewrite("lessgooo")
keyboard.press_and_release('enter')
while True:
    anjay()
