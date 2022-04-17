from tkinter import *
from tkinter.filedialog import askdirectory
import os
import tkinter as tk
import tkinter.ttk as ttk
import pygame
import threading
from pygame.mixer import music as music

class MusicPlayer():
    root = None
    MUSIC_END = pygame.USEREVENT+1
    num_of_chanells = 9

    def start(self):
        print("Me")
        self.init_ui()
        self.init_pygame()
        self.root.mainloop()

    def init_pygame(self):
        pygame.init()
        # pygame.mixer.init()


        pygame.mixer.music.set_endevent(self.MUSIC_END)
        pygame.mixer.set_num_channels(self.num_of_chanells)
        channel_list = []
        # index = 0
        for index in range(self.num_of_chanells):
            channel_list.append(pygame.mixer.Channel(index))

        pygame.mixer.music.load('C:/Users/97254/PycharmProjects/Execercises/MyMusicPlayer/sound1.mp3')
        pygame.mixer.music.set_volume(0)
        pygame.mixer.music.play()
        for channel in range(len(channel_list)):
            channel_list[channel].play(
                pygame.mixer.Sound('C:/Users/97254/PycharmProjects/Execercises/MyMusicPlayer/sound1.mp3'))
        self.check_event()

    def init_ui(self):
        root = tk.Tk()
        self.root = root

        # bottomFrame = Frame(fill="x")
        # bottomFrame.pack()
        # self.uploade_songs_button = Button(tk, text="Uploade songs", fg="green", bg="black", command=self.UplodeSounds)
        # self.uploade_songs_button.pack(side=BOTTOM)
        # self.ToggelLoop()
        # tk.geometry("480x480")
        # self.tk = tk

    def check_event(self):
        self.MUSIC_END = pygame.USEREVENT + 1
        for event in pygame.event.get():
            if event.type == self.MUSIC_END:
                print('music end event')

        self.root.after(1, self.check_event)

    def play(self):

        pygame.mixer.music.play()

    # --- main ---

mp = MusicPlayer()
MusicPlayer.start(mp)