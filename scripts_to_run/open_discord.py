import pyautogui
import time

auto_msg = "I am a bot, and this action was performed using a script that mulitate4#9118 that takes voice input and does actions. So when you say - Open Discord, it opens discord and sends this message :)"

def open_discord_fnc(server):
    pyautogui.hotkey("win", "s")
    time.sleep(0.3)
    pyautogui.write("discord")
    time.sleep(0.3)
    pyautogui.press("enter")

    if server == "hh":
        while True:
            time.sleep(1)
            hh_logo = pyautogui.locateOnScreen("icons/hh_logo.png")
            if not hh_logo:
                hh_logo = pyautogui.locateOnScreen("icons/hh_highlighted_logo.png")
            elif not hh_logo:
                hh_logo = pyautogui.locateCenterOnScreen("icons/hh_highlighted_alert_logo.png")
            
            if not hh_logo:
                continue
            else:
                break
        pyautogui.moveTo(hh_logo, duration=0.1)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.write(auto_msg)
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
        pyautogui.write(auto_msg)
        pyautogui.press("enter")

    elif server == "priyam":
        while True:
            time.sleep(1)
            p_logo = pyautogui.locateOnScreen("icons/priom_logo.png")
            if not p_logo:
                p_logo = pyautogui.locateOnScreen("icons/priom_highlighted_logo.png")
            
            if not p_logo:
                continue
            else:
                break
    
        pyautogui.moveTo(p_logo, duration=0.1)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.write(auto_msg)
        pyautogui.press("enter")


open_discord_fnc(server="priyam")