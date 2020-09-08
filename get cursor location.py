import pyautogui, time
from os import system

while True:
    x, y = pyautogui.position()
    ss = pyautogui.screenshot()
    color = ss.getpixel((x, y))
    pos_str = "x: " + str(x).rjust(2) + " y: " + str(y).rjust(2) + " rgb: " + str(color).rjust(2)
    print(pos_str)
    time.sleep(0.1)
    system("cls")