import pyautogui
import time

def open_discord(server):
    pyautogui.hotkey("win", "d")
    time.sleep(0.5)
    discord_logo = pyautogui.locateOnScreen("icons/discord_icon.png")
    if not discord_logo:
        discord_logo = pyautogui.locateOnScreen("icons/discord_highlighted_icon.png")
    pyautogui.moveTo(discord_logo.left + 1, discord_logo.top + 1, duration=0.5)
    pyautogui.doubleClick()

    if server == "hh":
        while True:
            time.sleep(1)
            hh_logo = pyautogui.locateOnScreen("icons/hh_logo.png")
            if not hh_logo:
                hh_logo = pyautogui.locateOnScreen("icons/hh_highlighted_logo.png")
            
            if not hh_logo:
                continue
            else:
                break
        pyautogui.moveTo(shh_logo, duration=0.1)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.write("I am a bot, and this action was performed using a script that mulitate4#9118 wrote in python, ok bye!")
        pyautogui.press("enter")
    
    elif server == "sgr":
        while True:
            time.sleep(1)
            supergamingreport_logo = pyautogui.locateOnScreen("icons/sgr_logo.png")
            if not supergamingreport_logo:
                supergamingreport_logo = pyautogui.locateOnScreen("icons/sgr_highlighted_logo.png")
            
            if not supergamingreport_logo:
                continue
            else:
                break
    
        pyautogui.moveTo(supergamingreport_logo, duration=0.1)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.write("I am a bot, and this action was performed using a script that mulitate4#9118 wrote in python, ok bye!")
        pyautogui.press("enter")
    


open_discord(server="sgr")