import pyautogui
import time as t
import keyboard
import random

numa=0
owo_text = "wh"
def anjay():
    global numa
    rnum= random.randint(0,3)
    rtime= random.randint(14,15)
    print("random number:",rnum)
    print("random time:",rtime)
    if (rnum==0):
        t.sleep(rtime)
        pyautogui.typewrite("wh")
        keyboard.press_and_release('enter')
        numa+=1
    elif (rnum==1):
        t.sleep(rtime)
        pyautogui.typewrite("w h")
        keyboard.press_and_release('enter')
        numa+=1
    elif (rnum==2):
        t.sleep(rtime)
        pyautogui.typewrite("w b")
        keyboard.press_and_release('enter')
        numa=0
    elif (rnum==3):
        t.sleep(rtime)
        pyautogui.typewrite("w hunt")
        keyboard.press_and_release('enter')
        numa+=1
    if (numa>=4):
        t.sleep(4)
        pyautogui.typewrite("owo b")
        keyboard.press_and_release('enter')
        numa = 0
t.sleep(5)
pyautogui.typewrite("w hunt")
keyboard.press_and_release('enter')
while True:
    anjay()
