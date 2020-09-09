import pyautogui
from time import sleep

def type_message(msg:str):
    sleep(3)
    pyautogui.write(msg)
    pyautogui.press("enter")

def search_app(app:str):
    pyautogui.hotkey("win", "s")
    sleep(0.3)
    pyautogui.write(app)
    sleep(0.3)
    pyautogui.press("enter")

#to-do // search online on browser
#to-do // send email