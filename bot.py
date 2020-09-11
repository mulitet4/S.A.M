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

if "type" in command.split()[0]:
    to_write = command.split()[1:]
    write_str = ""
    for word in to_write:
        write_str += word + " "
    print(f"typing {write_str}in 2 seconds")
    small_tasks.type_message(write_str)

if "search" in command.split()[0]:
    to_search = command.split()[1:]

#todo
#send email
#search on browser