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
    full_path = []
    sound_items = []
    channel_list = []
    set_loop_type_button = None
    uploade_songs_button = None
    is_loop = False
    playBut = None

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
        for index in range(self.num_of_chanells):
            self.channel_list.append(pygame.mixer.Channel(index))
        print(self.channel_list)
        pygame.mixer.music.load('C:/Users/97254/PycharmProjects/Execercises/MyMusicPlayer/sound1.mp3')
        pygame.mixer.music.set_volume(0)

        # for channel in range(len(channel_list)):
        #     channel_list[channel].play(
        #         pygame.mixer.Sound('C:/Users/97254/PycharmProjects/Execercises/MyMusicPlayer/sound1.mp3'))


    def init_ui(self):
        root = tk.Tk()
        self.root = root
        self.ToggelLoop()

        self.uploade_songs_button = Button(self.root, text="Uploade songs", fg="green", bg="black", command=self.UplodeSounds)
        self.uploade_songs_button.pack(side=BOTTOM)

        self.root.geometry("480x480")


    def check_event(self):
        self.MUSIC_END = pygame.USEREVENT + 1
        for event in pygame.event.get():
            if event.type == self.MUSIC_END:
                print('music end event')

        self.root.after(1, self.check_event)

    def play(self):
        loopType = 0
        if self.is_loop:
            loopType = -1
        index = 0
        pygame.mixer.music.load(f'{self.full_path[0]}')
        pygame.mixer.music.play()
        for sound in self.sound_items:
            self.channel_list[index].play(pygame.mixer.Sound(sound))
            index += 1

        self.check_event()



    def UplodeSounds(self):
        directory = askdirectory()
        os.chdir(directory)
        sound_file_names = os.listdir()

        index = 0
        for sound_name in sound_file_names:
            full_path = f"{directory}/{sound_name}"
            print(full_path)

            self.full_path.append(full_path)
            sound = pygame.mixer.Sound(full_path)
            self.sound_items.append(sound)
            index +=1
        if len(self.sound_items) > 0:
            self.uploade_songs_button.destroy()
            self.playBut = Button(self.root, text="Play", fg="green", bg="black", command=self.play)
            self.playBut.pack(side=BOTTOM)


    def ToggelLoop(self):
        button_name = ""
        print("hey")
        if self.is_loop:
            self.is_loop = False
            button_name = "Not Looping"
        else:
            self.is_loop = True
            button_name = "Looping"

        if self.set_loop_type_button == None:
            self.set_loop_type_button = Button(self.root, text=button_name, fg="green", bg="black",
                                               command=self.ToggelLoop)
            self.set_loop_type_button.pack(side=BOTTOM)
        else:
            self.set_loop_type_button.config(text=button_name)

    # --- main ---

mp = MusicPlayer()
MusicPlayer.start(mp)



    # pygame.quit()