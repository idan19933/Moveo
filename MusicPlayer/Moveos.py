import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
music_player = tkr.Tk()
music_player.title("My Music Player")
music_player.geometry("450x350")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()
play_list = tkr.Listbox(music_player, font="Helvetica 10 bold", bg='yellow', selectmode=tkr.SINGLE)
for item in song_list:
   pos = 0
   play_list.insert(pos, item)
   pos += 1
for i in play_list.curselection():
   print(play_list.get(i))
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
var = tkr.StringVar()
def play():
   pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
   var.set(play_list.get(tkr.ACTIVE))


   pygame.mixer.music.play()
def stop():
   pygame.mixer.music.stop()
def pause():
   pygame.mixer.music.pause()
def unpause():
   pygame.mixer.music.unpause()
song_title = tkr.Label(music_player, font="Helvetica 10 bold", textvariable=var)
Button1 = tkr.Button(music_player, width=4, height=2, font="Helvetica 10 bold", text="PLAY", command=play, bg="blue", fg="white")
Button2 = tkr.Button(music_player, width=4, height=2, font="Helvetica 10 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, width=4, height=2, font="Helvetica 10 bold", text="PAUSE", command=pause, bg="purple", fg="white")
Button4 = tkr.Button(music_player, width=4, height=2, font="Helvetica 10 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")


song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")

music_player.mainloop()