#! /usr/bin/env python3

import tkinter as tk
import pygame as pg
from os import listdir, chdir
from functools import partial
import re


class MusicPlayer:
    def __init__(self, parent):
        self.parent = parent
        self.parent.columnconfigure(0, weight=1, uniform='cols')
        self.parent.columnconfigure(1, weight=1, uniform='cols')
        self.parent.rowconfigure(0, weight=1)

        self.mytext = None

        pg.init()
        pg.mixer.init()

        track_label_frame = tk.LabelFrame(self.parent, text='Track')
        track_label_frame.grid(column=0, row=0, sticky='new')
        for i in range(2):
            track_label_frame.grid_columnconfigure(i, weight=3, uniform='labels')

        self.label = tk.Label(track_label_frame, text=None, bg='lightblue')
        self.label['relief'] = 'groove'
        self.label.grid(column=1, row=0, sticky='new')

        self.status = tk.Label(track_label_frame, text=None, bg='lightblue')
        self.status['relief'] = 'groove'
        self.status.grid(column=0, row=0, sticky='new')

        btn_label_frame = tk.LabelFrame(self.parent, text='Controls')
        btn_label_frame.grid(column=0, row=1, sticky='new')
        for i in range(4):
            btn_label_frame.grid_columnconfigure(i, weight=3, uniform='btns')

        self.btn_play = tk.Button(btn_label_frame, text='Play')
        self.btn_play['command'] = partial(self.play, state=0)
        self.btn_play.grid(column=0, row=0, sticky='new', padx=3, pady=2)

        btn_stop = tk.Button(btn_label_frame, text='Stop')
        btn_stop['command'] = partial(self.play, state=None)
        btn_stop.grid(column=1, row=0, sticky='new', padx=3, pady=2)

        btn_next = tk.Button(btn_label_frame, text='Next')
        btn_next['command'] = partial(self.nextsong)
        btn_next.grid(column=2, row=0, sticky='new', padx=3, pady=2)

        track_list_frame = tk.LabelFrame(self.parent, text='Track List')
        track_list_frame.grid(column=1, row=0, rowspan=2, sticky='news')
        track_list_frame.grid_columnconfigure(0, weight=3)
        track_list_frame.grid_rowconfigure(0, weight=3)

        scrollbar = tk.Scrollbar(track_list_frame, orien='vertical')
        self.playlist = tk.Listbox(track_list_frame, yscrollcommand=scrollbar.set, \
                                   selectbackground='lightblue', selectforeground='navy', selectmode='single', width=50)
        scrollbar.grid(column=1, row=0, sticky='news')
        scrollbar.config(command=self.playlist.yview)
        self.playlist.grid(column=0, row=0, sticky='news')

        chdir('C:/Users/97254/PycharmProjects/Execercises/MusicPlayer')
        songs = listdir()
        for song in songs:
            self.playlist.insert(tk.END, song)

    def play(self, state):
        if state == 0:
            display_label = self.playlist.get(tk.ACTIVE)[:-4]
            patt = r'\w+\s\w+'
            label = ' '.join(re.findall(patt, display_label))
            self.label['text'] = label
            self.status['text'] = 'Now Playing'

            pg.mixer.music.load(self.playlist.get(tk.ACTIVE))
            pg.mixer.music.play()
            self.btn_play['text'] = 'Pause'
            self.btn_play['command'] = partial(self.play, state=1)
            if not self.playlist.curselection():
                self.playlist.select_set(0)
            else:
                self.playlist.select_set(self.playlist.curselection()[0])

        elif state == 1:
            self.status['text'] = 'Paused'
            pg.mixer.music.pause()
            self.btn_play['text'] = 'Play'
            self.btn_play['command'] = partial(self.play, state=2)
        elif state == 2:
            self.status['text'] = 'Now Playing'
            pg.mixer.music.unpause()
            self.btn_play['text'] = 'Pause'
            self.btn_play['command'] = partial(self.play, state=1)
        else:
            self.status['text'] = 'Stopped'
            pg.mixer.music.stop()
            self.btn_play['command'] = partial(self.play, state=0)
            self.btn_play['text'] = 'Play'

    def nextsong(self):
        pg.mixer.music.stop()
        select_index = self.playlist.curselection()
        next_select = 0

        if len(select_index) > 0:
            last_select = int(select_index[-1])

            self.playlist.selection_clear(select_index)

            if last_select < self.playlist.size() - 1:
                next_select = last_select + 1
        self.playlist.activate(next_select)
        self.playlist.selection_set(next_select)
        self.play(state=0)


def main():
    root = tk.Tk()
    root.title('Tkinter Music Player')
    MusicPlayer(root)
    root.mainloop()


main()