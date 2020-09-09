import os
from time import sleep

import recognize_speech
from scripts_to_run import open_discord
from scripts_to_run import small_tasks

command = recognize_speech.recognize()

print(f"I think you said: {command}")
if command == "open discord":
    open_discord.open_discord_fnc(server="priyam")