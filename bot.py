import os
from time import sleep

from scripts_to_run import recognize_speech
from scripts_to_run import open_discord
from scripts_to_run import small_tasks

command = recognize_speech.recognize()

print(f"I think you said: {command}")

if "open" in command.split()[0]:
    to_open = command.split()[1:]
    app_str = ""
    for word in to_open:
        app_str += word + " "
    print(f"opening {app_str}\b....")
    small_tasks.search_app(app_str)
