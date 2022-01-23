import tkinter as tk
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Grid')

lbl1 = Label(text='Name')
lbl1.grid(row=0, column=0, padx=5, pady=5, sticky=W)

entry = Entry()
entry.grid(row=0, column=1)

lbl2 = Label(text='Address')
lbl2.grid(row=1, column=0, padx=5, pady=5)

entry2 = Entry()
entry2.grid(row=1, column=1, padx=5)

root.mainloop()
