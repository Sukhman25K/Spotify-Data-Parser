import json
from tkinter import filedialog
import tkinter as tk

TotalTime = 0
Songs = {}
Artists = {}

root = tk.Tk()
root.withdraw()
FileName = filedialog.askopenfilename(defaultextension='.json',filetypes=[('JSON Files', '*.json')])


try:
    with open(FileName,'r',encoding='utf-8') as File:
        Data = json.load(File)
        for song in Data:
            TotalTime += song['msPlayed']

            if song['trackName'] in Songs:
                Songs[song['trackName']] += 1
            elif song['trackName'] != 'Unknown Track':
                Songs[song['trackName']] = 1
            
            if song['artistName'] in Artists:
                Artists[song['artistName']] += song['msPlayed']/60000
            elif song['artistName'] != 'Unknown Artist':
                Artists[song['artistName']] = song['msPlayed']/60000

        Songs_Sorted = dict(sorted(Songs.items(),key=lambda item: item[1],reverse=True)[:5])
        Artists_Sorted = {key: round(value,2) for key,value in sorted(Artists.items(),key=lambda item: item[1],reverse=True)[:5]}

        print(f"Total minutes: {round(TotalTime/60000,2)} \n")

        print('Your top 5 tracks:')
        for track,plays in Songs_Sorted.items():
            print(f"{track} : {plays} times")
        print('\nYour top 5 artists:')
        for artist,minutes in Artists_Sorted.items():
            print(f"{artist} : {minutes} minutes")
except:
    print('File not found or unable to open the file')