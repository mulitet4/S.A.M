import os
from time import sleep

from scripts_to_run import Song_Downloader
from scripts_to_run import recognize_speech
from scripts_to_run import open_discord
from scripts_to_run import small_tasks

while True:
    command = ""
    song = ""
    x = input("Press enter to give commands: ")
    if not x:
        command = recognize_speech.recognize()

        print(f"I think you said: {command}")

    elif x == "m":
        command = input("Enter Command: ")

    elif x == "q":
        break

    if "open" in command.split()[0]:
        to_open = command.split()[1:]
        app_str = ""
        for word in to_open:
            app_str += word + " "
        print(f"Opening {app_str}\b....")
        small_tasks.search_app(app_str)

    if "type" in command.split()[0]:
        to_write = command.split()[1:]
        write_str = ""
        for word in to_write:
            write_str += word + " "
        print(f"Typing {write_str}in 2 seconds")
        small_tasks.type_message(write_str)

    if "search" in command.split()[0]:
        to_search = command.split()[1:]
        search_str = ""
        for word in to_search:
            search_str += word + "+"
        print(f"Searching {search_str}...")
        small_tasks.search_web(search_str)

    if "song" in command.split()[0]:
        song = command.split()[1:]
        song_str = ""
        for word in song:
            song_str += word + " "
        print(f"Downloading {song_str}\b...")
        Song_Downloader.download_song(query=song_str)

#todo
