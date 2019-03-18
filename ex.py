import sol
from tkinter import *

r=Tk()
f=Frame(r)
f.pack()

g=[[0 for i in range(9)] for j in range(9)]
entries = [[0 for i in range(9)] for j in range(9)]

def newsu():
    for i in range(9):
        for j in range(9):
            if (0<=i<=2 and (0<=j<=2 or 6<=j<=8))or(6<=i<=8 and (0<=j<=2 or 6<=j<=8))or(3<=i<=5 and 3<=j<=5):
                entries[i][j] = Entry(f, width=4, bg="black", fg="white", font=("Calibri,20"), justify="center")
                entries[i][j].grid(row=i, column=j, ipadx=10, ipady=15)
            else:
                entries[i][j] = Entry(f, width=4, font=("Calibri,20"), justify="center")
                entries[i][j].grid(row=i, column=j, ipadx=10, ipady=15)


def onPress():
    for i in range(9):
        for j in range(9):
            try:
                g[i][j] = int(entries[i][j].get())
            except:
                g[i][j]=0
    sol.abc(g)

newsu()
f1=Frame(r)
f1.pack()
b1=Button(f1,text='Solve',bg="green",fg="white", font="times 20", command=onPress)
b1.pack(side=LEFT)
b2=Button(f1,text='Clear All',font="times 20", command=newsu)
b2.pack(side=LEFT)


r.title('Sudoku')
r.mainloop()
