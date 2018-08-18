from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("TIC TAC TOE: PLAYER 1")
root.resizable(True,True)




player = 1
p1 = []
p2 = []

B1 = ttk.Button(root, text=' ')
B1.grid(row=0, column=0, sticky='new', ipadx=40, ipady=40)
B1.config(command=lambda: ButtonClick(1))

B2 = ttk.Button(root, text=' ')
B2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
B2.config(command=lambda: ButtonClick(2))

B3 = ttk.Button(root, text=' ')
B3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
B3.config(command=lambda: ButtonClick(3))

B4 = ttk.Button(root, text=' ')
B4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
B4.config(command=lambda: ButtonClick(4))

B5 = ttk.Button(root, text=' ')
B5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
B5.config(command=lambda: ButtonClick(5))

B6 = ttk.Button(root, text=' ')
B6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
B6.config(command=lambda: ButtonClick(6))

B7 = ttk.Button(root, text=' ')
B7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
B7.config(command=lambda: ButtonClick(7))

B8 = ttk.Button(root, text=' ')
B8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
B8.config(command=lambda: ButtonClick(8))

B9 = ttk.Button(root, text=' ')
B9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
B9.config(command=lambda: ButtonClick(9))


def ButtonClick(id):
    global player
    global p1
    global p2
    if(player == 1):
        setLayout(id , "X")
        p1.append(id)
        root.title("TIC TAC TOE: PLAYER 2")
        player = 2
        print("p1:{}".format(p1))
    elif(player == 2):
        setLayout(id , "O")
        p2.append(id)
        root.title("TIC TAC TOE: PLAYER 1")
        player = 1
        print("p2:{}".format(p1))
    checkWinner()


def setLayout(id, symbol):
    if(id == 1):
        B1.config(text=symbol)
        B1.state(['disabled'])
    elif(id == 2):
        B2.config(text=symbol)
        B2.state(['disabled'])
    elif (id == 3):
        B3.config(text=symbol)
        B3.state(['disabled'])
    elif (id == 4):
        B4.config(text=symbol)
        B4.state(['disabled'])
    elif (id == 5):
        B5.config(text=symbol)
        B5.state(['disabled'])
    elif (id == 6):
        B6.config(text=symbol)
        B6.state(['disabled'])
    elif (id == 7):
        B7.config(text=symbol)
        B7.state(['disabled'])
    elif (id == 8):
        B8.config(text=symbol)
        B8.state(['disabled'])
    elif (id == 9):
        B9.config(text=symbol)
        B9.state(['disabled'])


def checkWinner():
    winer = -1

    if((1 in p1) and (2 in p1) and (3 in p1)):
        winer = 1
    if((1 in p2) and (2 in p2 )and (3 in p2)):
        winer = 2
    if ((4 in p1) and (5 in p1) and (6 in p1)):
        winer = 1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winer = 2
    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winer = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winer = 2
    if ((1 in p1) and (4 in p1) and (7 in p1)):
        winer = 1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winer = 2
    if ((2 in p1) and (5 in p1) and (8 in p1)):
        winer = 1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        winer = 2
    if ((3 in p1) and (6 in p1) and (9 in p1)):
        winer = 1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        winer = 2
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winer = 1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winer = 2
    if ((3 in p1) and (5 in p1) and (9 in p1)):
        winer = 1
    if ((3 in p2) and (5 in p2) and (9 in p2)):
        winer = 2

    if (winer == 1):
        messagebox.showinfo(title="CONGRATES", message="PLAYER1 IS WINNER")
        answer=messagebox.askquestion(title="exit", message =" EXIT")
        if (answer == "yes"):
            root.destroy()
        else:
            p1.clear()
    elif(winer == 2):
        messagebox.showinfo(title="CONGRATES", message="PLAYER2 IS WINNER")
        answer=messagebox.askquestion(title="exit", message=" EXIT")
        if (answer == "yes"):
            root.destroy()
        else:
            p2.clear()
    else:
        checkDraw()
def checkDraw():
    if (len(p1)==5 or len(p2)==5):
       messagebox.showinfo(title="DRAW", message="GAME DRAW")
       answer = messagebox.askquestion(title="exit", message=" EXIT")
       if (answer == "yes"):
           root.destroy()
       else:
           p2.clear()

root.mainloop()
