from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

frames = None
color_list = ['red','brown','red','brown','red','brown','red','brown','red']
sounds = ['sound1','sound2','sound3','sound4','sound5','sound1','sound1','sound1','sound1']
for lable in range(9):
    my_lable = Label(root,bg=color_list[lable])
    my_lable.pack(side=BOTTOM,fill='x')
    my_lable.config(text=sounds[lable])


bottomframe = Label(root,bg="red")
bottomframe.pack( side=BOTTOM,fill='x' )
bottomframe.config(text="sound1")
redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

# blackbutton = Button(bottomframe, text="Black", fg="black")
# blackbutton.pack( side = BOTTOM)

root.mainloop()