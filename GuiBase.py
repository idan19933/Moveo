import pygame
import tkinter as tk


root = tk.Tk()
def check_event():
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            print('music end event')
            label['text'] = ''

    root.after(1, check_event)

def play():
    label['text'] = 'playing'
    pygame.mixer.music.play()

# --- main ---

pygame.init()
num_of_chanells = 9
MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)
pygame.mixer.set_num_channels(num_of_chanells)
channel_list = []
index = 0
for index in range(num_of_chanells):
    channel_list.append(pygame.mixer.Channel(index))

pygame.mixer.music.load('C:/Users/97254/PycharmProjects/Execercises/MyMusicPlayer/sound1.mp3')
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play()
for channel in range(len(channel_list)):
    channel_list[channel].play(pygame.mixer.Sound('C:/Users/97254/PycharmProjects/Execercises/MyMusicPlayer/sound1.mp3'))
check_event()






label = tk.Label(root)
label.pack()

button = tk.Button(root, text='Play', command=play)
button.pack()




root.mainloop()

pygame.quit()