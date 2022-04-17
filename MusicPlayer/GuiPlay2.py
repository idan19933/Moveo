from tkinter import *
from tkinter.filedialog import askdirectory
import os
import tkinter as tkr
import tkinter.ttk as ttk
import pygame
from multiprocessing import Process
# Create slider function
def slide():
   pass



music_player = Tk()
topFrame = Frame(music_player)
topFrame.pack()
leftFrame = Frame(music_player)
leftFrame.pack(side=LEFT)
music_player.geometry("1280x960")
# lable1 = Label(root,text="Lable one",bg="yellow", fg="blue")
# lable1.pack(side=RIGHT,fill=Y)
# lable2 = Label(root,text="Lable two",bg="yellow", fg="blue")
# lable2.pack(side=TOP ,fill=X)
def play():
   song2 = pygame.mixer.music.load(play_list.get(1))
   pygame.mixer.music.play()


def play2():
   song2 = pygame.mixer.music.load(play_list.get(0))
   pygame.mixer.music.play()


def play3():
   return play(), play()

start = Button(music_player,text="Start", fg="green", bg="black", command=play)
start.pack(side=BOTTOM, fill=X)
start2 = Button(music_player,text="Start", fg="green", bg="black",command=play2)
start2.pack(side=BOTTOM, fill=X)
pause = Button(music_player,text="Start All", fg="green", bg="black",command=play3)
pause.pack(side=BOTTOM,fill="x")
unpause = Button(music_player,text="Unpause", fg="green", bg="black")
unpause.pack(side=BOTTOM,fill="x")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()
play_list = tkr.Listbox(music_player, font="Helvetica 10 bold", bg='yellow', selectmode=tkr.SINGLE,)
play_list.pack(side=BOTTOM,fill="x")

pos = 0
for item in song_list:
   play_list.insert(pos, item)
   pos += 1
my_slider2 = ttk.Scale(music_player,from_=0 ,to=100, orient=HORIZONTAL,value=0,command=slide)
my_slider2.pack(side=BOTTOM,fill="x",pady=20)

play_list2 = tkr.Listbox(music_player, font="Helvetica 10 bold", bg='green', selectmode=tkr.SINGLE,)
play_list2.pack(side=BOTTOM,fill="x")
pos = 0
for item in song_list:
   play_list2.insert(pos, item)
   pos += 1

for i in play_list.curselection():
   print(play_list.get(i))
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
var = tkr.StringVar()


processes = []
if __name__=='__main__':
   processes.append(Process(target=play))
   processes.append(Process(target=play2))
   for process in processes:
      process.start()
      process.join()



my_slider = ttk.Scale(music_player,from_=0 ,to=100, orient=HORIZONTAL,value=0,command=slide)
my_slider.pack(side=BOTTOM,fill="x",pady=20)






music_player.mainloop()