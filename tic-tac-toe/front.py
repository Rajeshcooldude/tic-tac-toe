from tkinter import *
from tkinter import ttk
import os

def callback():
    filename = 'gui.py'
    os.system(filename)


root = Tk()
root.geometry("500x500")
'''label = ttk.Label(root,text="TIC TAC TOE" ,foreground="Red")
label.place(x=150, y=60)
label.config(font=("Georgia", 20))'''
photo = PhotoImage(file="tictactoe.gif")
Resize_photo=photo.subsample(4,4)
label1 = Label(root, image=Resize_photo)
label1.place(x=100,y=50)
photo = PhotoImage(file="image.png")
Resize_photo1=photo.subsample(1,1)
label2 = Label(root, image=Resize_photo1)
label2.place(x=120,y=150)

button = ttk.Button(root,text="PLAY GAME",width=30,command=callback)
button.place(x=150,y=390)
def Buclick():
    print("button clicked")
    #button.state(['disabled'])
    #root.destroy()
button.config(command=Buclick())

root.mainloop()