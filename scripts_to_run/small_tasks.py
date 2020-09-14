import pyautogui
from time import sleep
import webbrowser

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
def search_web(query: str):
    webbrowser.get().open_new_tab(f'https://www.google.com/search?q={query}')
    
#to-do // send email