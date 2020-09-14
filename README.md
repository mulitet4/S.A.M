# voice_commands_automation
S.A.M stands for Salty.Assistant.Machine

Automating boring stuff using voice commands, using the -
1. Speech_Recognition library, 
2. SoundDevice, 
3. SoundFile,
4. PyAutoGUI
5. ffmpeg-python
6. google api
7. youtube-dl

Features:
1. Opens whichever program you have - just say "open {program name}"
2. types whatever you want - say "write {sentence}"
3. search your browser - say "search {query}"

(hasnt been implemented yet)
4. download a song - say "download {song}"

The bot sends data to Google to process, otherwise this would have been a near impossible project, atleast for now! My bot basically takes mic input, processes it and does whatever is asked! 

speech.wav is overwritten everytime the script is run, but it will also be created automatically if deleted.

Bot name - S.A.M
Salty.Assistant.Machine

if you want to use the bot yourself, clone the repository, install the modules listed above, and run bot.py, nothing else.
