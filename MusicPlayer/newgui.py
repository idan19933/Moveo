from tkinter import *
from tkinter.filedialog import askdirectory
import os
import tkinter as tkr
import tkinter.ttk as ttk
import pygame
import threading
from pygame.mixer import music as music



# def add_sounds():
#      for song in song_list:
#         pygame.mixer.sound.play()
#



class MusicPlayer():
    sound_items = []
    tk = None
    is_loop = False
    set_loop_type_button = None
    uploade_songs_button = None
    playBut = None
    full_path = []

    def start(self):
        print("Me")
        self.init_ui()
        self.init_pygame()
        self.tk.mainloop()

    def init_pygame(self):
        pygame.init()
        pygame.mixer.init()

    def init_ui(self):
        tk = Tk()
        # bottomFrame = Frame(fill="x")
        # bottomFrame.pack()
        self.uploade_songs_button = Button(tk, text="Uploade songs", fg="green", bg="black", command=self.UplodeSounds)
        self.uploade_songs_button.pack(side=BOTTOM)
        self.ToggelLoop()
        tk.geometry("480x480")
        self.tk = tk


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
            self.playBut = Button(self.tk, text="Play", fg="green", bg="black", command=self.Play)
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
            self.set_loop_type_button = Button(self.tk, text=button_name, fg="green", bg="black",
                                               command=self.ToggelLoop)
            self.set_loop_type_button.pack(side=BOTTOM)
        else:
            self.set_loop_type_button.config(text=button_name)



    def Play(self):
        loopType = 0
        if self.is_loop:
            loopType = -1

        index = 0
        SONG_END = pygame.USEREVENT+1
        print(self.sound_items)
        pygame.mixer.music.set_endevent(SONG_END)
        pygame.mixer.music.load(f'{self.full_path[0]}')
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.play()
        for sound in self.sound_items:
            chanel = pygame.mixer.Channel(index)
            # pygame.mixer.Channel.set_endevent()
            chanel.play(sound, loopType)
            index += 1


        self.check_event()

    def check_event(self):
        print("Hey2")
        MUSIC_END = pygame.USEREVENT + 1
        for event in pygame.event.get():
            if event.type == MUSIC_END:
                print('music end event')



        #
        # running = True
        # while running:
        #
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             running = False
        #
        #         if event.type == SONG_END:
        #             print('music end event')
        #
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             # play again
        #             pygame.mixer.music.play()






    # __doc__ (as of 2008-08-02) for pygame.mixer.Channel.get_endevent:

    # Channel.get_endevent(): return type
    # get the event a channel sends when playback stops





mp = MusicPlayer()
MusicPlayer.start(mp)

