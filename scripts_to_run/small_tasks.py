import pyautogui
from time import sleep

def type_message(msg:str):
    sleep(3)
    pyautogui.write(msg)
    pyautogui.press("enter")