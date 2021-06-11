from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()

root.title("Clock")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string,font=("Arial",34))
    label.after(1000, time)



label = Label(root, background="black", foreground="cyan")

label.pack(anchor="center")
time()

mainloop()