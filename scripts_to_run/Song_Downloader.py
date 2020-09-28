#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
import os
import youtube_dl
import pydub
from time import sleep
from googleapiclient.discovery import build

pydub.AudioSegment.converter = "C:/FFmpeg/bin/ffmpeg.exe"

api_key = 'AIzaSyDnRq2F3eT2IHXQkZsZDzjO_1v_JvY7HsQ'
youtube = build('youtube', 'v3', developerKey=api_key)

pydub.AudioSegment.ffmpeg = "C:/FFmpeg/bin/ffmpeg.exe"

ydl_opts = {
    'format': 'bestaudio/best',
    'keepvideo': False,
    'outtmpl': '%(id)s.webm',
}

def download_song(query: str):
    res = youtube.search().list(q=query, part='snippet', type='video', maxResults=1)

    req = res.execute()

    for item in req['items']:
        print(item['snippet']['title'])
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['https://www.youtube.com/watch?v=' + item['id']['videoId']])

    print(item['snippet']['title']+"-"+item['id']['videoId']+".webm")
    song = pydub.AudioSegment.from_file(item['id']['videoId']+".webm")
    song.export("songs/"+item['snippet']['title']+'.mp3', format="mp3")

    os.remove(item['id']['videoId']+".webm")