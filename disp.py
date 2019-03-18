from tkinter import *


def grid(g):
    r=Tk()
    for i in range(9):
        for j in range(9):
            if (0<=i<=2 and (0<=j<=2 or 6<=j<=8))or(6<=i<=8 and (0<=j<=2 or 6<=j<=8))or(3<=i<=5 and 3<=j<=5):
                e = Entry(r, width=4, bg="black", fg="white", font=("Calibri,20"), justify="center")
                e.grid(row=i, column=j, ipadx=10, ipady=15)
            else:
                e = Entry(r, width=4, font=("Calibri,20"), justify="center")
                e.grid(row=i, column=j, ipadx=10, ipady=15)
            e.insert(END, '%d' % (g[i][j]))
    r.title('Solution')
    r.mainloop()
    

def inv():
    master=Tk()
    master.geometry("200x100")
    w = Message(master, text="Invalid Entry")
    w.config(font="calibri 20", padx=10, pady=10)
    w.pack()
    b=Button(master, text="Exit", command=quit)
    b.pack()
    master.mainloop()


